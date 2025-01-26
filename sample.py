import random
import json
import torch
import Brain
from NeuralNetwork import bag_of_words,tokenize
from Listen import Listen
from speak import Say
from Brain import NeuralNet
import os 
import sys
from Task import NonInputExecution
from Task import InputExecution
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer, QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from paradoxUI import Ui_ParadoxUI
import sys


class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        with open ('intents.json','r') as self.f:
            self.intents = json.load(self.f)

        self.FILE = "trainData.pth"
        self.data = torch.load(self.FILE)

        self.input_size = self.data['input_size']
        self.hidden_size = self.data['hidden_size']
        self.output_size = self.data['output_size']

        self.all_words = self.data['all_words']
        self.tags = self.data['tags']
        self.model_state = self.data['model_state']

        self.model = NeuralNet(self.input_size,self.hidden_size,self.output_size).to(self.device)
        self.model.load_state_dict(self.model_state)
        self.model.eval()

    def run(self):
        Say('hello I am Paradox. How can I help you?')
        while True:
            self.Main()


    def Main(self):
    
        self.sentence = Listen()
        self.result = str(self.sentence)

        if self.sentence =='bye' or self.sentence =='go to sleep':
            Say('thank You boss! See you later.')
            sys.exit()
    
        self.sentence = tokenize(self.sentence)
        self.x = bag_of_words(self.sentence, self.all_words)
        self.x = self.x.reshape(1,self.x.shape[0])
        self.x = torch.from_numpy(self.x).to(self.device)

        self.output = self.model(self.x)

        _,self.predicted = torch.max(self.output,dim=1)

        self.tag = self.tags[self.predicted.item()]
        self.probs = torch.softmax(self.output,dim=1)
        self.probs = self.probs[0][self.predicted.item()]

        if self.probs.item()>0.75:
            for self.intent in self.intents['intents']:
                if self.tag == self.intent['tags']:
                    self.reply = random.choice(self.intent['responses'])
                    if 'time' in self.reply:
                        NonInputExecution(self.reply)
                    elif 'date' in self.reply:
                        NonInputExecution(self.reply)
                    elif 'wikipedia' in self.reply:
                        InputExecution(self.reply, self.result)
                    elif 'search' in self.reply:
                        InputExecution(self.reply,self.result)
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

                    
                    else:
                        Say(self.reply)

    

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ParadoxUI()
        self.ui.setupUi(self)
        self.ui.Run.clicked.connect(self.startTask)
        self.ui.Stop.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("C:/Users/NAGENDRA/OneDrive/Desktop/paradoxuitools/main.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("C:/Users/NAGENDRA/OneDrive/Desktop/paradoxuitools/radiohalo-800.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("C:/Users/NAGENDRA/OneDrive/Desktop/paradoxuitools/spheres-motion-for-ai-product-design-by-gleb-large.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("C:/Users/NAGENDRA/OneDrive/Desktop/paradoxuitools/AlarmingSecretEgg-size_restricted.gif")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("C:/Users/NAGENDRA/OneDrive/Desktop/paradoxuitools/220w.gif")
        self.ui.label_6.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("C:/Users/NAGENDRA/OneDrive/Desktop/paradoxuitools/reload.gif")
        self.ui.label_7.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("C:/Users/NAGENDRA/OneDrive/Desktop/paradoxuitools/alien.gif")
        self.ui.label_8.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("C:/Users/NAGENDRA/OneDrive/Desktop/paradoxuitools/initial.gif")
        self.ui.label_9.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        
        timer = QTimer(self)
        # timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()



app = QApplication(sys.argv)
paradox = Main()
paradox.show()
exit(app.exec_())