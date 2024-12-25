from PyQt6.QtWidgets import QMainWindow
from forms.tb_dokumentasi_form import DokumentasiForm

class MainWindow(QMainWindow):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.dokumentasi_form = DokumentasiForm(self.ui)
        self.ui.btnDokumentasi.clicked.connect(self.open_dokumentasi_ui)

    def open_dokumentasi_ui(self):
        self.dokumentasi_form.load_data()
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageDokumentasi)
