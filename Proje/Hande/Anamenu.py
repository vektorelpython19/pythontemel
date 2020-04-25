import sys
sys.path.append(r"C:\Users\LENOVO\Documents\GitHub\pythontemel\DB")
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from PyQt5 import uic
from DB1 import DataEmlak

class Uygulama(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"C:\Users\LENOVO\Documents\GitHub\pythontemel\Proje\Hande\ProjeUI_1.ui",self)
        self.Goster()
        
    def Goster(self):
        self.prgCekim.SetValue(0)
        self.show()
        
    def ilDoldur(self):
        liste=self.dbEmlak.ilListele()
        self.cmbil.addItem("-1","Seçiniz")
        for item


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Uygulama()
    sys.exit(app.exec_())