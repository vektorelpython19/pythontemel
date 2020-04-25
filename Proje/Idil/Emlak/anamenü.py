import sys
sys.path.append("DB")
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from PyQt5 import uic
from DB1 import DataEmlak

class Uygulama(QMainWindow):
    def __init__(self):
        super().__init__()
        #1.çağırma
        uic.loadUi(r"Proje\Idil\Emlak\ProjeUI_1.ui",self)
        self.db.Emlak =DataEmlak
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
