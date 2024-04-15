from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_popWindow(object):
    def setupUi(self, popWindow):
        if popWindow.objectName():
            popWindow.setObjectName(u"popWindow")
        popWindow.resize(418, 162)
        self.centralwidget = QWidget(popWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 371, 130))
        self.frame.setStyleSheet(u"#frame {\n"
"background: #121417;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 371, 31))
        self.frame_2.setStyleSheet(u"#frame_2 {\n"
"background: #07080A;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(19, 6, 100, 20))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: grey;")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 60, 100, 20))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: grey;")
        popWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(popWindow)

        QMetaObject.connectSlotsByName(popWindow)


    def retranslateUi(self, popWindow):
        popWindow.setWindowTitle(QCoreApplication.translate("popWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("popWindow", u"CS2 Server Select", None))
        self.label_2.setText(QCoreApplication.translate("popWindow", u"Fetching Data...", None))


