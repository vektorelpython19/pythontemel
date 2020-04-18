import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import uic
class Ilk_Uygulama(QMainWindow):
    def __init__(self):
        super().__init__()
        self.win = uic.loadUi(r"Proje\AliUtku\ilkUI.ui")
        self.win.show()
    def Goster(self):
        self.setWindowTitle(self.baslik)
        self.setGeometry(self.sol,self.ust,self.width,self.height)
        dugme = QPushButton("Tıkla",self)
        dugme.move(100,70)
        dugme.clicked.connect(self.Mesaj)
        self.show()
    
    def Mesaj(self):
        cevap = QMessageBox.question(self,"Merhaba","İyi misin?",\
              QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if cevap == QMessageBox.Yes:
            QMessageBox.information(self,"Bilgi","Sevindim :)")
        else:
            QMessageBox.warning(self,"Mesaj","Üzüldüm...")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Ilk_Uygulama()
    sys.exit(app.exec_())        
    