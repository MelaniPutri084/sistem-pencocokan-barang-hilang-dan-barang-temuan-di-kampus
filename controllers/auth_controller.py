import re
from models.pengguna_model import PenggunaModel


class AuthController:

    @staticmethod
    def proses_register(nama, email, password, konfirmasi_password):
        # Validasi kolom kosong
        if (
            not nama.strip()
            or not email.strip()
            or not password
            or not konfirmasi_password
        ):
            return False, "Semua kolom wajib diisi!"

        # Validasi format email sederhana
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return False, "Format email tidak valid!"

        # Validasi panjang dan kecocokan password
        if len(password) < 6:
            return False, "Kata sandi minimal 6 karakter!"
        if password != konfirmasi_password:
            return False, "Konfirmasi kata sandi tidak cocok!"

        # Cek duplikasi email di database
        if PenggunaModel.cek_email_terdaftar(email):
            return False, "Email sudah terdaftar. Gunakan email lain."

        # Simpan ke database
        return PenggunaModel.tambah_pengguna(nama.strip(), email.strip(), password)