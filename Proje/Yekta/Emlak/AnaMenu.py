import sys
sys.path.append("/Users/yekta/PycharmProjects/pythontemel/Proje/Yekta/Emlak/DB")
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import uic
from DB.DB1 import DataEmlak

class Uygulama(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"/Users/yekta/PycharmProjects/pythontemel/Proje/Yekta/Emlak/ProjeUI_1.ui",self)
        self.dbEmlak = DataEmlak()
        self.Goster()

    def Goster(self):
        self.ilDoldur()
        self.prgCekim.setValue(0)
        self.show()

    def ilDoldur(self):
        liste = self.dbEmlak.ilListele()
        self.cmbil.addItem("-1","Seçiniz")
        for item in liste:
            self.cmbil.addItem(str(item[0]),item[1])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Uygulama()
    sys.exit(app.exec_())