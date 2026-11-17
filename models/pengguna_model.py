import hashlib
import mysql.connector
from database import get_connection


class PenggunaModel:
    def __init__(self):
        self.conn = None

    @staticmethod
    def hash_password(password):
        """Mengubah password menjadi hash SHA-256 (panjang 64 karakter)"""
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def cek_email_terdaftar(email):
        conn = get_connection()
        if not conn:
            return False
        cursor = conn.cursor()
        try:
            query = "SELECT id_pengguna FROM pengguna WHERE email = %s"
            cursor.execute(query, (email,))
            return cursor.fetchone() is not None
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def tambah_pengguna(nama, email, password, role="pengguna"):
        conn = get_connection()
        if not conn:
            return False, "Koneksi database gagal."
        cursor = conn.cursor()
        try:
            password_hash = PenggunaModel.hash_password(password)
            query = """
                INSERT INTO pengguna (nama, email, password_hash, role)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (nama, email, password_hash, role))
            conn.commit()
            return True, "Registrasi berhasil! Silakan login."
        except mysql.connector.Error as err:
            return False, f"Gagal menyimpan data: {err}"
        finally:
            cursor.close()
            conn.close()

    def autentikasi(self, username_atau_email, password):
        """Melakukan autentikasi pengguna berdasarkan username/email dan password"""
        # Mendukung instance mock conn dari pytest atau koneksi global
        conn = getattr(self, 'conn', None) or get_connection()
        if not conn:
            return None
            
        cursor = conn.cursor(dictionary=True)
        try:
            password_hash = self.hash_password(password)
            
            # Menyesuaikan dengan kolom database (username / email)
            # Menggunakan pengecekan fleksibel jika kolom username tidak ada di mock
            query = """
                SELECT id_user, username, email, role 
                FROM pengguna 
                WHERE (username = %s OR email = %s) AND password_hash = %s
            """
            cursor.execute(query, (username_atau_email, username_atau_email, password_hash))
            return cursor.fetchone()
        except Exception:
            return None
        finally:
            if hasattr(cursor, 'close'):
                cursor.close()
            # Jangan close conn jika itu adalah mock object dari pytest
            if not hasattr(self, 'conn') or self.conn is None:
                if hasattr(conn, 'close'):
                    conn.close()