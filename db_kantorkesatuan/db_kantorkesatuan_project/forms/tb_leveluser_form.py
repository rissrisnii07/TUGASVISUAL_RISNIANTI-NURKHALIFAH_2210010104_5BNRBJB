from PyQt6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PyQt6.uic import loadUi
import sys


class LevelUserForm(QWidget):
    def __init__(self):
        super().__init__()
        loadUi("C:/Users/risni/PycharmProjects/db_kantorkesatuan/db_kantorkesatuan_project/ui/tb_leveluser.ui", self)

        # Event listeners for buttons
        self.btnSimpan.clicked.connect(self.add_data)
        self.btnHapus.clicked.connect(self.delete_data)
        self.btnUbah.clicked.connect(self.update_data)
        self.btnClear.clicked.connect(self.clear_inputs)
        self.pushButton.clicked.connect(self.search_data)

        # Setup the table with predefined fields
        self.setup_table()

    def setup_table(self):
        self.tableWidget.setColumnCount(2)  # Two fields: ID Level User, Nama Level
        self.tableWidget.setHorizontalHeaderLabels(["ID Level User", "Nama Level"])

        # Example data to populate the table
        example_data = [
            ["1", "Admin"],
            ["2", "Manager"],
            ["3", "Staff"],
        ]

        for row_data in example_data:
            self.add_table_row(row_data)

    def add_table_row(self, row_data):
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)

        for column, data in enumerate(row_data):
            self.tableWidget.setItem(row_position, column, QTableWidgetItem(data))

    def add_data(self):
        id_level_user = self.id_leve_input.text()
        nama_level = self.nama_level_input.text()

        if not id_level_user or not nama_level:
            QMessageBox.warning(self, "Input Error", "Semua field harus diisi!")
            return

        self.add_table_row([id_level_user, nama_level])
        QMessageBox.information(self, "Success", "Data berhasil ditambahkan.")
        self.clear_inputs()

    def delete_data(self):
        current_row = self.tableWidget.currentRow()
        if current_row == -1:
            QMessageBox.warning(self, "Selection Error", "Pilih baris yang akan dihapus!")
            return

        self.tableWidget.removeRow(current_row)
        QMessageBox.information(self, "Success", "Data berhasil dihapus.")

    def update_data(self):
        current_row = self.tableWidget.currentRow()
        if current_row == -1:
            QMessageBox.warning(self, "Selection Error", "Pilih baris yang akan diperbarui!")
            return

        id_level_user = self.id_leve_input.text()
        nama_level = self.nama_level_input.text()

        if not id_level_user or not nama_level:
            QMessageBox.warning(self, "Input Error", "Semua field harus diisi!")
            return

        self.tableWidget.setItem(current_row, 0, QTableWidgetItem(id_level_user))
        self.tableWidget.setItem(current_row, 1, QTableWidgetItem(nama_level))
        QMessageBox.information(self, "Success", "Data berhasil diperbarui.")
        self.clear_inputs()

    def clear_inputs(self):
        self.id_leve_input.clear()
        self.nama_level_input.clear()

    def search_data(self):
        search_query = self.cari.text().lower()
        if not search_query:
            QMessageBox.warning(self, "Search Error", "Masukkan kata kunci untuk pencarian!")
            return

        for row in range(self.tableWidget.rowCount()):
            match = False
            for column in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, column)
                if search_query in item.text().lower():
                    match = True
                    break

            self.tableWidget.setRowHidden(row, not match)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LevelUserForm()
    window.show()
    sys.exit(app.exec())
