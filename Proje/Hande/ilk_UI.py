import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import uic
class Uygulama(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"Proje\Hande\Hande.ui")
        self.Goster()
        
    def Goster(self):
        self.show()