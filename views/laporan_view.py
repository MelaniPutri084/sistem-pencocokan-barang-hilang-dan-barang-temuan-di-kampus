import customtkinter as ctk
from PIL import Image
from tkinter import messagebox, ttk


class LaporanView(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("TEMUKAN — Dashboard Manajemen Barang Hilang & Temuan")
        self.geometry("1280x760")
        self.minsize(1080, 680)
        self.configure(fg_color="#0F172A")

        self.controller = None
        self.active_tab = "hilang"  # "hilang", "temuan", "verifikasi", "serah_terima"
        self.all_data = []

        # Styling Tabel Treeview agar menyatu dengan tema Dark Modern & Lega
        self.setup_treeview_style()

        # Grid Layout Utama: Kolom 0 (Sidebar), Kolom 1 (Konten Utama)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.build_sidebar()
        self.build_main_area()

    def setup_treeview_style(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Modern.Treeview",
            background="#1E293B",
            foreground="#F8FAFC",
            fieldbackground="#1E293B",
            borderwidth=0,
            rowheight=42,
            font=("Segoe UI", 10),
        )
        style.configure(
            "Modern.Treeview.Heading",
            background="#0F172A",
            foreground="#94A3B8",
            relief="flat",
            font=("Segoe UI", 10, "bold"),
            padding=(10, 12),
        )
        style.map(
            "Modern.Treeview",
            background=[("selected", "#2563EB")],
            foreground=[("selected", "#FFFFFF")],
        )
        style.map(
            "Modern.Treeview.Heading",
            background=[("active", "#1E293B")],
        )

    def set_controller(self, controller):
        self.controller = controller
        is_admin = getattr(self.controller, "is_admin", False)

        if is_admin:
            self.lbl_role_badge.configure(
                text="★ MODE ADMINISTRATOR",
                fg_color="#7C3AED",
                text_color="#FFFFFF",
            )
            self.lbl_role_desc.configure(
                text="Akses Verifikasi Klaim & Serah Terima"
            )
            # Tampilkan menu khusus Admin di sidebar
            self.btn_nav_verifikasi.pack(fill="x", padx=16, pady=4)
            self.btn_nav_serah.pack(fill="x", padx=16, pady=4)
        else:
            self.lbl_role_badge.configure(
                text="● MODE PENGGUNA",
                fg_color="#0284C7",
                text_color="#FFFFFF",
            )
            self.lbl_role_desc.configure(
                text="Kelola Laporan & Pengajuan Klaim"
            )
            # Sembunyikan menu khusus Admin
            self.btn_nav_verifikasi.pack_forget()
            self.btn_nav_serah.pack_forget()

    def build_sidebar(self):
        self.sidebar = ctk.CTkFrame(
            self,
            width=250,
            corner_radius=0,
            fg_color="#1E293B",
            border_width=1,
            border_color="#334155",
        )
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_propagate(False)

        brand_frame = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        brand_frame.pack(fill="x", padx=20, pady=(20, 14))

        # Memuat Logo Kustom di Sidebar
        try:
            logo_raw = Image.open("logo_temukan.png")
            self.sidebar_logo = ctk.CTkImage(
                light_image=logo_raw, dark_image=logo_raw, size=(32, 32)
            )
            lbl_logo = ctk.CTkLabel(
                brand_frame, text="", image=self.sidebar_logo
            )
            lbl_logo.pack(anchor="w", pady=(0, 4))
        except Exception:
            pass

        ctk.CTkLabel(
            brand_frame,
            text="TEMUKAN",
            font=("Segoe UI", 18, "bold"),
            text_color="#F8FAFC",
        ).pack(anchor="w")

        ctk.CTkLabel(
            brand_frame,
            text="Lost & Found System",
            font=("Segoe UI", 10),
            text_color="#64748B",
        ).pack(anchor="w")

        role_card = ctk.CTkFrame(
            self.sidebar, fg_color="#0F172A", corner_radius=12
        )
        role_card.pack(fill="x", padx=16, pady=(0, 20))

        self.lbl_role_badge = ctk.CTkLabel(
            role_card,
            text="● MEMUAT ROLE...",
            font=("Segoe UI", 10, "bold"),
            fg_color="#334155",
            corner_radius=6,
            padx=8,
            pady=3,
        )
        self.lbl_role_badge.pack(anchor="w", padx=12, pady=(12, 6))

        self.lbl_role_desc = ctk.CTkLabel(
            role_card,
            text="Memverifikasi sesi...",
            font=("Segoe UI", 11),
            text_color="#94A3B8",
            wraplength=190,
            justify="left",
        )
        self.lbl_role_desc.pack(anchor="w", padx=12, pady=(0, 12))

        ctk.CTkLabel(
            self.sidebar,
            text="MENU UTAMA",
            font=("Segoe UI", 10, "bold"),
            text_color="#64748B",
        ).pack(anchor="w", padx=22, pady=(0, 8))

        # Tombol Navigasi Sesuai Use Case
        self.btn_nav_hilang = ctk.CTkButton(
            self.sidebar,
            text="  📦  Barang Hilang",
            anchor="w",
            height=40,
            corner_radius=10,
            font=("Segoe UI", 12, "bold"),
            fg_color="#2563EB",
            hover_color="#1D4ED8",
            command=lambda: self.switch_menu("hilang"),
        )
        self.btn_nav_hilang.pack(fill="x", padx=16, pady=3)

        self.btn_nav_temuan = ctk.CTkButton(
            self.sidebar,
            text="  ✨  Barang Temuan",
            anchor="w",
            height=40,
            corner_radius=10,
            font=("Segoe UI", 12, "bold"),
            fg_color="transparent",
            hover_color="#334155",
            text_color="#CBD5E1",
            command=lambda: self.switch_menu("temuan"),
        )
        self.btn_nav_temuan.pack(fill="x", padx=16, pady=3)

        # Menu khusus untuk Admin (Verifikasi & Serah Terima)
        self.btn_nav_verifikasi = ctk.CTkButton(
            self.sidebar,
            text="  🛡️  Verifikasi Klaim",
            anchor="w",
            height=40,
            corner_radius=10,
            font=("Segoe UI", 12, "bold"),
            fg_color="transparent",
            hover_color="#334155",
            text_color="#CBD5E1",
            command=lambda: self.switch_menu("verifikasi"),
        )

        self.btn_nav_serah = ctk.CTkButton(
            self.sidebar,
            text="  🤝  Catat Serah Terima",
            anchor="w",
            height=40,
            corner_radius=10,
            font=("Segoe UI", 12, "bold"),
            fg_color="transparent",
            hover_color="#334155",
            text_color="#CBD5E1",
            command=lambda: self.switch_menu("serah_terima"),
        )

        ctk.CTkButton(
            self.sidebar,
            text="🚪  Keluar / Logout",
            height=40,
            corner_radius=10,
            font=("Segoe UI", 12, "bold"),
            fg_color="#DC2626",
            hover_color="#B91C1C",
            command=lambda: self.controller.logout()
            if self.controller
            else None,
        ).pack(side="bottom", fill="x", padx=16, pady=20)

    def build_main_area(self):
        self.main_area = ctk.CTkFrame(self, fg_color="transparent")
        self.main_area.grid(row=0, column=1, sticky="nsew", padx=24, pady=20)
        self.main_area.grid_columnconfigure(0, weight=1)
        self.main_area.grid_rowconfigure(3, weight=1)

        header_frame = ctk.CTkFrame(self.main_area, fg_color="transparent")
        header_frame.grid(row=0, column=0, sticky="ew", pady=(0, 16))

        self.lbl_page_title = ctk.CTkLabel(
            header_frame,
            text="Manajemen Laporan Barang Hilang",
            font=("Segoe UI", 22, "bold"),
            text_color="#F8FAFC",
        )
        self.lbl_page_title.pack(side="left")

        ctk.CTkButton(
            header_frame,
            text="↻ Segarkan Data",
            width=130,
            height=36,
            corner_radius=8,
            fg_color="#1E293B",
            hover_color="#334155",
            border_width=1,
            border_color="#334155",
            command=lambda: self.controller.refresh_data()
            if self.controller
            else None,
        ).pack(side="right")

        # KPI Cards
        kpi_frame = ctk.CTkFrame(self.main_area, fg_color="transparent")
        kpi_frame.grid(row=1, column=0, sticky="ew", pady=(0, 16))
        kpi_frame.grid_columnconfigure((0, 1, 2), weight=1)

        self.lbl_stat_total = self.create_kpi_card(
            kpi_frame, 0, "TOTAL LAPORAN AKTIF", "0", "#3B82F6"
        )
        self.lbl_stat_hilang = self.create_kpi_card(
            kpi_frame, 1, "BARANG HILANG", "0", "#F59E0B"
        )
        self.lbl_stat_temuan = self.create_kpi_card(
            kpi_frame, 2, "BARANG TEMUAN", "0", "#10B981"
        )

        # Form Input Card
        form_card = ctk.CTkFrame(
            self.main_area,
            fg_color="#1E293B",
            corner_radius=14,
            border_width=1,
            border_color="#334155",
        )
        form_card.grid(row=2, column=0, sticky="ew", pady=(0, 16))
        form_card.grid_columnconfigure((0, 1, 2), weight=1)

        self.lbl_form_header = ctk.CTkLabel(
            form_card,
            text="+ Tambah Laporan Barang Hilang Baru",
            font=("Segoe UI", 14, "bold"),
            text_color="#F8FAFC",
        )
        self.lbl_form_header.grid(
            row=0, column=0, columnspan=3, sticky="w", padx=18, pady=(14, 10)
        )

        self.entry_nama = self.create_input_field(
            form_card, 1, 0, "Nama Barang *", "Contoh: Jam Tangan Casio"
        )
        self.entry_kategori = self.create_input_field(
            form_card, 1, 1, "Kategori", "Contoh: Aksesoris / Elektronik"
        )
        self.entry_lokasi = self.create_input_field(
            form_card, 1, 2, "Lokasi Kejadian *", "Contoh: Gedung Perpustakaan"
        )

        self.entry_tanggal = self.create_input_field(
            form_card, 2, 0, "Tanggal (YYYY-MM-DD)", "2026-11-15"
        )
        self.entry_deskripsi = self.create_input_field(
            form_card,
            2,
            1,
            "Ciri-ciri / Deskripsi Barang",
            "Warna hitam, tali kulit...",
        )

        btn_box = ctk.CTkFrame(form_card, fg_color="transparent")
        btn_box.grid(row=2, column=2, sticky="sew", padx=18, pady=(24, 14))

        self.btn_submit = ctk.CTkButton(
            btn_box,
            text="Simpan Laporan Hilang",
            height=38,
            corner_radius=8,
            font=("Segoe UI", 12, "bold"),
            fg_color="#10B981",
            hover_color="#059669",
            command=self.simpan_laporan,
        )
        self.btn_submit.pack(fill="x")

        # Table Card
        table_card = ctk.CTkFrame(
            self.main_area,
            fg_color="#1E293B",
            corner_radius=14,
            border_width=1,
            border_color="#334155",
        )
        table_card.grid(row=3, column=0, sticky="nsew")
        table_card.grid_rowconfigure(1, weight=1)
        table_card.grid_columnconfigure(0, weight=1)

        toolbar = ctk.CTkFrame(table_card, fg_color="transparent")
        toolbar.grid(row=0, column=0, sticky="ew", padx=20, pady=(16, 12))

        self.lbl_table_title = ctk.CTkLabel(
            toolbar,
            text="📋 Daftar Barang Hilang Tercatat",
            font=("Segoe UI", 15, "bold"),
            text_color="#F8FAFC",
        )
        self.lbl_table_title.pack(side="left")

        btn_action_box = ctk.CTkFrame(toolbar, fg_color="transparent")
        btn_action_box.pack(side="right")

        ctk.CTkButton(
            btn_action_box,
            text="🔍 Lihat Detail & Klaim",
            width=160,
            height=36,
            corner_radius=8,
            font=("Segoe UI", 12, "bold"),
            fg_color="#2563EB",
            hover_color="#1D4ED8",
            command=self.lihat_detail,
        ).pack(side="left", padx=(0, 10))

        ctk.CTkButton(
            btn_action_box,
            text="🗑 Hapus Terpilih",
            width=130,
            height=36,
            corner_radius=8,
            font=("Segoe UI", 12, "bold"),
            fg_color="#DC2626",
            hover_color="#B91C1C",
            command=self.hapus_terpilih,
        ).pack(side="left")

        tree_wrap = ctk.CTkFrame(table_card, fg_color="transparent")
        tree_wrap.grid(row=1, column=0, sticky="nsew", padx=16, pady=(0, 16))

        columns = (
            "id",
            "jenis",
            "nama",
            "kategori",
            "lokasi",
            "deskripsi",
            "tanggal",
            "status",
        )
        self.tree = ttk.Treeview(
            tree_wrap,
            columns=columns,
            show="headings",
            style="Modern.Treeview",
        )

        headers = {
            "id": ("ID", 50),
            "jenis": ("Jenis", 90),
            "nama": ("Nama Barang", 180),
            "kategori": ("Kategori", 120),
            "lokasi": ("Lokasi", 160),
            "deskripsi": ("Deskripsi / Ciri-Ciri", 250),
            "tanggal": ("Tanggal", 110),
            "status": ("Status", 90),
        }

        for col, (text, width) in headers.items():
            self.tree.heading(col, text=text)
            anchor = (
                "center" if col in ("id", "jenis", "tanggal", "status") else "w"
            )
            self.tree.column(col, width=width, anchor=anchor)

        self.tree.bind("<Double-1>", lambda event: self.lihat_detail())

        scrollbar = ttk.Scrollbar(
            tree_wrap, orient="vertical", command=self.tree.yview
        )
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def create_kpi_card(self, parent, col, title, value, accent_color):
        card = ctk.CTkFrame(
            parent,
            fg_color="#1E293B",
            corner_radius=12,
            border_width=1,
            border_color="#334155",
        )
        padx = (0, 8) if col == 0 else ((8, 0) if col == 2 else (4, 4))
        card.grid(row=0, column=col, sticky="ew", padx=padx)

        bar = ctk.CTkFrame(card, width=5, fg_color=accent_color, corner_radius=4)
        bar.pack(side="left", fill="y", padx=(12, 12), pady=12)

        info = ctk.CTkFrame(card, fg_color="transparent")
        info.pack(side="left", fill="both", expand=True, pady=10)

        ctk.CTkLabel(
            info,
            text=title,
            font=("Segoe UI", 10, "bold"),
            text_color="#94A3B8",
        ).pack(anchor="w")

        val_lbl = ctk.CTkLabel(
            info,
            text=value,
            font=("Segoe UI", 22, "bold"),
            text_color="#F8FAFC",
        )
        val_lbl.pack(anchor="w")
        return val_lbl

    def create_input_field(self, parent, row, col, label_text, placeholder):
        box = ctk.CTkFrame(parent, fg_color="transparent")
        box.grid(row=row, column=col, sticky="ew", padx=18, pady=(4, 12))

        ctk.CTkLabel(
            box,
            text=label_text,
            font=("Segoe UI", 11, "bold"),
            text_color="#CBD5E1",
        ).pack(anchor="w", pady=(0, 4))

        entry = ctk.CTkEntry(
            box,
            placeholder_text=placeholder,
            height=38,
            corner_radius=8,
            fg_color="#0F172A",
            border_color="#334155",
            text_color="#F8FAFC",
        )
        entry.pack(fill="x")
        return entry

    def switch_menu(self, jenis):
        self.active_tab = jenis
        
        # Atur warna tombol aktif di sidebar
        for btn in [self.btn_nav_hilang, self.btn_nav_temuan, self.btn_nav_verifikasi, self.btn_nav_serah]:
            btn.configure(fg_color="transparent", text_color="#CBD5E1")

        if jenis == "hilang":
            self.btn_nav_hilang.configure(fg_color="#2563EB", text_color="#FFFFFF")
            self.lbl_page_title.configure(text="Manajemen Laporan Barang Hilang")
            self.lbl_form_header.configure(text="+ Tambah Laporan Barang Hilang Baru")
            self.btn_submit.configure(text="Simpan Laporan Hilang", fg_color="#10B981", hover_color="#059669")
            self.lbl_table_title.configure(text="📋 Daftar Barang Hilang Tercatat")
        elif jenis == "temuan":
            self.btn_nav_temuan.configure(fg_color="#10B981", text_color="#FFFFFF")
            self.lbl_page_title.configure(text="Manajemen Laporan Barang Temuan")
            self.lbl_form_header.configure(text="+ Tambah Laporan Barang Temuan Baru")
            self.btn_submit.configure(text="Simpan Laporan Temuan", fg_color="#10B981", hover_color="#059669")
            self.lbl_table_title.configure(text="📋 Daftar Barang Temuan Tercatat")
        elif jenis == "verifikasi":
            self.btn_nav_verifikasi.configure(fg_color="#7C3AED", text_color="#FFFFFF")
            self.lbl_page_title.configure(text="Panel Verifikasi Klaim Barang")
            self.lbl_table_title.configure(text="🛡️ Daftar Pengajuan Klaim Masuk (Pending)")
        elif jenis == "serah_terima":
            self.btn_nav_serah.configure(fg_color="#7C3AED", text_color="#FFFFFF")
            self.lbl_page_title.configure(text="Pencatatan Serah Terima Barang")
            self.lbl_table_title.configure(text="🤝 Riwayat Serah Terima / Aktif")

        self.render_table()

    def simpan_laporan(self):
        data = {
            "jenis_laporan": self.active_tab if self.active_tab in ["hilang", "temuan"] else "hilang",
            "nama_barang": self.entry_nama.get().strip(),
            "kategori": self.entry_kategori.get().strip(),
            "lokasi": self.entry_lokasi.get().strip(),
            "tanggal_kejadian": self.entry_tanggal.get().strip() or "2026-11-15",
            "deskripsi": self.entry_deskripsi.get().strip(),
        }

        if not data["nama_barang"] or not data["lokasi"]:
            messagebox.showwarning(
                "Data Belum Lengkap",
                "Nama barang dan lokasi kejadian wajib diisi!",
            )
            return

        if self.controller:
            self.controller.tambah_laporan(data)

    def tampilkan_data(self, data):
        self.all_data = data or []

        total = len(self.all_data)
        jml_hilang = sum(1 for d in self.all_data if d.get("jenis_laporan") == "hilang")
        jml_temuan = sum(1 for d in self.all_data if d.get("jenis_laporan") == "temuan")

        self.lbl_stat_total.configure(text=str(total))
        self.lbl_stat_hilang.configure(text=str(jml_hilang))
        self.lbl_stat_temuan.configure(text=str(jml_temuan))

        self.render_table()

    def render_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for item in self.all_data:
            j_lap = item.get("jenis_laporan", "hilang")
            status_item = str(item.get("status", "PENDING")).upper()

            # Filter tampilan berdasarkan tab aktif di sidebar
            if self.active_tab == "verifikasi":
                if status_item != "PENDING":
                    continue
            elif self.active_tab == "serah_terima":
                if status_item not in ["AKTIF", "SELESAI"]:
                    continue
            else:
                if j_lap != self.active_tab:
                    continue

            jenis_teks = "📦 HILANG" if j_lap == "hilang" else "✨ TEMUAN"
            if status_item == "AKTIF":
                status_teks = "🟢 AKTIF"
            elif status_item == "PENDING":
                status_teks = "🟡 PENDING"
            else:
                status_teks = f"⚪ {status_item}"

            deskripsi_teks = item.get("deskripsi") or "-"

            self.tree.insert(
                "",
                "end",
                values=(
                    f"#{item['id_laporan']}",
                    jenis_teks,
                    item["nama_barang"],
                    item["kategori"] or "-",
                    item["lokasi"],
                    deskripsi_teks,
                    item["tanggal_kejadian"],
                    status_teks,
                ),
            )

    def lihat_detail(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showinfo(
                "Info", "Pilih salah satu baris data pada tabel untuk melihat detail."
            )
            return

        item_data = self.tree.item(selected[0])["values"]
        id_str = item_data[0].replace("#", "")
        jenis = item_data[1]
        nama = item_data[2]
        kategori = item_data[3]
        lokasi = item_data[4]
        deskripsi = item_data[5]
        tanggal = item_data[6]
        status = item_data[7]

        popup = ctk.CTkToplevel(self)
        popup.title(f"Detail Laporan #{id_str} - {nama}")
        popup.geometry("520x500")
        popup.resizable(False, False)
        popup.configure(fg_color="#0F172A")
        popup.grab_set()

        card = ctk.CTkFrame(
            popup,
            fg_color="#1E293B",
            corner_radius=16,
            border_width=1,
            border_color="#334155",
        )
        card.pack(fill="both", expand=True, padx=16, pady=16)

        ctk.CTkLabel(
            card,
            text="✨ Detail Informasi Laporan",
            font=("Segoe UI", 16, "bold"),
            text_color="#F8FAFC",
        ).pack(anchor="w", padx=24, pady=(18, 10))

        info_frame = ctk.CTkFrame(card, fg_color="#0F172A", corner_radius=10)
        info_frame.pack(fill="x", padx=24, pady=(0, 10))

        info_text = (
            f"Nomor ID        : #{id_str}\n"
            f"Jenis Laporan : {jenis}\n"
            f"Nama Barang   : {nama}\n"
            f"Kategori         : {kategori}\n"
            f"Lokasi Kejadian: {lokasi}\n"
            f"Tanggal Kejadian: {tanggal}\n"
            f"Status Sesi     : {status}"
        )

        ctk.CTkLabel(
            info_frame,
            text=info_text,
            font=("Segoe UI", 12),
            text_color="#CBD5E1",
            justify="left",
        ).pack(anchor="w", padx=16, pady=12)

        ctk.CTkLabel(
            card,
            text="Deskripsi / Ciri-Ciri Barang:",
            font=("Segoe UI", 11, "bold"),
            text_color="#94A3B8",
        ).pack(anchor="w", padx=24, pady=(0, 4))

        desc_box = ctk.CTkFrame(card, fg_color="#0F172A", corner_radius=10)
        desc_box.pack(fill="x", padx=24, pady=(0, 14))

        ctk.CTkLabel(
            desc_box,
            text=deskripsi,
            font=("Segoe UI", 12),
            text_color="#F8FAFC",
            justify="left",
            wraplength=420,
        ).pack(anchor="w", padx=16, pady=10)

        btn_action_frame = ctk.CTkFrame(card, fg_color="transparent")
        btn_action_frame.pack(fill="x", padx=24, pady=(0, 14))

        is_admin = getattr(self.controller, "is_admin", False)
        if is_admin:
            def setujui_laporan():
                if self.controller:
                    self.controller.ubah_status_laporan(id_str, "AKTIF")
                    messagebox.showinfo("Sukses", f"Laporan #{id_str} berhasil diverifikasi dan diaktifkan!")
                    popup.destroy()

            ctk.CTkButton(
                btn_action_frame,
                text="🛡️ Setujui & Aktifkan Laporan (Verifikasi)",
                height=38,
                corner_radius=8,
                fg_color="#7C3AED",
                hover_color="#6D28D9",
                font=("Segoe UI", 11, "bold"),
                command=setujui_laporan,
            ).pack(fill="x")
        else:
            ctk.CTkButton(
                btn_action_frame,
                text="🤝 Ajukan Klaim Kepemilikan",
                height=38,
                corner_radius=8,
                fg_color="#2563EB",
                hover_color="#1D4ED8",
                font=("Segoe UI", 11, "bold"),
                command=lambda: messagebox.showinfo("Klaim", f"Pengajuan klaim untuk #{id_str} terkirim ke Admin."),
            ).pack(fill="x")

        ctk.CTkButton(
            card,
            text="Tutup Jendela",
            width=120,
            height=32,
            corner_radius=8,
            fg_color="#334155",
            hover_color="#475569",
            font=("Segoe UI", 11, "bold"),
            command=popup.destroy,
        ).pack(anchor="e", padx=24, pady=(0, 14))

    def hapus_terpilih(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showinfo(
                "Info", "Pilih salah satu baris data pada tabel terlebih dahulu."
            )
            return

        item_data = self.tree.item(selected[0])["values"]
        id_str = item_data[0].replace("#", "")
        nama_barang = item_data[2]

        if messagebox.askyesno(
            "Konfirmasi Hapus",
            f"Yakin ingin menghapus laporan '{nama_barang}' (ID: {id_str})?",
        ):
            if self.controller:
                self.controller.hapus_laporan(id_str)

    def tampilkan_pesan(self, judul, pesan):
        if "Berhasil" in judul or "Sukses" in judul:
            messagebox.showinfo(judul, pesan)
        else:
            messagebox.showerror(judul, pesan)

    def kosongkan_form(self):
        self.entry_nama.delete(0, "end")
        self.entry_kategori.delete(0, "end")
        self.entry_lokasi.delete(0, "end")
        self.entry_tanggal.delete(0, "end")
        self.entry_deskripsi.delete(0, "end")