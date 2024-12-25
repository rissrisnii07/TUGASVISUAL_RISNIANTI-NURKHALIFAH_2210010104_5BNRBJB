import mysql.connector

class DatabaseConnection:
    def __init__(self):
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host='127.0.0.1',
                user='root',  # Ganti sesuai username MySQL
                password='',  # Ganti sesuai password MySQL
                database='db_kantorkesatuan'
            )
            return self.connection
        except mysql.connector.Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def close(self):
        if self.connection:
            self.connection.close()
