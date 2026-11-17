from database import get_connection
import mysql.connector


class RegisterModel:

    @staticmethod
    def cek_email_terdaftar(email):
        conn = get_connection()
        if conn is None:
            return False
        cursor = conn.cursor()
        try:
            query = "SELECT id_pengguna FROM pengguna WHERE email = %s LIMIT 1"
            cursor.execute(query, (email,))
            return cursor.fetchone() is not None
        except Exception as e:
            print("Error cek email:", e)
            return False
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def tambah_pengguna(nama, email, password):
        conn = get_connection()
        if conn is None:
            return False, "Koneksi database gagal."

        cursor = conn.cursor()
        try:
            query = """
                INSERT INTO pengguna (nama, email, password)
                VALUES (%s, %s, %s)
            """
            cursor.execute(query, (nama, email, password))
            conn.commit()
            return True, "Registrasi berhasil! Silakan login."
        except mysql.connector.Error as err:
            return False, f"Gagal mendaftar: {err}"
        except Exception as e:
            return False, f"Terjadi kesalahan: {e}"
        finally:
            cursor.close()
            conn.close()