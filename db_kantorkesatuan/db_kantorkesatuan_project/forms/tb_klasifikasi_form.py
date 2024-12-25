import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem


class KlasifikasiForm(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("C:/Users/risni/PycharmProjects/db_kantorkesatuan/db_kantorkesatuan_project/ui/tb_klasifikasi.ui", self)

        # Menghubungkan tombol dengan fungsinya
        self.btnSimpan.clicked.connect(self.simpan_data)
        self.btnUbah.clicked.connect(self.ubah_data)
        self.btnHapus.clicked.connect(self.hapus_data)
        self.btnClear.clicked.connect(self.reload_data)
        self.pushButton.clicked.connect(self.cari_data)

        # Contoh data untuk diisi ke tabel
        self.data = [
            {"ID Kelas": "1", "Kode Klasifikasi": "A01", "Nama Klasifikasi": "Manajemen", "Uraian": "Pengelolaan umum"},
            {"ID Kelas": "2", "Kode Klasifikasi": "B02", "Nama Klasifikasi": "Keuangan", "Uraian": "Pengelolaan keuangan"},
        ]
        self.load_data_to_table()

    def load_data_to_table(self):
        """Memuat data ke tabel."""
        self.tableWidget.setRowCount(0)  # Bersihkan tabel
        for row_data in self.data:
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)
            for column, key in enumerate(row_data):
                self.tableWidget.setItem(row_position, column, QTableWidgetItem(row_data[key]))

    def simpan_data(self):
        """Menyimpan data baru ke tabel."""
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem("ID Baru"))
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem("Kode Baru"))
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem("Nama Baru"))
        self.tableWidget.setItem(row_position, 3, QTableWidgetItem("Uraian Baru"))
        QMessageBox.information(self, "Informasi", "Data berhasil disimpan!")

    def ubah_data(self):
        """Mengubah data yang dipilih di tabel."""
        selected_items = self.tableWidget.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Peringatan", "Pilih baris yang ingin diubah!")
            return
        for item in selected_items:
            item.setText("Diubah")
        QMessageBox.information(self, "Informasi", "Data berhasil diubah!")

    def hapus_data(self):
        """Menghapus baris yang dipilih di tabel."""
        selected_rows = set(item.row() for item in self.tableWidget.selectedItems())
        if not selected_rows:
            QMessageBox.warning(self, "Peringatan", "Pilih baris yang ingin dihapus!")
            return
        for row in sorted(selected_rows, reverse=True):
            self.tableWidget.removeRow(row)
        QMessageBox.information(self, "Informasi", "Data berhasil dihapus!")

    def reload_data(self):
        """Memuat ulang data ke tabel."""
        self.load_data_to_table()
        QMessageBox.information(self, "Informasi", "Data berhasil dimuat ulang!")

    def cari_data(self):
        """Mencari data berdasarkan input pencarian."""
        keyword = self.cari.text().lower()
        for row in range(self.tableWidget.rowCount()):
            match = False
            for column in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, column)
                if item and keyword in item.text().lower():
                    match = True
                    break
            self.tableWidget.setRowHidden(row, not match)
        QMessageBox.information(self, "Informasi", f"Hasil pencarian untuk '{keyword}' ditampilkan!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = KlasifikasiForm()
    form.show()
    sys.exit(app.exec())
