# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainZhYCqc.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainFrame = QFrame(self.centralwidget)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setGeometry(QRect(30, 30, 730, 471))
        font = QFont()
        font.setFamily(u"Arial")
        self.mainFrame.setFont(font)
        self.mainFrame.setStyleSheet(u"#mainFrame {\n"
"background: #121417;\n"
"color: white;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
".QLabel {\n"
"color: white;\n"
"}\n"
"\n"
"\n"
".QProgressBar {\n"
"        border: 2px solid rgba(33, 37, 43, 180);\n"
"        border-radius: 5px;\n"
"        text-align: center;\n"
"        background-color: rgba(33, 37, 43, 180);\n"
"        color: black;\n"
"    }\n"
"    .QProgressBar::chunk {\n"
"        background-color: #C42121;\n"
"		border:0px;\n"
"		border-radius: 3px;\n"
"    }\n"
"\n"
".QPushButton {\n"
"background : #C42121;\n"
"color : white;\n"
"border: 0px;\n"
"border-radius : 3px;\n"
"}")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.titleFrame = QFrame(self.mainFrame)
        self.titleFrame.setObjectName(u"titleFrame")
        self.titleFrame.setGeometry(QRect(-1, 0, 731, 35))
        self.titleFrame.setFont(font)
        self.titleFrame.setStyleSheet(u"#titleFrame {\n"
"background: #07080A;\n"
"color: grey;\n"
"border-radius: 3px;\n"
"}")
        self.titleFrame.setFrameShape(QFrame.StyledPanel)
        self.titleFrame.setFrameShadow(QFrame.Raised)
        self.titleLabel = QLabel(self.titleFrame)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(20, 10, 131, 16))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setWeight(75)
        self.titleLabel.setFont(font1)
        self.titleLabel.setStyleSheet(u"color: grey;")
        self.pushButton_2 = QPushButton(self.titleFrame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(690, 0, 30, 20))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(6)
        font2.setBold(True)
        font2.setWeight(75)
        self.pushButton_2.setFont(font2)
        self.stackedWidget = QStackedWidget(self.mainFrame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(15, 50, 701, 361))
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet(u".QStackedWidget {\n"
"background: #0C0E10;\n"
"border:0 px;\n"
"border-radius: 2px;\n"
"}\n"
"\n"
".QGroupBox::title  {\n"
" subcontrol-origin: margin;\n"
"subcontrol-position: top center;\n"
" padding: 5px 8000px 5px 8000px;\n"
" background-color:#C42121;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
".QCheckBox {\n"
"color: white;\n"
"padding: 2px;\n"
"background-color: #111317;\n"
"}\n"
"\n"
".QCheckBox::indicator:checked {\n"
"background-color: qradialgradient(\n"
"spread:pad, \n"
"                            cx:0.5,\n"
"                            cy:0.5,\n"
"                            radius:0.9,\n"
"                            fx:0.5,\n"
"                            fy:0.5,\n"
"stop:0.585227\n"
"rgba(196, 33, 33, 255),\n"
"stop:1 rgba(0, 0, 0, 255))\n"
"}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 105, 160, 121))
        font3 = QFont()
        font3.setPointSize(22)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"color: grey;")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.groupBox = QGroupBox(self.page_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 30, 170, 291))
        self.groupBox.setFont(font)
        self.bom2 = QCheckBox(self.groupBox)
        self.bom2.setObjectName(u"bom2")
        self.bom2.setGeometry(QRect(1, 30, 168, 20))
        self.bom2.setFont(font)
        self.maa2 = QCheckBox(self.groupBox)
        self.maa2.setObjectName(u"maa2")
        self.maa2.setGeometry(QRect(1, 60, 168, 20))
        self.maa2.setFont(font)
        self.dbx = QCheckBox(self.groupBox)
        self.dbx.setObjectName(u"dbx")
        self.dbx.setGeometry(QRect(1, 90, 168, 20))
        self.dbx.setFont(font)
        self.sgp = QCheckBox(self.groupBox)
        self.sgp.setObjectName(u"sgp")
        self.sgp.setGeometry(QRect(1, 120, 168, 20))
        self.sgp.setFont(font)
        self.seo = QCheckBox(self.groupBox)
        self.seo.setObjectName(u"seo")
        self.seo.setGeometry(QRect(1, 150, 168, 20))
        self.seo.setFont(font)
        self.groupBox_2 = QGroupBox(self.page_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(220, 30, 170, 291))
        self.groupBox_2.setFont(font)
        self.ams = QCheckBox(self.groupBox_2)
        self.ams.setObjectName(u"ams")
        self.ams.setGeometry(QRect(1, 30, 168, 20))
        self.ams.setFont(font)
        self.atl = QCheckBox(self.groupBox_2)
        self.atl.setObjectName(u"atl")
        self.atl.setGeometry(QRect(1, 60, 168, 20))
        self.atl.setFont(font)
        self.fra = QCheckBox(self.groupBox_2)
        self.fra.setObjectName(u"fra")
        self.fra.setGeometry(QRect(1, 90, 168, 20))
        self.fra.setFont(font)
        self.lhr = QCheckBox(self.groupBox_2)
        self.lhr.setObjectName(u"lhr")
        self.lhr.setGeometry(QRect(1, 120, 168, 20))
        self.lhr.setFont(font)
        self.par = QCheckBox(self.groupBox_2)
        self.par.setObjectName(u"par")
        self.par.setGeometry(QRect(1, 150, 168, 20))
        self.par.setFont(font)
        self.mad = QCheckBox(self.groupBox_2)
        self.mad.setObjectName(u"mad")
        self.mad.setGeometry(QRect(1, 180, 168, 20))
        self.mad.setFont(font)
        self.groupBox_3 = QGroupBox(self.page_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(420, 30, 170, 291))
        self.groupBox_3.setFont(font)
        self.dfw = QCheckBox(self.groupBox_3)
        self.dfw.setObjectName(u"dfw")
        self.dfw.setGeometry(QRect(1, 30, 168, 20))
        self.dfw.setFont(font)
        self.jfk = QCheckBox(self.groupBox_3)
        self.jfk.setObjectName(u"jfk")
        self.jfk.setGeometry(QRect(1, 60, 168, 20))
        self.jfk.setFont(font)
        self.iad = QCheckBox(self.groupBox_3)
        self.iad.setObjectName(u"iad")
        self.iad.setGeometry(QRect(1, 90, 168, 20))
        self.iad.setFont(font)
        self.sea = QCheckBox(self.groupBox_3)
        self.sea.setObjectName(u"sea")
        self.sea.setGeometry(QRect(1, 120, 168, 20))
        self.sea.setFont(font)
        self.pushButton_4 = QPushButton(self.page_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(574, 330, 130, 23))
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setBold(True)
        font4.setUnderline(True)
        font4.setWeight(75)
        self.pushButton_4.setFont(font4)
        self.pushButton_4.setStyleSheet(u"background : transparent;\n"
"color: #C42121;")
        self.stackedWidget.addWidget(self.page_2)
        self.progressBar = QProgressBar(self.mainFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(476, 428, 118, 23))
        self.progressBar.setFont(font)
        self.progressBar.setValue(10)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.pushButton = QPushButton(self.mainFrame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(600, 420, 101, 31))
        self.pushButton.setFont(font)
        self.pushButton_3 = QPushButton(self.mainFrame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(30, 430, 75, 23))
        font5 = QFont()
        font5.setFamily(u"Arial")
        font5.setBold(True)
        font5.setItalic(False)
        font5.setUnderline(True)
        font5.setWeight(75)
        self.pushButton_3.setFont(font5)
        self.pushButton_3.setStyleSheet(u"background: transparent;\n"
"color: #C42121;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"[CS2] Server Select", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Please Wait", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Asia", None))
        self.bom2.setText(QCoreApplication.translate("MainWindow", u"bom2 (Mumbai)", None))
        self.maa2.setText(QCoreApplication.translate("MainWindow", u"maa2 (Chennai)", None))
        self.dbx.setText(QCoreApplication.translate("MainWindow", u"dxb (United Arab Emirates)", None))
        self.sgp.setText(QCoreApplication.translate("MainWindow", u"sgp (Singapore)", None))
        self.seo.setText(QCoreApplication.translate("MainWindow", u"seo (South Korea)", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"EU", None))
        self.ams.setText(QCoreApplication.translate("MainWindow", u"ams (Netherlands)", None))
        self.atl.setText(QCoreApplication.translate("MainWindow", u"atl (Georgia)", None))
        self.fra.setText(QCoreApplication.translate("MainWindow", u"fra (Germany)", None))
        self.lhr.setText(QCoreApplication.translate("MainWindow", u"lhr (England)", None))
        self.par.setText(QCoreApplication.translate("MainWindow", u"par (France)", None))
        self.mad.setText(QCoreApplication.translate("MainWindow", u"mad (Spain)", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"US", None))
        self.dfw.setText(QCoreApplication.translate("MainWindow", u"dfw (Texas)", None))
        self.jfk.setText(QCoreApplication.translate("MainWindow", u"jfk (New York)", None))
        self.iad.setText(QCoreApplication.translate("MainWindow", u"iad (Virginia)", None))
        self.sea.setText(QCoreApplication.translate("MainWindow", u"sea (Washington)", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Reset (Unblock All)", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"GitHub", None))
    # retranslateUi

