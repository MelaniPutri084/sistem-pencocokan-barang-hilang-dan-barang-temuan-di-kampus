import re
from models.register_model import RegisterModel


class RegisterController:

    @staticmethod
    def proses_register(nama, email, password, konfirmasi_password):
        nama = nama.strip()
        email = email.strip()

        # Validasi kolom kosong
        if not nama or not email or not password or not konfirmasi_password:
            return False, "Semua kolom wajib diisi."

        # Validasi format email sederhana
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return False, "Format email tidak valid."

        # Validasi panjang password
        if len(password) < 5:
            return False, "Password minimal 5 karakter."

        # Validasi kecocokan password
        if password != konfirmasi_password:
            return False, "Konfirmasi password tidak cocok."

        # Cek apakah email sudah terdaftar
        if RegisterModel.cek_email_terdaftar(email):
            return False, "Email sudah terdaftar. Gunakan email lain."

        # Simpan ke database
        return RegisterModel.tambah_pengguna(nama, email, password)