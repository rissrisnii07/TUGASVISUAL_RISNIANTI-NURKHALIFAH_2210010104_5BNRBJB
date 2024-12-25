from PyQt6.QtWidgets import QMainWindow, QPushButton
from PyQt6.uic import loadUi
from form2 import formDua
class formSatu(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('form1.ui', self)
        self.button_tampil_form2=self.findChild(QPushButton,"button_tampil_form2")
        self.button_tampil_form2.clicked.connect(self.tampil_form2)

    def tampil_form2(self):
        self.form2 = formDua()
        self.form2.show()
        # self.close()