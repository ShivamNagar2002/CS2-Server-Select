from main_ui import *
import sys
import time 
from main_ui import Ui_MainWindow
import sys
from PySide2 import QtCore
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from urllib.request import urlopen
import json
import os 
import sys
import pyuac









class MainWindow(QMainWindow):
    global toblk 
    toblk = []
    global sv_list 
    sv_list = ["maa", "maa2", "bom", "bom2", "dxb", "sgp", "seo", "ams", "atl", "fra", "lhr", "par", "mad", "dfw", "jfk", "iad", "sea", "canm", "ctum", "sham", "tsnm" ]
    global config 
    config = {}
    config.fromkeys(sv_list)
    global alldata

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_NoSystemBackground)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.setupUi(self)
        self.onload()
        self.ui.pushButton_4.clicked.connect(lambda: os.system("start https://github.com/ShivamNagar2002") )
       
        
        self.ui.pushButton.clicked.connect(self.startbtn)
        self.ui.pushButton_3.clicked.connect(self.unblock)
        self.ui.pushButton_2.clicked.connect(self.f_exit)
        self.show()
       


    def f_exit(self):
        try:
            sys.exit()
        except:
            quit()
        
        try:
            os._exit()
        except:
            exit()

    def unblock(self):
        global toblk, sv_list , alldata
        for tmpx in sv_list :
            try :
                tmpvar = "CS2ServerSelect_BLOCK_"+tmpx
                cmd = "netsh advfirewall firewall delete rule  name={0}  ".format(tmpvar)
                os.system(cmd)
            except:
                pass
        
        self.ui.checkBox.setCheckState(Qt.Unchecked)
        self.ui.checkBox_2.setCheckState(Qt.Unchecked)
        self.ui.checkBox_3.setCheckState(Qt.Unchecked)
        self.ui.checkBox_4.setCheckState(Qt.Unchecked)
        self.ui.checkBox_5.setCheckState(Qt.Unchecked)
        self.ui.checkBox_6.setCheckState(Qt.Unchecked)
        self.ui.checkBox_7.setCheckState(Qt.Unchecked)
        self.ui.checkBox_8.setCheckState(Qt.Unchecked)
        self.ui.checkBox_9.setCheckState(Qt.Unchecked)
        self.ui.checkBox_10.setCheckState(Qt.Unchecked)
        self.ui.checkBox_11.setCheckState(Qt.Unchecked)
        self.ui.checkBox_12.setCheckState(Qt.Unchecked)
        self.ui.checkBox_13.setCheckState(Qt.Unchecked)
        self.ui.checkBox_14.setCheckState(Qt.Unchecked)
        self.ui.checkBox_15.setCheckState(Qt.Unchecked)
        self.ui.checkBox_16.setCheckState(Qt.Unchecked)
        self.ui.checkBox_17.setCheckState(Qt.Unchecked)
        self.ui.checkBox_18.setCheckState(Qt.Unchecked)
        self.ui.checkBox_19.setCheckState(Qt.Unchecked)
        self.ui.checkBox_20.setCheckState(Qt.Unchecked)
        self.ui.checkBox_21.setCheckState(Qt.Unchecked)
  
        
        
        




    def block(self):
        global toblk, sv_list , alldata
        for tmpx in toblk :
            x = 0
            x2 = ""
            while x < len(alldata[tmpx]):
                
                tmpvar = "CS2ServerSelect_BLOCK_"+tmpx
                
                if x == 0:
                    x2 = x2 + alldata[tmpx][x]
                if x > 0:
                    x2 = x2 + "," + alldata[tmpx][x]
                x= x+1
            print(x2)
            cmd = "netsh advfirewall firewall add rule  name={0}  dir=out action=block protocol=ANY  remoteip= \"{1}\"".format(tmpvar, x2)
            os.system(cmd)
                












    def startbtn(self):
        global toblk
        toblock  = []
        if int(self.ui.checkBox.checkState()) == 2:
            toblock.append("bom")
        if int(self.ui.checkBox_2.checkState()) == 2:
            toblock.append("bom2")
        if int(self.ui.checkBox_3.checkState()) == 2:
            toblock.append("maa")
        if int(self.ui.checkBox_4.checkState()) == 2:
            toblock.append("maa2")
        if int(self.ui.checkBox_5.checkState()) == 2:
            toblock.append("canm")
        if int(self.ui.checkBox_6.checkState()) == 2:
            toblock.append("ctum")
        if int(self.ui.checkBox_7.checkState()) == 2:
            toblock.append("sham")
        if int(self.ui.checkBox_8.checkState()) == 2:
            toblock.append("tsnm")
        if int(self.ui.checkBox_9.checkState()) == 2:
            toblock.append("ams")
        if int(self.ui.checkBox_10.checkState()) == 2:
            toblock.append("atl")
        if int(self.ui.checkBox_11.checkState()) == 2:
            toblock.append("fra")
        if int(self.ui.checkBox_12.checkState()) == 2:
            toblock.append("lhr")
        if int(self.ui.checkBox_13.checkState()) == 2:
            toblock.append("par")
        if int(self.ui.checkBox_14.checkState()) == 2:
            toblock.append("mad")
        if int(self.ui.checkBox_15.checkState()) == 2:
            toblock.append("dfw")
        if int(self.ui.checkBox_16.checkState()) == 2:
            toblock.append("jfk")
        if int(self.ui.checkBox_17.checkState()) == 2:
            toblock.append("iad")
        if int(self.ui.checkBox_18.checkState()) == 2:
            toblock.append("sea")
        if int(self.ui.checkBox_19.checkState()) == 2:
            toblock.append("dxb")
        if int(self.ui.checkBox_20.checkState()) == 2:
            toblock.append("sgp")
        if int(self.ui.checkBox_21.checkState()) == 2:
            toblock.append("seo")
        
        toblk = set(toblock)
        self.block()
        print(toblk)




    def onload(self):
        global config 
        global alldata
        global sv_list
        ## trying to fetch data from api

        url  = "https://api.steampowered.com/ISteamApps/GetSDRConfig/v1/?appid=730"


        with urlopen(url) as response:
            html_response = response.read()
            encoding = response.headers.get_content_charset('json')
            dedata = html_response.decode(encoding)
          

        i_string = json.dumps(dedata)  

       
        res_dictionary = json.loads(dedata)  
        


        t2 = res_dictionary["pops"]
        
        ips =[ ]
        alldata = {}
        alldata.fromkeys(t2)

        for x1 in sv_list: 
            x = 0
            ips = []
            try:
                while x < len(t2[x1]["relays"]):
                    ips.append(t2[x1]["relays"][x]["ipv4"])
                    alldata[x1] = ips
                    
                    x = x +1
            except:
                pass
     

    

       
               

    

        






## Movement Fucnitons 
    def center(self):
        qr = self.frameGeometry()

        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        time.sleep(0.024)
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        
        delta = QPoint (event.globalPos() - self.oldPos)
        
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
        
        


if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        print("Re-launching as admin!")
        pyuac.runAsAdmin()
    else:        
        app = QApplication(sys.argv)
        window = MainWindow()
        sys.exit(app.exec_())