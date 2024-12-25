from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from PyQt6 import uic

class JabatanForm(QMainWindow):
    def __init__(self):
        super().__init__()
        # Load file UI
        uic.loadUi('C:/Users/risni/PycharmProjects/db_kantorkesatuan/db_kantorkesatuan_project/ui/tb_jabatan.ui', self)

        # Hubungkan tombol dengan fungsi
        self.btnSimpan.clicked.connect(self.simpan_data)
        self.btnUbah.clicked.connect(self.ubah_data)
        self.btnHapus.clicked.connect(self.hapus_data)
        self.btnClear.clicked.connect(self.reload_data)
        self.pushButton.clicked.connect(self.cari_data)

        # Isi data awal (opsional)
        self.fill_sample_data()

    def fill_sample_data(self):
        """Mengisi tabel dengan data awal (contoh)."""
        sample_data = [
            ["1", "KJ001", "Manager"],
            ["2", "KJ002", "Supervisor"],
            ["3", "KJ003", "Staff"],
        ]
        for row in sample_data:
            self.tambah_ke_tabel(row)

    def tambah_ke_tabel(self, data):
        """Menambahkan data ke tabel."""
        row_count = self.tableJabatan.rowCount()
        self.tableJabatan.insertRow(row_count)
        for col, value in enumerate(data):
            self.tableJabatan.setItem(row_count, col, QTableWidgetItem(value))

    def simpan_data(self):
        """Menyimpan data baru ke tabel."""
        kode_jabatan = self.cari.text()
        nama_jabatan = self.nama_level_input.text()
        if not kode_jabatan or not nama_jabatan:
            QMessageBox.warning(self, "Error", "Harap isi semua field!")
            return

        id_jabatan = str(self.tableJabatan.rowCount() + 1)
        self.tambah_ke_tabel([id_jabatan, kode_jabatan, nama_jabatan])
        QMessageBox.information(self, "Berhasil", "Data berhasil disimpan!")

    def ubah_data(self):
        """Mengubah data yang dipilih di tabel."""
        selected_row = self.tableJabatan.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Pilih baris yang ingin diubah!")
            return

        kode_jabatan = self.cari.text()
        nama_jabatan = self.nama_level_input.text()
        if not kode_jabatan or not nama_jabatan:
            QMessageBox.warning(self, "Error", "Harap isi semua field!")
            return

        self.tableJabatan.setItem(selected_row, 1, QTableWidgetItem(kode_jabatan))
        self.tableJabatan.setItem(selected_row, 2, QTableWidgetItem(nama_jabatan))
        QMessageBox.information(self, "Berhasil", "Data berhasil diubah!")

    def hapus_data(self):
        """Menghapus data yang dipilih di tabel."""
        selected_row = self.tableJabatan.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Pilih baris yang ingin dihapus!")
            return

        self.tableJabatan.removeRow(selected_row)
        QMessageBox.information(self, "Berhasil", "Data berhasil dihapus!")

    def reload_data(self):
        """Menghapus semua data di tabel dan mengisi ulang dengan data awal."""
        self.tableJabatan.setRowCount(0)
        self.fill_sample_data()
        QMessageBox.information(self, "Berhasil", "Data berhasil di-reload!")

    def cari_data(self):
        """Mencari data berdasarkan input kode atau nama jabatan."""
        keyword = self.cari.text().strip().lower()
        if not keyword:
            QMessageBox.warning(self, "Error", "Masukkan kata kunci untuk mencari!")
            return

        matched_rows = []
        for row in range(self.tableJabatan.rowCount()):
            kode_jabatan = self.tableJabatan.item(row, 1).text().lower()
            nama_jabatan = self.tableJabatan.item(row, 2).text().lower()
            if keyword in kode_jabatan or keyword in nama_jabatan:
                matched_rows.append(row)

        # Highlight matched rows
        for row in range(self.tableJabatan.rowCount()):
            self.tableJabatan.setRowHidden(row, row not in matched_rows)

        if not matched_rows:
            QMessageBox.information(self, "Hasil", "Tidak ada data yang cocok dengan kata kunci.")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = JabatanForm()
    window.show()
    sys.exit(app.exec())
