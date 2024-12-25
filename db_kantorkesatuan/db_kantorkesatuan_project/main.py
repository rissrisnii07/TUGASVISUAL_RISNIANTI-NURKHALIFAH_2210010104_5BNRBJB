import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.uic import loadUi

from forms.tb_dokumentasi_form import DokumentasiForm
from forms.tb_jabatan_form import JabatanForm
from forms.tb_klasifikasi_form import KlasifikasiForm
from forms.tb_leveluser_form import LevelUserForm
from forms.tb_slider_form import SliderForm
from forms.tb_suratkeluar_form import SuratKeluarForm
from forms.tb_suratmasuk_form import SuratMasukForm
from forms.tb_user_form import UserForm

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()

        try:
            # Muat file UI
            loadUi("mainwindow.ui", self)

            self.btnDokumentasi.clicked.connect(self.open_dokumentasi)
            self.btnJabatan.clicked.connect(self.open_jabatan)
            self.btnKlasifikasi.clicked.connect(self.open_klasifikasi)
            self.btnLevelUser.clicked.connect(self.open_leveluser)
            self.btnSlider.clicked.connect(self.open_slider)
            self.btnSuratKeluar.clicked.connect(self.open_suratkeluar)
            self.btnSuratMasuk.clicked.connect(self.open_suratmasuk)
            self.btnUser.clicked.connect(self.open_user)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal memuat file UI: {e}")
            exit()

    # Fungsi untuk membuka form masing-masing
    def open_dokumentasi(self):

            try:
                print("Membuka DokumentasiForm...")
                self.dokumentasi_window = DokumentasiForm()
                self.dokumentasi_window.show()
            except Exception as e:
                print(f"Error saat membuka DokumentasiForm: {e}")
                QMessageBox.critical(self, "Error", f"Terjadi kesalahan: {e}")

    def open_jabatan(self):
        self.jabatan_window = JabatanForm()
        self.jabatan_window.show()

    def open_klasifikasi(self):
        self.klasifikasi_window = KlasifikasiForm()
        self.klasifikasi_window.show()

    def open_leveluser(self):
        self.leveluser_window = LevelUserForm()
        self.leveluser_window.show()

    def open_slider(self):
        self.slider_window = SliderForm()
        self.slider_window.show()

    def open_suratkeluar(self):
        self.suratkeluar_window = SuratKeluarForm()
        self.suratkeluar_window.show()

    def open_suratmasuk(self):
        self.suratmasuk_window = SuratMasukForm()
        self.suratmasuk_window.show()

    def open_user(self):
        self.user_window = UserForm()
        self.user_window.show()

# Jalankan aplikasi
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainApp()
    main_window.show()
    sys.exit(app.exec())
