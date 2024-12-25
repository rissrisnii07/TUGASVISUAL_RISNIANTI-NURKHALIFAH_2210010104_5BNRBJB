from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt6.uic import loadUi
import sys


class SliderForm(QMainWindow):
    def __init__(self):
        super().__init__()

        # Path ke file UI
        loadUi("C:/Users/risni/PycharmProjects/db_kantorkesatuan/db_kantorkesatuan_project/ui/tb_slider.ui", self)

        # Inisialisasi tombol
        self.btnSimpan.clicked.connect(self.simpan_data)
        self.btnUbah.clicked.connect(self.ubah_data)
        self.btnHapus.clicked.connect(self.hapus_data)
        self.btnClear.clicked.connect(self.reload_data)
        self.pushButton.clicked.connect(self.cari_data)

        # Inisialisasi tabel
        self.setup_table()

        # Menampilkan form
        self.setWindowTitle("TABEL SLIDER")
        self.show()

    def setup_table(self):
        # Atur kolom tabel
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["ID Slider", "Gambar", "Keterangan"])

        # Tambahkan contoh data
        self.tableWidget.setRowCount(3)
        data = [
            ["1", "gambar1.jpg", "Slider 1"],
            ["2", "gambar2.jpg", "Slider 2"],
            ["3", "gambar3.jpg", "Slider 3"],
        ]
        for row_idx, row_data in enumerate(data):
            for col_idx, value in enumerate(row_data):
                self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(value))

    def simpan_data(self):
        # Ambil data dari tabel atau form input untuk disimpan
        print("Data disimpan")

    def ubah_data(self):
        # Logika untuk mengubah data yang dipilih di tabel
        selected_row = self.tableWidget.currentRow()
        if selected_row != -1:
            print(f"Data di baris {selected_row} diubah")
        else:
            print("Tidak ada baris yang dipilih untuk diubah")

    def hapus_data(self):
        # Logika untuk menghapus data yang dipilih di tabel
        selected_row = self.tableWidget.currentRow()
        if selected_row != -1:
            self.tableWidget.removeRow(selected_row)
            print(f"Baris {selected_row} dihapus")
        else:
            print("Tidak ada baris yang dipilih untuk dihapus")

    def reload_data(self):
        # Logika untuk memuat ulang data (reset ke kondisi awal)
        self.setup_table()
        print("Data di-reload")

    def cari_data(self):
        # Ambil teks dari QLineEdit untuk pencarian
        search_term = self.cari.text().lower()
        if not search_term:
            print("Kolom pencarian kosong")
            return

        # Filter data pada tabel berdasarkan pencarian
        for row in range(self.tableWidget.rowCount()):
            match = any(
                search_term in (self.tableWidget.item(row, col).text().lower() if self.tableWidget.item(row, col) else "")
                for col in range(self.tableWidget.columnCount())
            )
            self.tableWidget.setRowHidden(row, not match)
        print(f"Mencari: {search_term}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SliderForm()
    sys.exit(app.exec())
