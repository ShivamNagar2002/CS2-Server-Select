
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
        self.groupBox.setGeometry(QRect(430, 20, 170, 291))
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
        self.hkg = QCheckBox(self.groupBox)
        self.hkg.setObjectName(u"hkg")
        self.hkg.setGeometry(QRect(1, 180, 168, 20))
        self.hkg.setFont(font)
        self.tyo = QCheckBox(self.groupBox)
        self.tyo.setObjectName(u"tyo")
        self.tyo.setGeometry(QRect(1, 210, 168, 20))
        self.tyo.setFont(font)
        self.groupBox_2 = QGroupBox(self.page_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(30, 20, 371, 291))
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
        self.hel = QCheckBox(self.groupBox_2)
        self.hel.setObjectName(u"hel")
        self.hel.setGeometry(QRect(1, 210, 168, 20))
        self.hel.setFont(font)
        self.sto = QCheckBox(self.groupBox_2)
        self.sto.setObjectName(u"sto")
        self.sto.setGeometry(QRect(1, 240, 168, 20))
        self.sto.setFont(font)
        self.vie = QCheckBox(self.groupBox_2)
        self.vie.setObjectName(u"vie")
        self.vie.setGeometry(QRect(190, 30, 168, 20))
        self.vie.setFont(font)
        self.waw = QCheckBox(self.groupBox_2)
        self.waw.setObjectName(u"waw")
        self.waw.setGeometry(QRect(190, 60, 168, 20))
        self.waw.setFont(font)
        self.sto2 = QCheckBox(self.groupBox_2)
        self.sto2.setObjectName(u"sto2")
        self.sto2.setGeometry(QRect(190, 90, 168, 20))
        self.sto2.setFont(font)
        self.next_page = QPushButton(self.page_2)
        self.next_page.setObjectName(u"next_page")
        self.next_page.setGeometry(QRect(650, 320, 41, 31))
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(11)
        self.next_page.setFont(font4)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.groupBox_4 = QGroupBox(self.page_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(40, 20, 170, 151))
        self.groupBox_4.setFont(font)
        self.eze = QCheckBox(self.groupBox_4)
        self.eze.setObjectName(u"eze")
        self.eze.setGeometry(QRect(1, 30, 168, 20))
        self.eze.setFont(font)
        self.gru = QCheckBox(self.groupBox_4)
        self.gru.setObjectName(u"gru")
        self.gru.setGeometry(QRect(1, 60, 168, 20))
        self.gru.setFont(font)
        self.lim = QCheckBox(self.groupBox_4)
        self.lim.setObjectName(u"lim")
        self.lim.setGeometry(QRect(1, 90, 168, 20))
        self.lim.setFont(font)
        self.scl = QCheckBox(self.groupBox_4)
        self.scl.setObjectName(u"scl")
        self.scl.setGeometry(QRect(1, 120, 168, 20))
        self.scl.setFont(font)
        self.groupBox_5 = QGroupBox(self.page_3)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(40, 260, 170, 71))
        self.groupBox_5.setFont(font)
        self.jnb = QCheckBox(self.groupBox_5)
        self.jnb.setObjectName(u"jnb")
        self.jnb.setGeometry(QRect(1, 30, 168, 20))
        self.jnb.setFont(font)
        self.groupBox_6 = QGroupBox(self.page_3)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(450, 20, 170, 291))
        self.groupBox_6.setFont(font)
        self.pwg = QCheckBox(self.groupBox_6)
        self.pwg.setObjectName(u"pwg")
        self.pwg.setGeometry(QRect(1, 30, 168, 20))
        self.pwg.setFont(font)
        self.pwj = QCheckBox(self.groupBox_6)
        self.pwj.setObjectName(u"pwj")
        self.pwj.setGeometry(QRect(1, 60, 168, 20))
        self.pwj.setFont(font)
        self.pwu = QCheckBox(self.groupBox_6)
        self.pwu.setObjectName(u"pwu")
        self.pwu.setGeometry(QRect(1, 90, 168, 20))
        self.pwu.setFont(font)
        self.pww = QCheckBox(self.groupBox_6)
        self.pww.setObjectName(u"pww")
        self.pww.setGeometry(QRect(1, 120, 168, 20))
        self.pww.setFont(font)
        self.pwz = QCheckBox(self.groupBox_6)
        self.pwz.setObjectName(u"pwz")
        self.pwz.setGeometry(QRect(1, 150, 168, 20))
        self.pwz.setFont(font)
        self.shb = QCheckBox(self.groupBox_6)
        self.shb.setObjectName(u"shb")
        self.shb.setGeometry(QRect(1, 180, 168, 20))
        self.shb.setFont(font)
        self.groupBox_7 = QGroupBox(self.page_3)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(40, 180, 170, 71))
        self.groupBox_7.setFont(font)
        self.syd = QCheckBox(self.groupBox_7)
        self.syd.setObjectName(u"syd")
        self.syd.setGeometry(QRect(1, 30, 168, 20))
        self.syd.setFont(font)
        self.groupBox_3 = QGroupBox(self.page_3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(250, 20, 170, 291))
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
        self.ord = QCheckBox(self.groupBox_3)
        self.ord.setObjectName(u"ord")
        self.ord.setGeometry(QRect(1, 150, 168, 20))
        self.ord.setFont(font)
        self.lax = QCheckBox(self.groupBox_3)
        self.lax.setObjectName(u"lax")
        self.lax.setGeometry(QRect(1, 180, 168, 20))
        self.lax.setFont(font)
        self.pushButton_5 = QPushButton(self.page_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(650, 320, 41, 31))
        self.pushButton_5.setFont(font4)
        self.stackedWidget.addWidget(self.page_3)
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
        self.pushButton_4 = QPushButton(self.mainFrame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(100, 430, 130, 23))
        font6 = QFont()
        font6.setFamily(u"Arial")
        font6.setBold(True)
        font6.setUnderline(True)
        font6.setWeight(75)
        self.pushButton_4.setFont(font6)
        self.pushButton_4.setStyleSheet(u"background : transparent;\n"
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
        self.hkg.setText(QCoreApplication.translate("MainWindow", u"hkg (Hong Kong)", None))
        self.tyo.setText(QCoreApplication.translate("MainWindow", u"tyo (Japan)", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"EU", None))
        self.ams.setText(QCoreApplication.translate("MainWindow", u"ams (Netherlands)", None))
        self.atl.setText(QCoreApplication.translate("MainWindow", u"atl (Georgia)", None))
        self.fra.setText(QCoreApplication.translate("MainWindow", u"fra (Germany)", None))
        self.lhr.setText(QCoreApplication.translate("MainWindow", u"lhr (England)", None))
        self.par.setText(QCoreApplication.translate("MainWindow", u"par (France)", None))
        self.mad.setText(QCoreApplication.translate("MainWindow", u"mad (Spain)", None))
        self.hel.setText(QCoreApplication.translate("MainWindow", u"hel (Finland)", None))
        self.sto.setText(QCoreApplication.translate("MainWindow", u"sto  (Sweden)", None))
        self.vie.setText(QCoreApplication.translate("MainWindow", u"vie (Austria)", None))
        self.waw.setText(QCoreApplication.translate("MainWindow", u"waw  (Poland)", None))
        self.sto2.setText(QCoreApplication.translate("MainWindow", u"sto2 (Sweden)", None))
        self.next_page.setText(QCoreApplication.translate("MainWindow", u">>", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"SA", None))
        self.eze.setText(QCoreApplication.translate("MainWindow", u"eze (Argentina)", None))
        self.gru.setText(QCoreApplication.translate("MainWindow", u"gru (Brazil)", None))
        self.lim.setText(QCoreApplication.translate("MainWindow", u"lim (Peru)", None))
        self.scl.setText(QCoreApplication.translate("MainWindow", u"scl (Chile)", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"AF", None))
        self.jnb.setText(QCoreApplication.translate("MainWindow", u"jnb (South Africa)", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"CN", None))
        self.pwg.setText(QCoreApplication.translate("MainWindow", u"pwg  (Guangdong, China)", None))
        self.pwj.setText(QCoreApplication.translate("MainWindow", u"pwj    (Tianjin, China)", None))
        self.pwu.setText(QCoreApplication.translate("MainWindow", u"pwu  (Hebei, China)", None))
        self.pww.setText(QCoreApplication.translate("MainWindow", u"pww  (Wuhan,  China)", None))
        self.pwz.setText(QCoreApplication.translate("MainWindow", u"pwz   (Zhejiang, China)", None))
        self.shb.setText(QCoreApplication.translate("MainWindow", u"shb  (Shanghai, China)", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Australia", None))
        self.syd.setText(QCoreApplication.translate("MainWindow", u"syd  (Sydney, Australia)", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"NA", None))
        self.dfw.setText(QCoreApplication.translate("MainWindow", u"dfw (Texas)", None))
        self.jfk.setText(QCoreApplication.translate("MainWindow", u"jfk (New York)", None))
        self.iad.setText(QCoreApplication.translate("MainWindow", u"iad (Virginia)", None))
        self.sea.setText(QCoreApplication.translate("MainWindow", u"sea (Washington)", None))
        self.ord.setText(QCoreApplication.translate("MainWindow", u"ord Chicago (Illinois)", None))
        self.lax.setText(QCoreApplication.translate("MainWindow", u"lax Los Angeles (California)", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"<<", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"GitHub", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Reset (Unblock All)", None))
