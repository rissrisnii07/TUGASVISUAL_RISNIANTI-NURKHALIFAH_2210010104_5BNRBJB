from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from PyQt6.QtCore import Qt

# Load the UI file
class DokumentasiForm(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the UI from the .ui file
        uic.loadUi('C:/Users/risni/PycharmProjects/db_kantorkesatuan/db_kantorkesatuan_project/ui/tb_dokumentasi.ui', self)

        # Connect buttons to their corresponding methods
        self.btnSimpan.clicked.connect(self.simpan_data)
        self.btnUbah.clicked.connect(self.ubah_data)
        self.btnHapus.clicked.connect(self.hapus_data)
        self.btnClear.clicked.connect(self.reload_data)
        self.btnCari.clicked.connect(self.cari_data)

        # Initial setup for table widget
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(['ID Dok', 'Tanggal Dok', 'Judul', 'Foto', 'Isi', 'Link'])
        self.tableWidget.setRowCount(0)

        # Pre-fill some fields for demonstration
        self.fill_sample_data()

    def fill_sample_data(self):
        # Add some sample data into the table for demonstration
        data = [
            ['1', '2024-12-01', 'Dokumentasi 1', 'foto1.jpg', 'Isi dokumentasi 1', 'http://link1.com'],
            ['2', '2024-12-02', 'Dokumentasi 2', 'foto2.jpg', 'Isi dokumentasi 2', 'http://link2.com'],
            ['3', '2024-12-03', 'Dokumentasi 3', 'foto3.jpg', 'Isi dokumentasi 3', 'http://link3.com'],
        ]

        for row_data in data:
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)
            for column, value in enumerate(row_data):
                self.tableWidget.setItem(row_position, column, QTableWidgetItem(value))

        # Set some initial values for the input fields
        self.judulInput.setText("Judul Contoh")
        self.tglInput.setText("2024-12-01")
        self.fotoInput.setPlainText("foto_contoh.jpg")
        self.isiInput.setPlainText("Ini adalah isi dokumentasi contoh.")
        self.linkInput.setText("http://contohlink.com")

    def simpan_data(self):
        judul = self.judulInput.text()
        tgl = self.tglInput.text()
        foto = self.fotoInput.toPlainText()
        isi = self.isiInput.toPlainText()
        link = self.linkInput.text()

        if not judul or not tgl or not foto or not isi or not link:
            QMessageBox.warning(self, "Warning", "All fields must be filled!")
            return

        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)

        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str(row_position + 1)))  # ID Dok
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(tgl))  # Tanggal Dok
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(judul))  # Judul
        self.tableWidget.setItem(row_position, 3, QTableWidgetItem(foto))  # Foto
        self.tableWidget.setItem(row_position, 4, QTableWidgetItem(isi))  # Isi
        self.tableWidget.setItem(row_position, 5, QTableWidgetItem(link))  # Link

        self.clear_fields()

    def ubah_data(self):
        row = self.tableWidget.currentRow()
        if row == -1:
            QMessageBox.warning(self, "Warning", "Please select a row to edit!")
            return

        judul = self.judulInput.text()
        tgl = self.tglInput.text()
        foto = self.fotoInput.toPlainText()
        isi = self.isiInput.toPlainText()
        link = self.linkInput.text()

        if not judul or not tgl or not foto or not isi or not link:
            QMessageBox.warning(self, "Warning", "All fields must be filled!")
            return

        self.tableWidget.setItem(row, 1, QTableWidgetItem(tgl))  # Tanggal Dok
        self.tableWidget.setItem(row, 2, QTableWidgetItem(judul))  # Judul
        self.tableWidget.setItem(row, 3, QTableWidgetItem(foto))  # Foto
        self.tableWidget.setItem(row, 4, QTableWidgetItem(isi))  # Isi
        self.tableWidget.setItem(row, 5, QTableWidgetItem(link))  # Link

        self.clear_fields()

    def hapus_data(self):
        row = self.tableWidget.currentRow()
        if row == -1:
            QMessageBox.warning(self, "Warning", "Please select a row to delete!")
            return
        self.tableWidget.removeRow(row)

    def reload_data(self):
        self.tableWidget.setRowCount(0)

    def cari_data(self):
        search_term = self.tglInput_2.text().lower()
        for row in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(row, 1)
            if item and search_term in item.text().lower():
                self.tableWidget.selectRow(row)
                break
        else:
            QMessageBox.information(self, "Info", "No matching data found.")

    def clear_fields(self):
        self.judulInput.clear()
        self.tglInput.clear()
        self.fotoInput.clear()
        self.isiInput.clear()
        self.linkInput.clear()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = DokumentasiForm()
    window.show()
    sys.exit(app.exec())
