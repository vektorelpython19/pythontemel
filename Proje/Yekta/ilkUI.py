import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


class Uygulama(QMainWindow):
    def __init__(self):
        super().__init__()
        # 1.çağırma
        uic.loadUi(r"/Users/yekta/PycharmProjects/pythontemel/Proje/Yekta/ilkUIHoca.ui",self)
        # self.btGonder
        # 2.çağırma
        # self.win = uic.loadUi(r"/Users/yekta/PycharmProjects/pythontemel/Proje/Yekta/ilkUIHoca.ui")
        # self.win.btGonder
        self.Goster()

    def comboDoldur(self):
        sozluk = {"-1":"Seciniz","1":"Evet","2":"Hayir"}
        for item in sozluk.values():
            self.cmbSecim.addItem(item)

    def Goster(self):
        self.btGonder.clicked.connect(self.aktarim)
        self.comboDoldur()
        self.txtUser.setText("Merhabaaaa")
        self.show()

    def aktarim(self):
        self.lbltxt.setText(self.txtUser.text())
        self.lblcmb.setText(self.cmbSecim.currentText())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Uygulama()
    sys.exit(app.exec_())