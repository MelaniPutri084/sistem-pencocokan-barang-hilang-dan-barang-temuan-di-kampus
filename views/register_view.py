import customtkinter as ctk
from tkinter import messagebox


class RegisterView(ctk.CTk):
    def __init__(self, on_register_success, on_back_to_login):
        super().__init__()
        self.on_register_success = on_register_success
        self.on_back_to_login = on_back_to_login

        self.title("TEMUKAN - Pendaftaran Akun Baru")
        width, height = 880, 560
        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight()
        x = (screen_w // 2) - (width // 2)
        y = (screen_h // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")
        self.resizable(False, False)
        self.configure(fg_color="#0F172A")

        # Grid 2 Kolom (Kiri Branding, Kanan Form Register)
        self.grid_columnconfigure(0, weight=5)
        self.grid_columnconfigure(1, weight=6)
        self.grid_rowconfigure(0, weight=1)

        # --- PANEL KIRI (BRANDING) ---
        left_panel = ctk.CTkFrame(
            self, fg_color="#1D4ED8", corner_radius=0
        )
        left_panel.grid(row=0, column=0, sticky="nsew")

        left_inner = ctk.CTkFrame(left_panel, fg_color="transparent")
        left_inner.place(relx=0.5, rely=0.5, anchor="center")

        ctk.CTkLabel(
            left_inner,
            text="✨",
            font=("Segoe UI Emoji", 54),
        ).pack(pady=(0, 10))

        ctk.CTkLabel(
            left_inner,
            text="Bergabunglah",
            font=("Segoe UI", 32, "bold"),
            text_color="#FFFFFF",
        ).pack()

        ctk.CTkLabel(
            left_inner,
            text="Buat akun baru untuk mulai melaporkan\ndan mencari barang hilang dengan mudah.",
            font=("Segoe UI", 13),
            text_color="#DBEAFE",
            justify="center",
        ).pack(pady=(8, 25))

        # --- PANEL KANAN (FORM REGISTER) ---
        right_panel = ctk.CTkFrame(
            self, fg_color="#0F172A", corner_radius=0
        )
        right_panel.grid(row=0, column=1, sticky="nsew")

        form_container = ctk.CTkFrame(right_panel, fg_color="transparent")
        form_container.place(relx=0.5, rely=0.5, anchor="center")

        ctk.CTkLabel(
            form_container,
            text="Daftar Akun Baru",
            font=("Segoe UI", 22, "bold"),
            text_color="#F8FAFC",
        ).pack(anchor="w")

        ctk.CTkLabel(
            form_container,
            text="Lengkapi data diri Anda di bawah ini.",
            font=("Segoe UI", 11),
            text_color="#94A3B8",
        ).pack(anchor="w", pady=(2, 16))

        # Input Nama Lengkap
        ctk.CTkLabel(
            form_container,
            text="Nama Lengkap",
            font=("Segoe UI", 11, "bold"),
            text_color="#CBD5E1",
        ).pack(anchor="w", pady=(0, 4))

        self.entry_nama = ctk.CTkEntry(
            form_container,
            placeholder_text="Nama Lengkap Anda",
            width=340,
            height=38,
            corner_radius=8,
            fg_color="#1E293B",
            border_color="#334155",
            text_color="#F8FAFC",
        )
        self.entry_nama.pack(pady=(0, 10))

        # Input Email
        ctk.CTkLabel(
            form_container,
            text="Alamat Email",
            font=("Segoe UI", 11, "bold"),
            text_color="#CBD5E1",
        ).pack(anchor="w", pady=(0, 4))

        self.entry_email = ctk.CTkEntry(
            form_container,
            placeholder_text="nama@email.com",
            width=340,
            height=38,
            corner_radius=8,
            fg_color="#1E293B",
            border_color="#334155",
            text_color="#F8FAFC",
        )
        self.entry_email.pack(pady=(0, 10))

        # Input Password
        ctk.CTkLabel(
            form_container,
            text="Kata Sandi",
            font=("Segoe UI", 11, "bold"),
            text_color="#CBD5E1",
        ).pack(anchor="w", pady=(0, 4))

        self.entry_password = ctk.CTkEntry(
            form_container,
            placeholder_text="••••••••",
            show="•",
            width=340,
            height=38,
            corner_radius=8,
            fg_color="#1E293B",
            border_color="#334155",
            text_color="#F8FAFC",
        )
        self.entry_password.pack(pady=(0, 16))

        # Tombol Daftar
        self.btn_register = ctk.CTkButton(
            form_container,
            text="Daftar Sekarang",
            width=340,
            height=40,
            corner_radius=8,
            font=("Segoe UI", 12, "bold"),
            fg_color="#2563EB",
            hover_color="#1D4ED8",
            command=self.register,
        )
        self.btn_register.pack(pady=(0, 10))

        # Tombol Kembali ke Login
        self.btn_back = ctk.CTkButton(
            form_container,
            text="Sudah punya akun? Masuk di sini",
            width=340,
            height=32,
            corner_radius=8,
            font=("Segoe UI", 11),
            fg_color="transparent",
            hover_color="#1E293B",
            text_color="#94A3B8",
            command=self.on_back_to_login,
        )
        self.btn_back.pack()

    def register(self):
        nama = self.entry_nama.get().strip()
        email = self.entry_email.get().strip()
        password = self.entry_password.get().strip()

        if not nama or not email or not password:
            messagebox.showwarning(
                "Peringatan", "Semua kolom wajib diisi!"
            )
            return

        if self.on_register_success:
            self.on_register_success(nama, email, password)