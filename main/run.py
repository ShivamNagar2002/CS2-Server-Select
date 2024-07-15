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
import threading





toblk = []

currBlocked = [] 
alldata = []
counter = 0



class MainWindow(QMainWindow):
    global toblk 
    toblk = []
    global sv_list 
    sv_list = [ "maa2", "bom2", "dxb", "sgp", "seo", "ams", "atl", "fra", "lhr", "par", "mad", "dfw", "jfk", "iad", "sea", "canm", "ctum", "sham", "tsnm" ]
    global currBlocked 
    currBlocked = [] 
    global alldata

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_NoSystemBackground)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.setupUi(self)
        ## calling on load 
        t1 = threading.Thread(target=self.onload)
        t1.start()
        self.ui.pushButton_3.clicked.connect(lambda: os.system("start https://github.com/ShivamNagar2002") )
       
        
        self.ui.pushButton.clicked.connect(self.newFncStart)
        self.ui.pushButton_4.clicked.connect(self.unblock)
        self.ui.pushButton_2.clicked.connect(self.f_exit)
        
       

            
        self.show()
       


    def f_exit(self):
            sys.exit()
            quit()
            os._exit()
            exit()





## Function to unblock all Servers 

    def unblock(self):
        global toblk, sv_list , alldata
        for tmpx in sv_list :
            try :
                tmpvar = "CS2ServerSelect_BLOCK_"+tmpx
                cmd = "netsh advfirewall firewall delete rule  name={0} >NUL 2>&1 ".format(tmpvar)
                os.system(cmd)
            except:
                pass
        
        checkboxes = self.ui.mainFrame.findChildren(QCheckBox)
        ## Changing staes of all checkboxes 
        for checkbox in checkboxes:
            checkbox.setCheckState(Qt.Unchecked)


     
        
        
        

     

### New Function to block Selected servers ( Removed old if checks )
    def newBlockFnc(self):
        global toblk, alldata
        for key in toblk.keys():
            firewall_rule_name = "CS2ServerSelect_BLOCK_"+ key
            if toblk[key] == True:
                x = 0 
                x2 = ""
                while x < len(alldata[key]):
                    if x == 0 :
                        x2 = x2 + alldata[key][x]
                    if x > 0:
                        x2 = x2 + ',' + alldata[key][x]
                    x = x + 1
                cmd = "netsh advfirewall firewall show rule name={0} >NUL 2>&1".format(firewall_rule_name)
                
                if os.system(cmd) == 1:
                    try:
                        cmd = "netsh advfirewall firewall add rule  name={0}  dir=out action=block protocol=ANY  remoteip= \"{1}\"  >NUL 2>&1".format(firewall_rule_name, x2)
                        os.system(cmd)
                        
                    except:
                        pass 

            elif toblk[key] == False :
                    try:
                        cmd = "netsh advfirewall firewall delete rule  name={0} >NUL 2>&1 ".format(firewall_rule_name)
                        os.system(cmd)
                    except:
                        pass             
        toblk = {}




### Functionn to fetch states of all checkboxed and load them into a toblk (to block ) dictionary : True/False
    def newFncStart(self):
        global sv_list 
        global toblk
        toblk = {}
        checkboxes = self.ui.mainFrame.findChildren(QCheckBox)

        for checkbox in checkboxes:
            toblk[checkbox.objectName()] = checkbox.isChecked()
        self.newBlockFnc()
    


   






### Pre-Checks all already blocked servers  and reapply settings
    def fetchCurrBlocked(self):
        global sv_list
        global currBlocked
        global toblk
        toblk = {}
        for x in sv_list:
            cmd = "netsh advfirewall firewall show rule name=CS2ServerSelect_BLOCK_{0} >NUL 2>&1".format(x)
            if os.system(cmd) == 1:
                toblk[x] = False
                try:
                    currBlocked.pop(x)
                except:
                    pass
            elif os.system(cmd) == 0:
                toblk[x] = True
                currBlocked.append(x) 
        currBlocked = set(currBlocked)  
        
        self.unblock()
     
        tmp_thread = threading.Thread(target=self.newBlockFnc)
        tmp_thread.start()      
        return currBlocked

    def onload(self):
        global currBlocked 
        global alldata
        global sv_list

    
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
                    x = x +1
                alldata[x1] = ips        
            except:
                pass
        
        self.fetchCurrBlocked()
        time.sleep(0.25)
 
        checkboxes = self.ui.mainFrame.findChildren(QCheckBox)
        self.ui.progressBar.setValue(50)
        
        for checkbox in checkboxes:
            time.sleep(0.005)
            if checkbox.objectName() in currBlocked:
                checkbox.setCheckState(Qt.Checked)
                
                

        self.ui.progressBar.setValue(100)
        time.sleep(0.9)
        self.ui.progressBar.hide()
        self.ui.stackedWidget.setCurrentIndex(1)
        
        


        


     

    

       
               

    

        






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
        if __name__ == "__main__":
            app = QApplication(sys.argv)
            window = MainWindow()
            sys.exit(app.exec_())
