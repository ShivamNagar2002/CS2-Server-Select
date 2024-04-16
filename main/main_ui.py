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
        MainWindow.resize(885, 544)
        font = QFont()
        font.setFamily(u"Arial")
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainFrame = QFrame(self.centralwidget)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setGeometry(QRect(10, 0, 861, 521))
        self.mainFrame.setFont(font)
        self.mainFrame.setStyleSheet(u"#mainFrame {\n"
"background: #121417;\n"
"color: white;\n"
"border-radius:3px;\n"
"}\n"
"QLabel {\n"
"color: white;\n"
"}")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.titleFrame = QFrame(self.mainFrame)
        self.titleFrame.setObjectName(u"titleFrame")
        self.titleFrame.setGeometry(QRect(0, 0, 860, 40))
        self.titleFrame.setFont(font)
        self.titleFrame.setStyleSheet(u"#titleFrame {\n"
"background: #07080A;\n"
"color: grey ;\n"
"border-radius: 3px;\n"
"} \n"
"\n"
"")
        self.titleFrame.setFrameShape(QFrame.StyledPanel)
        self.titleFrame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.titleFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 150, 20))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: grey;")
        self.pushButton_2 = QPushButton(self.titleFrame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(810, 0, 40, 20))
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"background : #C42121;\n"
"color : white;\n"
"border: 0px;\n"
"padding:0px;\n"
"")
        self.stackedWidget = QStackedWidget(self.mainFrame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(30, 50, 800, 410))
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet(u"QStackedWidget {\n"
"background: #0C0E10;\n"
"}\n"
"\n"
"\n"
"QGroupBox::title  {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 5px 8000px 5px 8000px;\n"
"    background-color:#C42121;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"QCheckBox {\n"
"	color: white;\n"
"	padding: 2px;\n"
"\n"
"	background-color: #111317;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: qradialgradient(\n"
"spread:pad, \n"
"                            cx:0.5,\n"
"                            cy:0.5,\n"
"                            radius:0.9,\n"
"                            fx:0.5,\n"
"                            fy:0.5,\n"
"stop:0.585227\n"
" rgba(196, 33, 33, 255),\n"
" stop:1 rgba(0, 0, 0, 255))\n"
"\n"
"}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.groupBox = QGroupBox(self.page)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 50, 170, 320))
        self.groupBox.setFont(font)
        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(2, 30, 165, 20))
        self.checkBox.setFont(font)
        self.checkBox_2 = QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(2, 60, 165, 20))
        self.checkBox_2.setFont(font)
        self.checkBox_3 = QCheckBox(self.groupBox)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(2, 90, 165, 20))
        self.checkBox_3.setFont(font)
        self.checkBox_4 = QCheckBox(self.groupBox)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setGeometry(QRect(2, 120, 165, 20))
        self.checkBox_4.setFont(font)
        self.checkBox_19 = QCheckBox(self.groupBox)
        self.checkBox_19.setObjectName(u"checkBox_19")
        self.checkBox_19.setGeometry(QRect(2, 150, 165, 20))
        self.checkBox_19.setFont(font)
        self.checkBox_20 = QCheckBox(self.groupBox)
        self.checkBox_20.setObjectName(u"checkBox_20")
        self.checkBox_20.setGeometry(QRect(2, 180, 165, 20))
        self.checkBox_20.setFont(font)
        self.checkBox_21 = QCheckBox(self.groupBox)
        self.checkBox_21.setObjectName(u"checkBox_21")
        self.checkBox_21.setGeometry(QRect(2, 210, 165, 20))
        self.checkBox_21.setFont(font)
        self.groupBox_2 = QGroupBox(self.page)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(450, 220, 170, 151))
        self.groupBox_2.setFont(font)
        self.checkBox_5 = QCheckBox(self.groupBox_2)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setGeometry(QRect(2, 30, 165, 20))
        self.checkBox_5.setFont(font)
        self.checkBox_6 = QCheckBox(self.groupBox_2)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setGeometry(QRect(2, 60, 165, 20))
        self.checkBox_6.setFont(font)
        self.checkBox_7 = QCheckBox(self.groupBox_2)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setGeometry(QRect(2, 90, 165, 20))
        self.checkBox_7.setFont(font)
        self.checkBox_8 = QCheckBox(self.groupBox_2)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setGeometry(QRect(2, 120, 165, 20))
        self.checkBox_8.setFont(font)
        self.groupBox_3 = QGroupBox(self.page)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(240, 50, 170, 320))
        self.groupBox_3.setFont(font)
        self.checkBox_9 = QCheckBox(self.groupBox_3)
        self.checkBox_9.setObjectName(u"checkBox_9")
        self.checkBox_9.setGeometry(QRect(2, 30, 165, 20))
        self.checkBox_9.setFont(font)
        self.checkBox_10 = QCheckBox(self.groupBox_3)
        self.checkBox_10.setObjectName(u"checkBox_10")
        self.checkBox_10.setGeometry(QRect(2, 60, 165, 20))
        self.checkBox_10.setFont(font)
        self.checkBox_11 = QCheckBox(self.groupBox_3)
        self.checkBox_11.setObjectName(u"checkBox_11")
        self.checkBox_11.setGeometry(QRect(2, 90, 165, 20))
        self.checkBox_11.setFont(font)
        self.checkBox_12 = QCheckBox(self.groupBox_3)
        self.checkBox_12.setObjectName(u"checkBox_12")
        self.checkBox_12.setGeometry(QRect(2, 120, 165, 20))
        self.checkBox_12.setFont(font)
        self.checkBox_13 = QCheckBox(self.groupBox_3)
        self.checkBox_13.setObjectName(u"checkBox_13")
        self.checkBox_13.setGeometry(QRect(2, 150, 165, 20))
        self.checkBox_13.setFont(font)
        self.checkBox_14 = QCheckBox(self.groupBox_3)
        self.checkBox_14.setObjectName(u"checkBox_14")
        self.checkBox_14.setGeometry(QRect(2, 180, 165, 20))
        self.checkBox_14.setFont(font)
        self.groupBox_4 = QGroupBox(self.page)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(450, 50, 170, 151))
        self.groupBox_4.setFont(font)
        self.checkBox_15 = QCheckBox(self.groupBox_4)
        self.checkBox_15.setObjectName(u"checkBox_15")
        self.checkBox_15.setGeometry(QRect(2, 30, 165, 20))
        self.checkBox_15.setFont(font)
        self.checkBox_16 = QCheckBox(self.groupBox_4)
        self.checkBox_16.setObjectName(u"checkBox_16")
        self.checkBox_16.setGeometry(QRect(2, 60, 165, 20))
        self.checkBox_16.setFont(font)
        self.checkBox_17 = QCheckBox(self.groupBox_4)
        self.checkBox_17.setObjectName(u"checkBox_17")
        self.checkBox_17.setGeometry(QRect(2, 90, 165, 20))
        self.checkBox_17.setFont(font)
        self.checkBox_18 = QCheckBox(self.groupBox_4)
        self.checkBox_18.setObjectName(u"checkBox_18")
        self.checkBox_18.setGeometry(QRect(2, 120, 165, 20))
        self.checkBox_18.setFont(font)
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 390, 130, 13))
        self.label_2.setFont(font)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(360, 190, 80, 30))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"color: grey;")
        self.stackedWidget.addWidget(self.page_2)
        self.pushButton = QPushButton(self.mainFrame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(710, 480, 110, 30))
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"background : #C42121;\n"
"color : white;\n"
"border: 0px;\n"
"border-radius : 3px;")
        self.pushButton_3 = QPushButton(self.mainFrame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(570, 490, 140, 20))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setBold(True)
        font3.setUnderline(True)
        font3.setWeight(75)
        self.pushButton_3.setFont(font3)
        self.pushButton_3.setStyleSheet(u"\n"
"background : #121417;\n"
"color : #C42121;\n"
"border: 0px;\n"
"border-radius : 3px;")
        self.pushButton_4 = QPushButton(self.mainFrame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(30, 480, 140, 20))
        self.pushButton_4.setFont(font3)
        self.pushButton_4.setStyleSheet(u"\n"
"background : #121417;\n"
"color : #C42121;\n"
"border: 0px;\n"
"border-radius : 3px;")
        self.label_3 = QLabel(self.mainFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(4, 506, 180, 13))
        self.label_3.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"[CS2] Server Select", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Asia", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"bom1 (Mumbai)", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"bom2 (Mumbai)", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"maa1 (Chennai)", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"maa2 (Chennai)", None))
        self.checkBox_19.setText(QCoreApplication.translate("MainWindow", u"dxb (United Arab Emirates)", None))
        self.checkBox_20.setText(QCoreApplication.translate("MainWindow", u"sgp (Singapore)", None))
        self.checkBox_21.setText(QCoreApplication.translate("MainWindow", u"seo (South Korea)", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"China", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"canm ", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"ctum ", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"sham ", None))
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"tsnm ", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"EU", None))
        self.checkBox_9.setText(QCoreApplication.translate("MainWindow", u"ams (Netherlands)", None))
        self.checkBox_10.setText(QCoreApplication.translate("MainWindow", u"atl (Georgia)", None))
        self.checkBox_11.setText(QCoreApplication.translate("MainWindow", u"fra (Germany)", None))
        self.checkBox_12.setText(QCoreApplication.translate("MainWindow", u"lhr (England)", None))
        self.checkBox_13.setText(QCoreApplication.translate("MainWindow", u"par (France)", None))
        self.checkBox_14.setText(QCoreApplication.translate("MainWindow", u"mad (Spain)", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"US", None))
        self.checkBox_15.setText(QCoreApplication.translate("MainWindow", u"dfw (Texas)", None))
        self.checkBox_16.setText(QCoreApplication.translate("MainWindow", u"jfk (New York)", None))
        self.checkBox_17.setText(QCoreApplication.translate("MainWindow", u"iad (Virginia)", None))
        self.checkBox_18.setText(QCoreApplication.translate("MainWindow", u"sea (Washington)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Select Servers to Block.", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Loading", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Reset All (Unblock All)", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"GitHub", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"https://github.com/ShivamNagar2002", None))


