from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
import sys
# membuat class Jendela yang mewarisi Class QWidget
class Jendela(QWidget):
   #membuat method sebagai constructor
   # self merupakan variabel buatan kita dan bisa diganti lain
    def __init__(self):
        super().__init__() #super berfungsi untuk mewarisi sifat lebih jauh lagi
        #setGeometry(posisi X, Posisi Y, Lebar, Tinggi)
        self.setGeometry(300,200, 600, 400)
        self.setWindowTitle("Belajar Membuat Form dengan Class OOP")

        #cara lain untuk mengatur panjang dan lebar
        #self.setFixedWidth(500)
        #self.setFixedHeight(400)

app = QApplication(sys.argv)
window = Jendela()
window.show()
sys.exit(app.exec())
