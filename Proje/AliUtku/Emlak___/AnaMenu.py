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
        uic.loadUi(r"Proje\AliUtku\Emlak\ProjeUT_1.ui",self)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Uygulama()
    sys.exit(app.exec_())