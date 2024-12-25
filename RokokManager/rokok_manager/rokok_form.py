from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6.uic import loadUi

class RokokForm(QDialog):
    def __init__(self, rokok_list, refresh_callback):
        super().__init__()
        loadUi('rokok_form.ui', self)  # Memuat desain UI
        self.rokok_list = rokok_list  # Referensi ke daftar rokok
        self.refresh_callback = refresh_callback  # Callback untuk refresh tabel

        # Hubungkan tombol dengan fungsinya
        self.btn_simpan.clicked.connect(self.simpan_rokok)
        self.btn_batal.clicked.connect(self.close)

    def simpan_rokok(self):
        id = self.input_id.text()
        nama = self.input_nama.text()
        harga = self.input_harga.value()
        stok = self.input_stok.value()

        # Validasi input, pastikan nama tidak kosong
        if not nama:
            QMessageBox.warning(self, "Error", "Nama rokok harus diisi!")
            return

        # Menambahkan rokok baru tanpa input ID
        rokok_id = len(self.rokok_list) + 1  # ID otomatis berdasarkan panjang list
        self.rokok_list.append({"id": rokok_id, "nama": nama, "harga": harga, "stok": stok})

        # Memanggil callback untuk refresh tabel di Main Window
        self.refresh_callback()


