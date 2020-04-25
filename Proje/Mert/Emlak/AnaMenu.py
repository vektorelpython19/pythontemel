import sys
import os
sys.path.append(os.getcwd()+os.sep+"DB")
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from PyQt5 import uic
from DB1 import DataEmlak

class Uygulama(QMainWindow):
    def __init__(self):
        super().__init__()
        #1.çağırma
        uic.loadUi(r"Proje\Mert\Emlak\ProjeUI_1.ui",self)
        self.Goster()

    def Goster(self):
        self.prgCekim.setValue(0)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Uygulama()
    sys.exit(app.exec_())
