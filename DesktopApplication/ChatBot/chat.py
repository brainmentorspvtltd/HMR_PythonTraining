from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1237, 744)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(360, 10, 571, 101))
        self.label.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 170, 641, 121))
        self.lineEdit.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(950, 230, 251, 61))
        self.pushButton.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(720, 200, 131, 81))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.image = QPixmap('mic-icon.png')
        self.label_2.setPixmap(self.image)
        self.label_2.setObjectName("image")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 410, 641, 91))
        self.lineEdit_2.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1237, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Personal ChatBot"))
        self.lineEdit.setText(_translate("MainWindow", "Enter your message..."))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.lineEdit_2.setText(_translate("MainWindow", "What Can I Do For You ?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

