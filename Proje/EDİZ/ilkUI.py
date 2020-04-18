import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QRadioButton
from PyQt5 import uic
class Uygulama(QMainWindow):
    def __init__(self):
        super().__init__()
        #1.çağırma
        uic.loadUi(r"Proje\EDİZ\ilkUI.ui",self)
        # self.btGonder
        #2.çağırma
        # self.win = uic.loadUi(r"Proje\EDİZ\ilkUI.ui")
        # self.win.btGonder
        self.Goster()
    def comboDoldur(self):
        # self.ornek = [(1,"Adana"),(2,"Adıyaman")]
        sozluk = {"-1":"Seçiniz","1":"Evet","2":"Hayır"}
        for item in sozluk.values():
            self.cmbSecim.addItem(item)


    def Goster(self):
        self.btGonder.clicked.connect(self.aktarim)
        self.comboDoldur()
        self.txtUser.setText("Merhabaaaaaa")
        self.show()

    def aktarim(self):
        #----------TextBox-----------------------
        self.lbltxt.setText(self.txtUser.text())
        self.txtUser.setText("Aktarıldı")
        #---------ComboBox-----------------------
        self.lblcmb.setText(self.cmbSecim.currentText())
        self.cmbSecim.setCurrentIndex(2)
        #--------RadioButton---------------------
        if self.rdb1.isChecked() == True:
            self.lblrdb.setText("İşaretledi")
            self.rdb1.setChecked(False)
        else:
            self.lblrdb.setText("İşaretli Değil")
        #--------CheckBox---------------------
        if self.chk1.isChecked() == True:
            self.lblchk.setText("İşaretli")
            self.chk1.setChecked(False)
        else:
            self.lblchk.setText("İşaretli Değil")
        #---------------ProgressBar---------------
        self.prgs1.setMaximum(100)
        self.lblprgs.setText(str(self.prgs1.value()))
        mevcut = self.prgs1.value() + 10
        self.prgs1.setValue(mevcut)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Uygulama()
    sys.exit(app.exec_())

    