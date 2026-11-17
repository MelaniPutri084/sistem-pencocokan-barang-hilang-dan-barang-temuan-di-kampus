import customtkinter as ctk
from PIL import Image
from tkinter import messagebox


class LoginView(ctk.CTk):

    def __init__(self, on_login_success):
        super().__init__()
        self.on_login_success = on_login_success
        self.register_callback = None

        self.title("TEMUKAN - Masuk ke Sistem")
        width, height = 880, 520
        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight()
        x = (screen_w // 2) - (width // 2)
        y = (screen_h // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")
        self.resizable(False, False)
        self.configure(fg_color="#0F172A")

        # Grid Utama 2 Kolom (Kiri: Panel Branding & Logo, Kanan: Form Login)
        self.grid_columnconfigure(0, weight=5)
        self.grid_columnconfigure(1, weight=6)
        self.grid_rowconfigure(0, weight=1)

        # --- PANEL KIRI (BRANDING & LOGO KUSTOM) ---
        left_panel = ctk.CTkFrame(self, fg_color="#1D4ED8", corner_radius=0)
        left_panel.grid(row=0, column=0, sticky="nsew")

        left_inner = ctk.CTkFrame(left_panel, fg_color="transparent")
        left_inner.place(relx=0.5, rely=0.5, anchor="center")

        # Memuat Logo Kustom (logo_temukan.png)
        try:
            logo_raw = Image.open("logo_temukan.png")
            self.logo_img = ctk.CTkImage(
                light_image=logo_raw, dark_image=logo_raw, size=(100, 100)
            )
            lbl_logo = ctk.CTkLabel(left_inner, text="", image=self.logo_img)
            lbl_logo.pack(pady=(0, 2))
        except Exception:
            ctk.CTkLabel(
                left_inner, text="🔍", font=("Segoe UI Emoji", 48)
            ).pack(pady=(0, 10))

        # Judul dengan sentuhan gaya yang lebih kece & elegan
        title_box = ctk.CTkFrame(left_inner, fg_color="transparent")
        title_box.pack(pady=(2, 0))

        ctk.CTkLabel(
            title_box,
            text="T E M U K A N",
            font=("Segoe UI", 30, "bold"),
            text_color="#FFFFFF",
        ).pack()

        # Garis aksen minimalis di bawah judul
        accent_line = ctk.CTkFrame(
            title_box, width=45, height=3, fg_color="#93C5FD", corner_radius=2
        )
        accent_line.pack(pady=(6, 8))

        ctk.CTkLabel(
            left_inner,
            text="Platform Terpadu Pelaporan &\nPencarian Barang Hilang",
            font=("Segoe UI", 12),
            text_color="#DBEAFE",
            justify="center",
        ).pack(pady=(0, 18))

        # Kotak Fitur Unggulan
        feature_box = ctk.CTkFrame(
            left_inner, fg_color="#1E40AF", corner_radius=12
        )
        feature_box.pack(padx=16, pady=4, fill="x")

        ctk.CTkLabel(
            feature_box,
            text="✓ Verifikasi Laporan Real-Time\n✓ Manajemen Hak Akses Terpusat\n✓ Filter Otomatis Barang & Temuan",
            font=("Segoe UI", 11),
            text_color="#EFF6FF",
            justify="left",
        ).pack(padx=16, pady=12)

        # --- PANEL KANAN (FORM LOGIN) ---
        right_panel = ctk.CTkFrame(self, fg_color="#0F172A", corner_radius=0)
        right_panel.grid(row=0, column=1, sticky="nsew")

        form_container = ctk.CTkFrame(right_panel, fg_color="transparent")
        form_container.place(relx=0.5, rely=0.5, anchor="center")

        ctk.CTkLabel(
            form_container,
            text="Selamat Datang Kembali",
            font=("Segoe UI", 24, "bold"),
            text_color="#F8FAFC",
        ).pack(anchor="w")

        ctk.CTkLabel(
            form_container,
            text="Silakan masukkan kredensial akun Anda untuk melanjutkan.",
            font=("Segoe UI", 12),
            text_color="#94A3B8",
        ).pack(anchor="w", pady=(2, 22))

        # Input Email
        ctk.CTkLabel(
            form_container,
            text="Alamat Email",
            font=("Segoe UI", 12, "bold"),
            text_color="#CBD5E1",
        ).pack(anchor="w", pady=(0, 4))

        self.entry_email = ctk.CTkEntry(
            form_container,
            placeholder_text="nama@email.com",
            width=340,
            height=40,
            corner_radius=8,
            fg_color="#1E293B",
            border_color="#334155",
            text_color="#F8FAFC",
        )
        self.entry_email.pack(pady=(0, 14))

        # Input Password
        ctk.CTkLabel(
            form_container,
            text="Kata Sandi",
            font=("Segoe UI", 12, "bold"),
            text_color="#CBD5E1",
        ).pack(anchor="w", pady=(0, 4))

        pass_frame = ctk.CTkFrame(form_container, fg_color="transparent")
        pass_frame.pack(pady=(0, 10))

        self.entry_password = ctk.CTkEntry(
            pass_frame,
            placeholder_text="••••••••",
            show="•",
            width=284,
            height=40,
            corner_radius=8,
            fg_color="#1E293B",
            border_color="#334155",
            text_color="#F8FAFC",
        )
        self.entry_password.pack(side="left", padx=(0, 6))

        self.show_pass = False
        self.btn_toggle_pass = ctk.CTkButton(
            pass_frame,
            text="👁",
            width=48,
            height=40,
            corner_radius=8,
            fg_color="#1E293B",
            hover_color="#334155",
            command=self.toggle_password,
        )
        self.btn_toggle_pass.pack(side="left")

        # Tombol Login
        self.btn_login = ctk.CTkButton(
            form_container,
            text="Masuk ke Dashboard",
            width=340,
            height=42,
            corner_radius=8,
            font=("Segoe UI", 13, "bold"),
            fg_color="#2563EB",
            hover_color="#1D4ED8",
            command=self.login,
        )
        self.btn_login.pack(pady=(16, 8))

        # Tombol Pindah ke Pendaftaran
        self.btn_to_register = ctk.CTkButton(
            form_container,
            text="Belum punya akun? Daftar di sini",
            width=340,
            height=30,
            corner_radius=6,
            font=("Segoe UI", 11),
            fg_color="transparent",
            hover_color="#1E293B",
            text_color="#94A3B8",
            command=self.trigger_register,
        )
        self.btn_to_register.pack()

        self.bind("<Return>", lambda event: self.login())

    def toggle_password(self):
        self.show_pass = not self.show_pass
        self.entry_password.configure(show="" if self.show_pass else "•")

    def set_register_callback(self, callback):
        self.register_callback = callback

    def trigger_register(self):
        if self.register_callback:
            self.register_callback()

    def login(self):
        email = self.entry_email.get().strip()
        password = self.entry_password.get().strip()

        if not email or not password:
            messagebox.showwarning(
                "Peringatan", "Email dan kata sandi wajib diisi!"
            )
            return

        if self.on_login_success:
            self.on_login_success(email, password)