"""Generated PyQt5 UI for the PARADOX assistant window."""

import os

from dotenv import load_dotenv
from PyQt5 import QtCore, QtGui, QtWidgets


load_dotenv()

# Load the animated assets and title image from the environment.
main_image = os.getenv('main_image')
title_image = os.getenv('title_image')
radiohalo_image = os.getenv('radiohalo_image')
motion_sphere_image = os.getenv('motion_sphere_image')
radar_image = os.getenv('radar_image')
t200w_image = os.getenv('200w_image')
reload_image = os.getenv('reload_image')
alien_image = os.getenv('alien_image')
initiating_image = os.getenv('initiating_image')


class Ui_ParadoxUI(object):
    """Build the main GUI window and its animated labels."""

    def setupUi(self, ParadoxUI):
        # Main window configuration.
        ParadoxUI.setObjectName('ParadoxUI')
        ParadoxUI.resize(1112, 841)

        # The main background label holds the primary animated image.
        self.centralwidget = QtWidgets.QWidget(ParadoxUI)
        self.centralwidget.setObjectName('centralwidget')
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1111, 851))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet('background:rgb(0, 255, 0)')
        self.label.setText('')
        self.label.setPixmap(QtGui.QPixmap(main_image))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setObjectName('label')

        # Run button starts the voice assistant in the background.
        self.Run = QtWidgets.QPushButton(self.centralwidget)
        self.Run.setGeometry(QtCore.QRect(892, 720, 151, 41))
        font = QtGui.QFont()
        font.setFamily('MS Shell Dlg 2')
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.Run.setFont(font)
        self.Run.setAutoFillBackground(False)
        self.Run.setStyleSheet(
            'border-color: rgb(255, 255, 255);\n'
            'border-color: rgb(170, 255, 0);\n\n'
            'background-color: rgb(0, 255, 0);'
        )
        self.Run.setObjectName('Run')

        # Stop button closes the window and terminates the UI session.
        self.Stop = QtWidgets.QPushButton(self.centralwidget)
        self.Stop.setGeometry(QtCore.QRect(892, 770, 151, 41))
        font = QtGui.QFont()
        font.setFamily('MS Shell Dlg 2')
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.Stop.setFont(font)
        self.Stop.setAutoFillBackground(False)
        self.Stop.setStyleSheet('background-color: rgb(255, 0, 0);')
        self.Stop.setObjectName('Stop')

        # Title banner.
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(460, 750, 221, 91))
        self.label_2.setText('')
        self.label_2.setPixmap(QtGui.QPixmap(title_image))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName('label_2')

        # Radio halo animation.
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(460, 350, 191, 141))
        self.label_3.setText('')
        self.label_3.setPixmap(QtGui.QPixmap(radiohalo_image))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName('label_3')

        # Motion sphere animation.
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 570, 361, 271))
        self.label_4.setText('')
        self.label_4.setPixmap(QtGui.QPixmap(motion_sphere_image))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName('label_4')

        # Radar animation.
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(840, 340, 251, 161))
        self.label_5.setText('')
        self.label_5.setPixmap(QtGui.QPixmap(radar_image))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName('label_5')

        # Animated text or status image.
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(460, 670, 211, 121))
        self.label_6.setText('')
        self.label_6.setPixmap(QtGui.QPixmap(t200w_image))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName('label_6')

        # Reload animation.
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(850, 110, 231, 221))
        self.label_7.setText('')
        self.label_7.setPixmap(QtGui.QPixmap(reload_image))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName('label_7')

        # Alien animation.
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(890, 590, 141, 101))
        self.label_8.setText('')
        self.label_8.setPixmap(QtGui.QPixmap(alien_image))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName('label_8')

        # Initiating animation.
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(350, 20, 401, 121))
        self.label_9.setText('')
        self.label_9.setPixmap(QtGui.QPixmap(initiating_image))
        self.label_9.setScaledContents(False)
        self.label_9.setObjectName('label_9')

        ParadoxUI.setCentralWidget(self.centralwidget)
        self.retranslateUi(ParadoxUI)
        QtCore.QMetaObject.connectSlotsByName(ParadoxUI)

    def retranslateUi(self, ParadoxUI):
        _translate = QtCore.QCoreApplication.translate
        ParadoxUI.setWindowTitle(_translate('ParadoxUI', 'P.A.R.A.D.O.X'))
        self.Run.setText(_translate('ParadoxUI', 'Run'))
        self.Stop.setText(_translate('ParadoxUI', 'TERMINATE'))


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    paradox_ui = QtWidgets.QMainWindow()
    ui = Ui_ParadoxUI()
    ui.setupUi(paradox_ui)
    paradox_ui.show()
    sys.exit(app.exec_())

