import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem

class SuratKeluarForm(QMainWindow):
    def __init__(self):
        super().__init__()
        # Memuat file .ui
        uic.loadUi("C:/Users/risni/PycharmProjects/db_kantorkesatuan/db_kantorkesatuan_project/ui/tb_suratkeluar.ui", self)

        # Menghubungkan tombol ke fungsinya
        self.btnSimpan.clicked.connect(self.simpan_data)
        self.btnHapus.clicked.connect(self.hapus_data)
        self.btnUbah.clicked.connect(self.ubah_data)
        self.btnClear.clicked.connect(self.reload_data)

        # Contoh data untuk ditampilkan di tabel
        self.data = [
            ["1", "001", "Umum", "Rahasia", "2024-01-01", "2024-01-02", "Surat Undangan", "1 Tahun", "Bapak A", "Foto1.jpg"],
            ["2", "002", "Kepegawaian", "Biasa", "2024-02-01", "2024-02-02", "Surat Peringatan", "2 Tahun", "Ibu B", "Foto2.jpg"],
        ]

        # Memuat data ke dalam tabel
        self.load_data()

    def load_data(self):
        """Memuat data ke dalam tabel."""
        self.tableWidget.setRowCount(len(self.data))
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setHorizontalHeaderLabels([
            "ID Surat Keluar", "No Agenda", "Klasifikasi", "Sifat",
            "Tanggal Surat", "Tanggal Masuk", "Perihal", "Retensi",
            "Kepada", "Foto"
        ])
        for row_idx, row_data in enumerate(self.data):
            for col_idx, value in enumerate(row_data):
                self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(value))

    def simpan_data(self):
        """Menyimpan data baru ke tabel."""
        # Ambil data dari form input
        id_surat = self.tglInput.text()
        no_agenda = self.judulInput.text()
        klasifikasi = self.linkInput.text()
        sifat = self.tglInput_2.text()
        tgl_surat = self.tglInput_3.text()
        tgl_masuk = self.judulInput_2.text()
        perihal = self.linkInput_2.text()
        retensi = self.tglInput_4.text()
        kepada = self.isiInput.toPlainText()
        foto = self.fotoInput.toPlainText()

        # Tambahkan ke data
        if all([id_surat, no_agenda, klasifikasi, sifat, tgl_surat, tgl_masuk, perihal, retensi, kepada, foto]):
            self.data.append([id_surat, no_agenda, klasifikasi, sifat, tgl_surat, tgl_masuk, perihal, retensi, kepada, foto])
            self.load_data()
            QMessageBox.information(self, "Info", "Data berhasil disimpan!")
        else:
            QMessageBox.warning(self, "Peringatan", "Semua field harus diisi!")

    def hapus_data(self):
        """Menghapus data yang dipilih di tabel."""
        selected_row = self.tableWidget.currentRow()
        if selected_row >= 0:
            self.tableWidget.removeRow(selected_row)
            del self.data[selected_row]
            QMessageBox.information(self, "Info", "Data berhasil dihapus!")
        else:
            QMessageBox.warning(self, "Peringatan", "Pilih baris yang akan dihapus!")

    def ubah_data(self):
        """Mengubah data di baris yang dipilih."""
        selected_row = self.tableWidget.currentRow()
        if selected_row >= 0:
            id_surat = self.tglInput.text()
            no_agenda = self.judulInput.text()
            klasifikasi = self.linkInput.text()
            sifat = self.tglInput_2.text()
            tgl_surat = self.tglInput_3.text()
            tgl_masuk = self.judulInput_2.text()
            perihal = self.linkInput_2.text()
            retensi = self.tglInput_4.text()
            kepada = self.isiInput.toPlainText()
            foto = self.fotoInput.toPlainText()

            if all([id_surat, no_agenda, klasifikasi, sifat, tgl_surat, tgl_masuk, perihal, retensi, kepada, foto]):
                self.data[selected_row] = [id_surat, no_agenda, klasifikasi, sifat, tgl_surat, tgl_masuk, perihal, retensi, kepada, foto]
                self.load_data()
                QMessageBox.information(self, "Info", "Data berhasil diubah!")
            else:
                QMessageBox.warning(self, "Peringatan", "Semua field harus diisi!")
        else:
            QMessageBox.warning(self, "Peringatan", "Pilih baris yang akan diubah!")

    def reload_data(self):
        """Memuat ulang data dari sumber."""
        self.load_data()
        QMessageBox.information(self, "Info", "Data berhasil dimuat ulang!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SuratKeluarForm()
    window.show()
    sys.exit(app.exec())
