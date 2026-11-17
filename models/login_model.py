from database import get_connection


class LoginModel:

    def cek_login(self, email, password):
        """Memeriksa kredensial email dan password untuk proses login."""
        connection = get_connection()
        if connection is None:
            return None

        cursor = None
        try:
            # Menggunakan dictionary=True agar hasil query berupa dictionary (mudah diakses via key)
            cursor = connection.cursor(dictionary=True)
            query = """
                SELECT id_pengguna, nama, email, role 
                FROM pengguna 
                WHERE email = %s AND password = %s
            """
            cursor.execute(query, (email, password))
            user = cursor.fetchone()
            return user
        except Exception as e:
            print("ERROR DATABASE SAAT CEK LOGIN:", repr(e))
            return None
        finally:
            if cursor is not None:
                cursor.close()
            connection.close()

    def register(self, nama, email, password):
        """Mendaftarkan akun pengguna baru dengan role default 'user'."""
        connection = get_connection()
        if connection is None:
            return False

        cursor = None
        try:
            cursor = connection.cursor()
            query = """
                INSERT INTO pengguna (nama, email, password, role)
                VALUES (%s, %s, %s, 'user')
            """
            cursor.execute(query, (nama, email, password))
            connection.commit()
            return True
        except Exception as e:
            print("ERROR DATABASE SAAT REGISTER:", repr(e))
            connection.rollback()
            return False
        finally:
            if cursor is not None:
                cursor.close()
            connection.close()