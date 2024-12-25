import sys
from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QLineEdit, QTextEdit, QLabel
from PyQt6.QtCore import Qt
from PyQt6.uic import loadUi

class SuratMasukForm(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('C:/Users/risni/PycharmProjects/db_kantorkesatuan/db_kantorkesatuan_project/ui/tb_suratmasuk.ui', self)  # Load the UI from the .ui file

        # Initialize the button actions
        self.btnSimpan.clicked.connect(self.simpan_data)
        self.btnUbah.clicked.connect(self.ubah_data)
        self.btnHapus.clicked.connect(self.hapus_data)
        self.btnCari.clicked.connect(self.cari_data)
        self.btnClear.clicked.connect(self.reload_data)

        # Additional setup if needed
        self.reload_data()

    def simpan_data(self):
        # Code to save data to database or handle saving
        print("Data has been saved.")

    def ubah_data(self):
        # Code to update data in the database or handle updating
        print("Data has been updated.")

    def hapus_data(self):
        # Code to delete data from the database or handle deletion
        print("Data has been deleted.")

    def cari_data(self):
        # Code to search the data based on input
        print("Search executed.")

    def reload_data(self):
        # Code to reload data into the table widget
        self.tableWidget.setRowCount(0)  # Clear the table
        # Example of adding data to the table (replace with actual data loading logic)
        data = [
            ["1", "123", "Klasifikasi A", "Sifat A", "2024-11-01", "2024-11-02", "Perihal A", "Retensi A", "Pengirim A", "Kepada A", "foto1.jpg"],
            ["2", "124", "Klasifikasi B", "Sifat B", "2024-11-02", "2024-11-03", "Perihal B", "Retensi B", "Pengirim B", "Kepada B", "foto2.jpg"]
        ]
        for row_data in data:
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)
            for column, item in enumerate(row_data):
                self.tableWidget.setItem(row_position, column, QTableWidgetItem(item))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SuratMasukForm()
    window.show()
    sys.exit(app.exec())
