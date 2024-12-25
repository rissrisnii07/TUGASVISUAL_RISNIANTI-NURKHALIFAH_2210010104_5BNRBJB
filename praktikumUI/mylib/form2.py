from PyQt6.QtWidgets import QMainWindow
from PyQt6.uic import loadUi

class formDua(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('form2.ui', self)
        self.hitungButton.clicked.connect(self.luas)

    def luas(self):
        panjang = self.editPanjang.text()
        lebar = self.editLebar.text()
        print(int(lebar) +int(panjang))