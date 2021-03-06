from PyQt5 import QtCOre, QtGui, QtWidgets

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
            MainWindow.resize(451, 671)
            MainWindow.setStyleSheet(u"background-color: rgb(158, 255, 164);")
            self.centralwidget = QtWidget(MainWindow)
            self.centralwidget.setObjectName(u"centralwidget")
            self.meaning = QLabel(self.centralwidget)
            self.meaning.setObjectName(u"meaning")
            self.meaning.setGeometry(QRect(10, 0, 431, 100))
            self.meaning.setStyleSheet(u"background-color: rgb(170, 170, 255);")
            self.pushButton_equally = QPushButton(self.centralwidget)
            self.pushButton_equally.setObjectName(u"pushButton_equally")
            self.pushButton_equally.setGeometry(QRect(230, 440, 100, 100))
            font = QFont()
            font.setFamily(u"Calibri")
            font.setPointSize(48)
            self.pushButton_equally.setFont(font)
            self.pushButton_equally.setStyleSheet(u"background-color: rgb(255, 170, 255);")
            self.pushButtom_zero = QPushButton(self.centralwidget)
            self.pushButtom_zero.setObjectName(u"pushButtom_zero")
            self.pushButtom_zero.setGeometry(QRect(10, 440, 100, 100))
            self.pushButtom_zero.setFont(font)
            self.pushButtom_zero.setStyleSheet(u"background-color: rgb(255, 170, 255);")
            self.pushButton_point = QPushButton(self.centralwidget)
            self.pushButton_point.setObjectName(u"pushButton_point")
            self.pushButton_point.setGeometry(QRect(120, 440, 100, 100))
            self.pushButton_point.setFont(font)
            self.pushButton_point.setStyleSheet(u"background-color: rgb(255, 170, 255);")
            self.pushButton_share = QPushButton(self.centralwidget)
            self.pushButton_share.setObjectName(u"pushButton_share")
            self.pushButton_share.setGeometry(QRect(340, 440, 100, 100))
            self.pushButton_share.setFont(font)
            self.pushButton_share.setStyleSheet(u"background-color: rgb(255, 170, 255);")
            self.pushButton_factorial = QPushButton(self.centralwidget)
            self.pushButton_factorial.setObjectName(u"pushButton_factorial")
            self.pushButton_factorial.setGeometry(QRect(230, 550, 100, 100))
            self.pushButton_factorial.setFont(font)
            self.pushButton_factorial.setStyleSheet(u"background-color: rgb(255, 170, 255);")
            self.pushButton_18 = QPushButton(self.centralwidget)
            self.pushButton_18.setObjectName(u"pushButton_18")
            self.pushButton_18.setGeometry(QRect(10, 550, 100, 100))
            self.pushButton_18.setFont(font)
            self.pushButton_18.setStyleSheet(u"background-color: rgb(255, 170, 255);")
            self.pushButton_square_root = QPushButton(self.centralwidget)
            self.pushButton_square_root.setObjectName(u"pushButton_square_root")
            self.pushButton_square_root.setGeometry(QRect(120, 550, 100, 100))
            self.pushButton_square_root.setFont(font)
            self.pushButton_square_root.setStyleSheet(u"background-color: rgb(255, 170, 255);")
            self.pushButton_C = QPushButton(self.centralwidget)
            self.pushButton_C.setObjectName(u"pushButton_C")
            self.pushButton_C.setGeometry(QRect(340, 550, 100, 100))
            font1 = QFont()
            font1.setFamily(u"Calibri")
            font1.setPointSize(48)
            font1.setBold(False)
            font1.setWeight(50)
            self.pushButton_C.setFont(font1)
            self.pushButton_C.setStyleSheet(u"background-color: rgb(255, 170, 255);")
            self.pushButton_multiply = QPushButton(self.centralwidget)
            self.pushButton_multiply.setObjectName(u"pushButton_multiply")
            self.pushButton_multiply.setGeometry(QRect(340, 330, 100, 100))
            self.pushButton_multiply.setFont(font)
            self.pushButton_multiply.setStyleSheet(u"background-color: rgb(255, 170, 255);")
            self.pushButton_nine = QPushButton(self.centralwidget)
            self.pushButton_nine.setObjectName(u"pushButton_nine")
            self.pushButton_nine.setGeometry(QRect(230, 330, 100, 100))
            self.pushButton_nine.setFont(font)
            self.pushButton_nine.setStyleSheet(u"background-color: rgb(255, 170, 255);")
            self.pushButtom_seven = QPushButton(self.centralwidget)
            self.pushButtom_seven.setObjectName(u"pushButtom_seven")
            self.pushButtom_seven.setGeometry(QRect(10, 330, 100, 100))
            self.pushButtom_seven.setFont(font)
            self.pushButtom_seven.setStyleSheet(u"background-color: rgb(255, 170, 255);")
            self.pushButton_eight = QPushButton(self.centralwidget)
            self.pushButton_eight.setObjectName(u"pushButton_eight")
            self.pushButton_eight.setGeometry(QRect(120, 330, 100, 100))
            self.pushButton_eight.setFont(font)
            self.pushButton_eight.setStyleSheet(u"background-color: rgb(255, 170, 255);")
            self.pushButton_minus = QPushButton(self.centralwidget)
            self.pushButton_minus.setObjectName(u"pushButton_minus")
            self.pushButton_minus.setGeometry(QRect(340, 220, 100, 100))
            self.pushButton_minus.setFont(font)
            self.pushButton_minus.setStyleSheet(u"background-color: rgb(255, 170, 255);")
            self.pushButton_six = QPushButton(self.centralwidget)
            self.pushButton_six.setObjectName(u"pushButton_six")
            self.pushButton_six.setGeometry(QRect(230, 220, 100, 100))
            self.pushButton_six.setFont(font)
            self.pushButton_six.setStyleSheet(u"background-color: rgb(255, 170, 255);")
            self.pushButtom_four = QPushButton(self.centralwidget)
            self.pushButtom_four.setObjectName(u"pushButtom_four")
            self.pushButtom_four.setGeometry(QRect(10, 220, 100, 100))
            self.pushButtom_four.setFont(font)
            self.pushButtom_four.setStyleSheet(u"background-color: rgb(255, 170, 255);")
            self.pushButton_five = QPushButton(self.centralwidget)
            self.pushButton_five.setObjectName(u"pushButton_five")
            self.pushButton_five.setGeometry(QRect(120, 220, 100, 100))
            self.pushButton_five.setFont(font)
            self.pushButton_five.setStyleSheet(u"background-color: rgb(255, 170, 255);")
            self.pushButton_plus = QPushButton(self.centralwidget)
            self.pushButton_plus.setObjectName(u"pushButton_plus")
            self.pushButton_plus.setGeometry(QRect(340, 110, 100, 100))
            self.pushButton_plus.setFont(font)
            self.pushButton_plus.setStyleSheet(u"background-color: rgb(255, 170, 255);")
            self.pushButton_three = QPushButton(self.centralwidget)
            self.pushButton_three.setObjectName(u"pushButton_three")
            self.pushButton_three.setGeometry(QRect(230, 110, 100, 100))
            self.pushButton_three.setFont(font)
            self.pushButton_three.setStyleSheet(u"background-color: rgb(255, 170, 255);")
            self.pushButtom_one = QPushButton(self.centralwidget)
            self.pushButtom_one.setObjectName(u"pushButtom_one")
            self.pushButtom_one.setGeometry(QRect(10, 110, 100, 100))
            self.pushButtom_one.setFont(font)
            self.pushButtom_one.setStyleSheet(u"background-color: rgb(255, 170, 255);")
            self.pushButton_two = QPushButton(self.centralwidget)
            self.pushButton_two.setObjectName(u"pushButton_two")
            self.pushButton_two.setGeometry(QRect(120, 110, 100, 100))
            self.pushButton_two.setFont(font)
            self.pushButton_two.setStyleSheet(u"background-color: rgb(255, 170, 255);")
            MainWindow.setCentralWidget(self.centralwidget)
            self.menubar = QMenuBar(MainWindow)
            self.menubar.setObjectName(u"menubar")
            self.menubar.setGeometry(QRect(0, 0, 451, 21))
            MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.meaning.setText("")
        self.pushButton_equally.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.pushButtom_zero.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_point.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.pushButton_share.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.pushButton_factorial.setText(QCoreApplication.translate("MainWindow", u"!", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"^", None))
        self.pushButton_square_root.setText(QCoreApplication.translate("MainWindow", u"\u221a", None))
        self.pushButton_C.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.pushButton_multiply.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.pushButton_nine.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButtom_seven.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_eight.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_six.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButtom_four.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_five.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_three.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButtom_one.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_two.setText(QCoreApplication.translate("MainWindow", u"2", None))
    # retranslateUi


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplications(sys.argv)
    MainWindow = QtWidgets.QMainWindow()