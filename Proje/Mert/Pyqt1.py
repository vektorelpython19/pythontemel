import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QMessageBox
from PyQt5.QtGui import QIcon

class Ilk_Uygulama(QMainWindow):
    def __init__(self):
        super().__init__()
        self.baslik = "İlk Pencere PYQT5"
        self.sol = 100
        self.ust = 100
        self.width = 640
        self.height = 480
        self.Goster()

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
            QMessageBox.warning(self,"Mesaj","Üzüldüm :(")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Ilk_Uygulama()
    sys.exit(app.exec_())