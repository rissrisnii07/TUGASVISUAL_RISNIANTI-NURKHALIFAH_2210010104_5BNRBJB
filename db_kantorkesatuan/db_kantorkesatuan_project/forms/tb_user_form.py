import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PyQt6.uic import loadUi


class UserForm(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('C:/Users/risni/PycharmProjects/db_kantorkesatuan/db_kantorkesatuan_project/ui/tb_user.ui', self)

        # Inisialisasi tombol dengan fungsi
        self.btnSimpan.clicked.connect(self.simpan_data)
        self.btnUbah.clicked.connect(self.ubah_data)
        self.btnHapus.clicked.connect(self.hapus_data)
        self.btnCari.clicked.connect(self.cari_data)
        self.btnClear.clicked.connect(self.reload_data)

        # Membuat tabel jika belum ada
        self.create_table()

        # Memasukkan data awal jika tabel kosong
        self.isi_data_awal()

        # Load data awal
        self.reload_data()

    def create_table(self):
        """
        Membuat tabel `tb_user` jika belum ada di database.
        """
        conn = sqlite3.connect('kantorkesatuan.db')
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tb_user (
            id_user INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_lengkap TEXT,
            nip TEXT,
            username TEXT,
            password TEXT,
            id_jabatan INTEGER,
            id_level_user INTEGER,
            foto TEXT
        )
        """)
        conn.commit()
        conn.close()

    def isi_data_awal(self):
        """
        Mengisi data awal ke tabel `tb_user` jika tabel masih kosong.
        """
        try:
            conn = sqlite3.connect('kantorkesatuan.db')
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM tb_user")
            count = cursor.fetchone()[0]

            if count == 0:  # Jika tabel kosong, tambahkan data contoh
                contoh_data = [
                    ("Ahmad Hidayat", "123456789", "ahmad", "password123", 1, 1, "foto1.jpg"),
                    ("Siti Aminah", "987654321", "siti", "password456", 2, 2, "foto2.jpg"),
                    ("Budi Santoso", "456789123", "budi", "password789", 3, 3, "foto3.jpg")
                ]
                cursor.executemany("""
                INSERT INTO tb_user (nama_lengkap, nip, username, password, id_jabatan, id_level_user, foto)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """, contoh_data)
                conn.commit()
                QMessageBox.information(self, "Data Awal", "Data awal berhasil dimasukkan ke tabel tb_user.")
            else:
                QMessageBox.information(self, "Data Awal", "Data sudah ada, tidak ada data yang dimasukkan.")

            conn.close()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"Error: {e}")

    def reload_data(self):
        """
        Memuat ulang data dari tabel `tb_user` ke dalam QTableWidget.
        """
        self.tableWidget.setRowCount(0)  # Membersihkan tabel sebelum memuat ulang data

        try:
            conn = sqlite3.connect('kantorkesatuan.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tb_user")
            rows = cursor.fetchall()

            for row_data in rows:
                row_position = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_position)
                for column, item in enumerate(row_data):
                    self.tableWidget.setItem(row_position, column, QTableWidgetItem(str(item)))

            conn.close()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"Error: {e}")

    def simpan_data(self):
        """
        Menyimpan data baru ke tabel `tb_user`.
        """
        nama_lengkap = self.namaInput.text()
        nip = self.nipInput.text()
        username = self.usernameInput.text()
        password = self.passwordInput.text()
        id_jabatan = self.jabatanInput.text()
        id_level_user = self.levelInput.text()
        foto = self.fotoInput.text()

        if not nama_lengkap or not username or not password:
            QMessageBox.warning(self, "Input Error", "Nama, Username, dan Password wajib diisi!")
            return

        try:
            conn = sqlite3.connect('kantorkesatuan.db')
            cursor = conn.cursor()
            cursor.execute("""
            INSERT INTO tb_user (nama_lengkap, nip, username, password, id_jabatan, id_level_user, foto)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (nama_lengkap, nip, username, password, id_jabatan, id_level_user, foto))
            conn.commit()
            conn.close()
            QMessageBox.information(self, "Success", "Data berhasil disimpan!")
            self.reload_data()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"Error: {e}")

    def ubah_data(self):
        """
        Mengubah data pada tabel `tb_user` berdasarkan `id_user`.
        """
        id_user = self.idInput.text()
        nama_lengkap = self.namaInput.text()
        nip = self.nipInput.text()
        username = self.usernameInput.text()
        password = self.passwordInput.text()
        id_jabatan = self.jabatanInput.text()
        id_level_user = self.levelInput.text()
        foto = self.fotoInput.text()

        if not id_user:
            QMessageBox.warning(self, "Input Error", "ID User wajib diisi untuk mengubah data!")
            return

        try:
            conn = sqlite3.connect('kantorkesatuan.db')
            cursor = conn.cursor()
            cursor.execute("""
            UPDATE tb_user
            SET nama_lengkap = ?, nip = ?, username = ?, password = ?, id_jabatan = ?, id_level_user = ?, foto = ?
            WHERE id_user = ?
            """, (nama_lengkap, nip, username, password, id_jabatan, id_level_user, foto, id_user))
            conn.commit()
            conn.close()
            QMessageBox.information(self, "Success", "Data berhasil diubah!")
            self.reload_data()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"Error: {e}")

    def hapus_data(self):
        """
        Menghapus data pada tabel `tb_user` berdasarkan `id_user`.
        """
        id_user = self.idInput.text()

        if not id_user:
            QMessageBox.warning(self, "Input Error", "ID User wajib diisi untuk menghapus data!")
            return

        try:
            conn = sqlite3.connect('kantorkesatuan.db')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tb_user WHERE id_user = ?", (id_user,))
            conn.commit()
            conn.close()
            QMessageBox.information(self, "Success", "Data berhasil dihapus!")
            self.reload_data()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"Error: {e}")

    def cari_data(self):
        """
        Mencari data berdasarkan nama lengkap atau username.
        """
        search_text = self.searchInput.text()

        if not search_text:
            QMessageBox.warning(self, "Input Error", "Masukkan kata kunci pencarian!")
            return

        self.tableWidget.setRowCount(0)  # Bersihkan tabel sebelum menampilkan data pencarian

        try:
            conn = sqlite3.connect('kantorkesatuan.db')
            cursor = conn.cursor()
            cursor.execute("""
            SELECT * FROM tb_user WHERE nama_lengkap LIKE ? OR username LIKE ?
            """, (f'%{search_text}%', f'%{search_text}%'))
            rows = cursor.fetchall()

            for row_data in rows:
                row_position = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_position)
                for column, item in enumerate(row_data):
                    self.tableWidget.setItem(row_position, column, QTableWidgetItem(str(item)))

            conn.close()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"Error: {e}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UserForm()
    window.show()
    sys.exit(app.exec())
