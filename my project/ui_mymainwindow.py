import PySide2 *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

from MainWindow import Ui_MainWindow

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def __init__(self, *args, **kwargs):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(877, 685)
        MainWindow.setStyleSheet(u"")
        self.open_file_action = QAction(MainWindow)
        self.open_file_action.setObjectName(u"open_file_action")
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setStyleSheet(u"background-color: rgb(86, 104, 129);\n"
"background-color: rgb(170, 197, 213);")
        self.verticalLayout = QVBoxLayout(self.centralWidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.playlistView = QListView(self.centralWidget)
        self.playlistView.setObjectName(u"playlistView")
        self.playlistView.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.playlistView.setAcceptDrops(True)
        self.playlistView.setStyleSheet(u"background-color: rgb(133, 160, 200);\n"
"background-color: rgb(213, 223, 236);")
        self.playlistView.setFrameShape(QFrame.NoFrame)
        self.playlistView.setFrameShadow(QFrame.Sunken)
        self.playlistView.setProperty("showDropIndicator", True)
        self.playlistView.setDragDropMode(QAbstractItemView.DropOnly)
        self.playlistView.setDefaultDropAction(Qt.CopyAction)
        self.playlistView.setAlternatingRowColors(True)
        self.playlistView.setUniformItemSizes(True)

        self.verticalLayout.addWidget(self.playlistView)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(self.centralWidget)
        self.label.setObjectName(u"label")
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setPixmap(QPixmap(u"../mediaplayer/images/speaker-volume.png"))

        self.horizontalLayout_5.addWidget(self.label)

        self.volumeSlider = QSlider(self.centralWidget)
        self.volumeSlider.setObjectName(u"volumeSlider")
        self.volumeSlider.setCursor(QCursor(Qt.SplitHCursor))
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setValue(100)
        self.volumeSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_5.addWidget(self.volumeSlider)

        self.stopButton = QPushButton(self.centralWidget)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.stopButton.setStyleSheet(u"background-color: rgb(203, 235, 255);")
        icon = QIcon()
        icon.addFile(u"pics/icons8-\u0441\u0442\u043e\u043f-90.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stopButton.setIcon(icon)
        self.stopButton.setCheckable(False)

        self.horizontalLayout_5.addWidget(self.stopButton)

        self.playButton = QPushButton(self.centralWidget)
        self.playButton.setObjectName(u"playButton")
        self.playButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.playButton.setStyleSheet(u"background-color: rgb(203, 235, 255);")
        self.playButton.setInputMethodHints(Qt.ImhNone)
        icon1 = QIcon()
        icon1.addFile(u"pics/icons8-\u0432\u043e\u0441\u043f\u0440\u043e\u0438\u0437\u0432\u0435\u0434\u0435\u043d\u0438\u0435-90.png", QSize(), QIcon.Normal, QIcon.Off)
        self.playButton.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.playButton)

        self.pauseButton = QPushButton(self.centralWidget)
        self.pauseButton.setObjectName(u"pauseButton")
        self.pauseButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pauseButton.setStyleSheet(u"background-color: rgb(203, 235, 255);")
        icon2 = QIcon()
        icon2.addFile(u"pics/icons8-\u043f\u0430\u0443\u0437\u0430-90.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pauseButton.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.pauseButton)

        self.previousButton = QPushButton(self.centralWidget)
        self.previousButton.setObjectName(u"previousButton")
        font = QFont()
        font.setFamily(u"Calibri")
        font.setBold(False)
        font.setWeight(50)
        self.previousButton.setFont(font)
        self.previousButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.previousButton.setStyleSheet(u"background-color: rgb(203, 235, 255);")
        icon3 = QIcon()
        icon3.addFile(u"pics/icons8-\u043f\u0435\u0440\u0435\u0439\u0442\u0438-\u0432-\u043d\u0430\u0447\u0430\u043b\u043e-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.previousButton.setIcon(icon3)

        self.horizontalLayout_5.addWidget(self.previousButton)

        self.nextButton = QPushButton(self.centralWidget)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.nextButton.setLayoutDirection(Qt.RightToLeft)
        self.nextButton.setStyleSheet(u"background-color: rgb(203, 235, 255);")
        icon4 = QIcon()
        icon4.addFile(u"pics/icons8-\u043f\u0435\u0440\u0435\u0439\u0442\u0438-\u0432-\u043d\u0430\u0447\u0430\u043b\u043e-96 \u2014 \u043a\u043e\u043f\u0438\u044f.png", QSize(), QIcon.Normal, QIcon.Off)
        self.nextButton.setIcon(icon4)

        self.horizontalLayout_5.addWidget(self.nextButton)

        self.viewButton = QPushButton(self.centralWidget)
        self.viewButton.setObjectName(u"viewButton")
        self.viewButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.viewButton.setStyleSheet(u"background-color: rgb(203, 235, 255);")
        icon5 = QIcon()
        icon5.addFile(u"pics/QMBM7464.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.viewButton.setIcon(icon5)
        self.viewButton.setCheckable(False)

        self.horizontalLayout_5.addWidget(self.viewButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.currentTimeLabel = QLabel(self.centralWidget)
        self.currentTimeLabel.setObjectName(u"currentTimeLabel")
        self.currentTimeLabel.setMinimumSize(QSize(80, 0))
        font1 = QFont()
        font1.setFamily(u"Calibri")
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setWeight(75)
        self.currentTimeLabel.setFont(font1)
        self.currentTimeLabel.setStyleSheet(u"")
        self.currentTimeLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.currentTimeLabel)

        self.timeSlider = QSlider(self.centralWidget)
        self.timeSlider.setObjectName(u"timeSlider")
        self.timeSlider.setCursor(QCursor(Qt.SplitHCursor))
        self.timeSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.timeSlider)

        self.totalTimeLabel = QLabel(self.centralWidget)
        self.totalTimeLabel.setObjectName(u"totalTimeLabel")
        self.totalTimeLabel.setMinimumSize(QSize(80, 0))
        self.totalTimeLabel.setFont(font1)
        self.totalTimeLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.totalTimeLabel)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 877, 21))
        self.menuFIle = QMenu(self.menuBar)
        self.menuFIle.setObjectName(u"menuFIle")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menuBar.addAction(self.menuFIle.menuAction())
        self.menuFIle.addAction(self.open_file_action)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Failamp", None))
        self.open_file_action.setText(QCoreApplication.translate("MainWindow", u"Open file...", None))
        self.label.setText("")
        self.stopButton.setText("")
        self.playButton.setText("")
        self.pauseButton.setText("")
        self.previousButton.setText("")
        self.nextButton.setText("")
        self.viewButton.setText("")
        self.currentTimeLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">0:00</span></p></body></html>", None))
        self.totalTimeLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">0:00</span></p></body></html>", None))
        self.menuFIle.setTitle(QCoreApplication.translate("MainWindow", u"FIle", None))
    # retranslateUi

