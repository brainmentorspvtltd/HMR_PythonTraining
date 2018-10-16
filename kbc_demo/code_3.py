# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'code_1.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap
import pygame
pygame.mixer.init()

sound_1 = pygame.mixer.Sound('sound_2.wav')

class Ui_Dialog(QtWidgets.QMainWindow):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1085, 735)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1085, 731))
        self.frame.setStyleSheet("background-color: rgb(249, 249, 249);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_img = QtWidgets.QLabel(self.frame)
        self.label_img.setGeometry(QtCore.QRect(0, 0, 1085, 735))
        pixmap = QPixmap("kbc_.png")
        self.label_img.setPixmap(pixmap)
        # self.label = QtWidgets.QLabel(self.frame)
        # self.label.setGeometry(QtCore.QRect(140, 120, 791, 121))
        # self.label.setStyleSheet("font: 36pt \"MS Shell Dlg 2\";")
        # self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(160, 560, 171, 101))
        self.pushButton.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(750, 560, 171, 101))
        self.pushButton_2.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 1081, 741))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(50, 180, 811, 121))
        self.label_2.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 350, 271, 101))
        self.pushButton_3.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(490, 350, 271, 101))
        self.pushButton_4.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_5.setGeometry(QtCore.QRect(60, 540, 271, 101))
        self.pushButton_5.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_6.setGeometry(QtCore.QRect(490, 540, 271, 101))
        self.pushButton_6.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.pushButton_6.setObjectName("pushButton_6")

        self.pushButton.clicked.connect(self.startGame)
        sound_1.play()

        self.frame_2.hide()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        # self.label.setText(_translate("Dialog", "Kaun Banega Crorepati"))
        self.pushButton.setText(_translate("Dialog", "Start"))
        self.pushButton_2.setText(_translate("Dialog", "Quit"))
        self.label_2.setText(_translate("Dialog", "Ques 1. Who is the prime minister of India ?"))
        self.pushButton_3.setText(_translate("Dialog", "Modi"))
        self.pushButton_4.setText(_translate("Dialog", "Yogi"))
        self.pushButton_5.setText(_translate("Dialog", "Lalu"))
        self.pushButton_6.setText(_translate("Dialog", "Arvind"))

    def startGame(self):

        self.frame_2.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

