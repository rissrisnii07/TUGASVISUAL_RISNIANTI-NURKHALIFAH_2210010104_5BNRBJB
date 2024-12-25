import sys
from PyQt6.QtWidgets import QApplication
from form1 import formSatu
`
if __name__== "__main__":
    aplikasi = QApplication(sys.argv)
    tampilForm = formSatu()
    tampilForm.show()
    sys.exit(aplikasi.exec())