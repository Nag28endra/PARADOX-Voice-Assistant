"""Main application entry point for the PARADOX assistant."""

import json
import os
import random
import sys

import torch
from dotenv import load_dotenv
from PyQt5 import QtGui
from PyQt5.QtCore import QThread, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow

from Brain import NeuralNet
from Listen import Listen
from NeuralNetwork import bag_of_words, tokenize
from Task import InputExecution, NonInputExecution
from paradoxUI import Ui_ParadoxUI
from speak import Say


# Load all configuration variables from the environment file.
load_dotenv()

main_image = os.getenv('main_image')
title_image = os.getenv('title_image')
radiohalo_image = os.getenv('radiohalo_image')
motion_sphere_image = os.getenv('motion_sphere_image')
radar_image = os.getenv('radar_image')
t200w_image = os.getenv('200w_image')
reload_image = os.getenv('reload_image')
alien_image = os.getenv('alien_image')
initiating_image = os.getenv('initiating_image')


class MainThread(QThread):
    """Background worker that listens to speech and routes commands."""

    def __init__(self):
        super(MainThread, self).__init__()

        # Use GPU when available, otherwise fall back to CPU.
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        with open('intents.json', 'r') as file:
            self.intents = json.load(file)

        # Load the saved model metadata and weights.
        self.file_name = 'trainData.pth'
        self.data = torch.load(self.file_name)

        self.input_size = self.data['input_size']
        self.hidden_size = self.data['hidden_size']
        self.output_size = self.data['output_size']

        self.all_words = self.data['all_words']
        self.tags = self.data['tags']
        self.model_state = self.data['model_state']

        self.model = NeuralNet(self.input_size, self.hidden_size, self.output_size).to(self.device)
        self.model.load_state_dict(self.model_state)
        self.model.eval()

    def run(self):
        """Start the assistant and keep listening for commands."""
        Say('hello I am Paradox. How can I help you?')
        while True:
            self.main()

    def main(self):
        """Read a sentence, classify it, and execute the matching action."""
        self.sentence = Listen()
        self.result = str(self.sentence)

        if self.sentence == 'bye' or self.sentence == 'go to sleep':
            Say('thank You boss! See you later.')
            sys.exit()

        # Convert the user input into a bag-of-words vector.
        self.sentence = tokenize(self.sentence)
        self.x = bag_of_words(self.sentence, self.all_words)
        self.x = self.x.reshape(1, self.x.shape[0])
        self.x = torch.from_numpy(self.x).to(self.device)

        self.output = self.model(self.x)
        _, self.predicted = torch.max(self.output, dim=1)

        self.tag = self.tags[self.predicted.item()]
        self.probs = torch.softmax(self.output, dim=1)
        self.probs = self.probs[0][self.predicted.item()]

        # Only execute the action when the model is confident enough.
        if self.probs.item() > 0.75:
            for self.intent in self.intents['intents']:
                if self.tag == self.intent['tags']:
                    self.reply = random.choice(self.intent['responses'])

                    # Route commands that do not need extra text input.
                    if 'time' in self.reply:
                        NonInputExecution(self.reply)
                    elif 'date' in self.reply:
                        NonInputExecution(self.reply)
                    elif 'wikipedia' in self.reply:
                        InputExecution(self.reply, self.result)
                    elif 'search' in self.reply:
                        InputExecution(self.reply, self.result)
                    elif 'notepad' in self.reply:
                        Say('opening notepad')
                        InputExecution(self.reply, self.result)
                    elif 'cnotepad' in self.reply:
                        Say('closing notepad..')
                        InputExecution(self.reply, self.result)
                    elif 'commandprompt' in self.reply:
                        Say('opening command prompt...')
                        InputExecution(self.reply, self.result)
                    elif 'word' in self.reply:
                        Say('opening MS Word...')
                        InputExecution(self.reply, self.result)
                    elif 'powerpoint' in self.reply:
                        Say('opening MS Powerpoint...')
                        InputExecution(self.reply, self.result)
                    elif 'excel' in self.reply:
                        Say('opening MS Excel...')
                        InputExecution(self.reply, self.result)
                    elif 'brave' in self.reply:
                        Say('opening Brave Browser...')
                        InputExecution(self.reply, self.result)
                    elif 'cword' in self.reply:
                        Say('closing MS Word..')
                        InputExecution(self.reply, self.result)
                    elif 'cpowerpoint' in self.reply:
                        Say('closing MS powerpoint..')
                        InputExecution(self.reply, self.result)
                    elif 'cexcel' in self.reply:
                        Say('closing MS excel..')
                        InputExecution(self.reply, self.result)
                    elif 'cbrave' in self.reply:
                        Say('closing brave ..')
                        InputExecution(self.reply, self.result)
                    elif 'news' in self.reply:
                        InputExecution(self.reply, self.result)
                    elif 'play' in self.tag:
                        InputExecution(self.reply, self.result)
                    elif 'open youtube' in self.tag:
                        InputExecution(self.reply, self.result)
                    elif 'open google' in self.tag:
                        InputExecution(self.reply, self.result)
                    elif 'joke' in self.tag:
                        InputExecution(self.reply, self.result)
                    elif 'leaving' in self.tag:
                        sys.exit()
                        InputExecution(self.reply, self.reply)
                    else:
                        Say(self.reply)


# Create the background thread once so the GUI can start it on demand.
startExecution = MainThread()


class Main(QMainWindow):
    """PyQt5 window that hosts the PARADOX GUI assets."""

    def __init__(self):
        super().__init__()
        self.ui = Ui_ParadoxUI()
        self.ui.setupUi(self)

        # Wire the Run and Stop buttons to the assistant lifecycle.
        self.ui.Run.clicked.connect(self.startTask)
        self.ui.Stop.clicked.connect(self.close)

    def startTask(self):
        """Load the animated GIFs and launch the background worker."""
        self.ui.movie = QtGui.QMovie(main_image)
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie(radiohalo_image)
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie(motion_sphere_image)
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie(radar_image)
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie(t200w_image)
        self.ui.label_6.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie(reload_image)
        self.ui.label_7.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie(alien_image)
        self.ui.label_8.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie(initiating_image)
        self.ui.label_9.setMovie(self.ui.movie)
        self.ui.movie.start()

        timer = QTimer(self)
        timer.start(1000)
        startExecution.start()


app = QApplication(sys.argv)
paradox = Main()
paradox.show()
exit(app.exec_())
