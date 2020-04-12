import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton
from PyQt5.QtGui import QIcon

class ilkUygulama(QMainWindow):
        def __init__(self):
                super().__init__()
                self.baslik = "Ilk pencere"
                self.sol = 100
                self.ust = 100
                self.width = 640
                self.height = 480
                self.goster()

        def goster(self):
            self.setWindowTitle(self.baslik)
            self.setGeometry(self.sol,self.ust,self.width,self.height)
            dugme = QPushButton("Tikla",self)
            dugme.move(100,70)
            self.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = ilkUygulama()
    sys.exit(app.exec_())

