import sys
import os
sys.path.append("/Users/yekta/PycharmProjects/pythontemel/DB")
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import uic
from DB1 import DataEmlak

class Uygulama(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"/Users/yekta/PycharmProjects/pythontemel/Proje/Yekta/Emlak/ProjeUI_1.ui",self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Uygulama()
    sys.exit(app.exec_())