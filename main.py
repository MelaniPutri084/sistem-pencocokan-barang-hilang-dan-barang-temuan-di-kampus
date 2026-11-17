import customtkinter as ctk
from tkinter import messagebox
from views.splash_view import SplashView
from views.login_view import LoginView
from views.register_view import RegisterView
from views.laporan_view import LaporanView
from models.login_model import LoginModel
from models.laporan_model import LaporanModel
from controllers.laporan_controller import LaporanController

# Impor koneksi dari database.py milikmu
try:
    from database import get_connection
except ImportError:
    get_connection = None

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


def buka_login():
    login_model = LoginModel()

    def proses_login(email, password):
        user = login_model.cek_login(email, password)
        if user:
            if isinstance(user, dict):
                user_id = user.get("id_pengguna")
                user_role = user.get("role", "user")
            elif isinstance(user, (list, tuple)):
                user_id = user[0]
                user_role = user[3] if len(user) > 3 else "user"
            else:
                user_id = user
                user_role = "user"

            is_admin = str(user_role).lower() == "admin"

            login_view.after(10, login_view.destroy)

            laporan_view = LaporanView()
            
            # AMBIL KONEKSI LANGSUNG DARI database.py (db_temukan)
            db_conn = get_connection() if get_connection else None
            laporan_model = LaporanModel(db_conn)

            LaporanController(
                model=laporan_model,
                view=laporan_view,
                current_user_id=user_id,
                is_admin=is_admin,
                on_logout=buka_login,
            )
            laporan_view.mainloop()
        else:
            messagebox.showerror("Login Gagal", "Email atau kata sandi salah!")

    def buka_register():
        login_view.destroy()

        def proses_register(nama, email, password):
            berhasil = login_model.register(nama, email, password)
            if berhasil:
                messagebox.showinfo(
                    "Berhasil",
                    "Akun berhasil didaftarkan! Silakan masuk.",
                )
                register_view.destroy()
                buka_login()
            else:
                messagebox.showerror(
                    "Gagal",
                    "Gagal mendaftarkan akun (email mungkin sudah terdaftar).",
                )

        register_view = RegisterView(
            on_register_success=proses_register,
            on_back_to_login=lambda: (register_view.destroy(), buka_login()),
        )
        register_view.mainloop()

    login_view = LoginView(on_login_success=proses_login)
    login_view.set_register_callback(buka_register)
    login_view.mainloop()


if __name__ == "__main__":
    splash = SplashView(on_finish=buka_login)
    splash.mainloop()