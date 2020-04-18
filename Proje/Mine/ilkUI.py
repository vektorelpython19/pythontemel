import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import uic
class Uygulama(QMainWindow):
    def __init__(self):
        super().__init__()
        #1.çağırma
        uic.loadUi(r"Proje\Mine\ilkUI.ui",self)
        # self.btGonder
        #2.çağırma
        # self.win = uic.loadUi(r"Proje\EDİZ\ilkUI.ui")
        # self.win.btGonder
        self.Goster()
    
    def Goster(self):
        self.show()
    