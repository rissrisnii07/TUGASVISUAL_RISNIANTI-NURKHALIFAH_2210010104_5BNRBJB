import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)

window = QMainWindow()

window.statusBar().showMessage("Belajar Visual 3")

window.menuBar().addMenu("File")
window.menuBar().addMenu("Transaksi")
window.menuBar().addMenu("Laporan")

window.show()

sys.exit(app.exec())