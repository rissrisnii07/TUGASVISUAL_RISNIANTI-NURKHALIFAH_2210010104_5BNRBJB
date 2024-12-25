from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from PyQt6.uic import loadUi
from rokok_form import RokokForm

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('rokok_manager.ui', self)  # Memuat UI utama

        self.rokok_list = [
            {"id": "a1", "nama": "Sampoerna Mild", "harga": "Rp 330.000 ", "stok": 5},
            {"id": "la4", "nama": "L.A Ice Purple", "harga": "Rp 320.000", "stok": 8},
            {"id": "crs3", "nama": "Crystal Coffee", "harga": "Rp 150.000", "stok": 10}
        ]  # Daftar rokok
        self.btn_tambah.clicked.connect(self.tambah_rokok)
        self.btn_hapus.clicked.connect(self.hapus_rokok)
        self.btn_ubah.clicked.connect(self.ubah_rokok)

        self.load_data()  # Memuat data awal

    def load_data(self):
        """Mengisi tabel dengan data dari self.rokok_list."""
        self.table_rokok.setRowCount(0)
        for row_number, rokok in enumerate(self.rokok_list):
            self.table_rokok.insertRow(row_number)
            self.table_rokok.setItem(row_number, 0, QTableWidgetItem(str(rokok["id"])))
            self.table_rokok.setItem(row_number, 1, QTableWidgetItem(rokok["nama"]))
            self.table_rokok.setItem(row_number, 2, QTableWidgetItem(str(rokok["harga"])))
            self.table_rokok.setItem(row_number, 3, QTableWidgetItem(str(rokok["stok"])))

    def tambah_rokok(self):
        """Menampilkan form untuk menambah rokok."""
        def refresh():
            self.load_data()

        self.form = RokokForm(self.rokok_list, refresh)
        self.form.show()

    def ubah_rokok(self):
        """Mengubah data rokok yang dipilih."""
        row = self.table_rokok.currentRow()
        if row == -1:
            QMessageBox.warning(self, "Error", "Pilih rokok yang ingin diubah!")
            return

        rokok_id = int(self.table_rokok.item(row, 0).text())
        rokok = next((r for r in self.rokok_list if r['id'] == rokok_id), None)
        if not rokok:
            QMessageBox.warning(self, "Error", "Data tidak ditemukan!")
            return

        def refresh():
            self.load_data()

        self.form = RokokForm(self.rokok_list, refresh)
        self.form.input_nama.setText(rokok["nama"])
        self.form.input_harga.setValue(rokok["harga"])
        self.form.input_stok.setValue(rokok["stok"])
        self.form.rokok_id = rokok["id"]
        self.form.show()

    def hapus_rokok(self):
        """Menghapus data rokok yang dipilih."""
        row = self.table_rokok.currentRow()
        if row == -1:
            QMessageBox.warning(self, "Error", "Pilih rokok yang ingin dihapus!")
            return

        rokok_id = int(self.table_rokok.item(row, 0).text())
        self.rokok_list = [r for r in self.rokok_list if r['id'] != rokok_id]
        self.load_data()
        QMessageBox.information(self, "Success", "Rokok berhasil dihapus!")

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    main_window = MainApp()
    main_window.show()
    sys.exit(app.exec())
