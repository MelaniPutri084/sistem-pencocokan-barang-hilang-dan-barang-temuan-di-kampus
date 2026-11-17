import customtkinter as ctk
from PIL import Image


class SplashView(ctk.CTk):

    def __init__(self, on_finish):
        super().__init__()
        self.on_finish = on_finish

        # Menghilangkan border jendela bawaan (frameless)
        self.overrideredirect(True)

        width, height = 520, 340
        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight()
        x = (screen_w // 2) - (width // 2)
        y = (screen_h // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

        self.configure(fg_color="#0F172A")
        self.attributes("-alpha", 0.0)

        # Kartu Utama Splash Screen
        self.card = ctk.CTkFrame(
            self,
            fg_color="#1E293B",
            corner_radius=18,
            border_width=1,
            border_color="#334155",
        )
        self.card.pack(fill="both", expand=True, padx=12, pady=12)

        # Memuat Logo Kustom (logo_temukan.png)
        try:
            logo_raw = Image.open("logo_temukan.png")
            self.logo_img = ctk.CTkImage(
                light_image=logo_raw, dark_image=logo_raw, size=(96, 96)
            )
            self.badge = ctk.CTkLabel(self.card, text="", image=self.logo_img)
        except Exception:
            # Cadangan jika file logo belum tersedia di folder
            self.badge = ctk.CTkLabel(
                self.card,
                text="🔍",
                font=("Segoe UI Emoji", 40),
                fg_color="#2563EB",
                width=72,
                height=72,
                corner_radius=18,
                text_color="#FFFFFF",
            )
        self.badge.pack(pady=(30, 10))

        # Judul Aplikasi
        self.lbl_title = ctk.CTkLabel(
            self.card,
            text="TEMUKAN",
            font=("Segoe UI", 28, "bold"),
            text_color="#F8FAFC",
        )
        self.lbl_title.pack()

        # Subjudul
        self.lbl_sub = ctk.CTkLabel(
            self.card,
            text="Sistem Informasi Manajemen Barang Hilang & Temuan",
            font=("Segoe UI", 12),
            text_color="#94A3B8",
        )
        self.lbl_sub.pack(pady=(2, 25))

        # Progress Bar Modern
        self.progress = ctk.CTkProgressBar(
            self.card,
            width=380,
            height=8,
            corner_radius=4,
            fg_color="#0F172A",
            progress_color="#3B82F6",
        )
        self.progress.set(0)
        self.progress.pack(pady=(0, 10))

        # Status Teks Muat Modul
        self.lbl_status = ctk.CTkLabel(
            self.card,
            text="Menyiapkan koneksi sistem...",
            font=("Segoe UI", 11),
            text_color="#64748B",
        )
        self.lbl_status.pack()

        self.step = 0
        self.alpha = 0.0
        self.animate_fade_in()

    def animate_fade_in(self):
        if self.alpha < 1.0:
            self.alpha += 0.08
            self.attributes("-alpha", min(self.alpha, 1.0))
            self.after(20, self.animate_fade_in)
        else:
            self.animate_progress()

    def animate_progress(self):
        if self.step <= 100:
            self.progress.set(self.step / 100)
            
            # Ubah teks status secara dinamis saat loading berjalan
            if self.step == 30:
                self.lbl_status.configure(text="Memuat modul autentikasi...")
            elif self.step == 70:
                self.lbl_status.configure(text="Menghubungkan ke database...")
            elif self.step == 95:
                self.lbl_status.configure(text="Hampir selesai...")

            self.step += 3
            self.after(25, self.animate_progress)
        else:
            self.after(300, self.finish)

    def finish(self):
        self.destroy()
        if self.on_finish:
            self.on_finish()