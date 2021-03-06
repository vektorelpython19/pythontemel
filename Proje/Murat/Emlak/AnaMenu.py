import sys
import os
sys.path.append(os.getcwd()+os.sep+"DB")
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from PyQt5 import uic
from DB.DB1 import DataEmlak

class Uygulama(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"Proje\EDİZ\Emlak\ProjeUI_1.ui",self)
        self.dbEmlak = DataEmlak()
        self.Goster()

    def Goster(self):
        self.ilDoldur()
        self.prgCekim.setValue(0)
        self.show()

    def ilDoldur(self):
        liste = self.dbEmlak.ilListele()
        self.cmbil.addItem("Seçiniz","-1")
        for item in liste:
            self.cmbil.addItem(item[1],item[0])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Uygulama()
    sys.exit(app.exec_())
