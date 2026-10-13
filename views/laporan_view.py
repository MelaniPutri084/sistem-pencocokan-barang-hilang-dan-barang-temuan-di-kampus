import customtkinter as ctk
from tkinter import ttk, messagebox


class LaporanView(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("TEMUKAN - Laporan Barang")
        self.geometry("1100x700")
        self.minsize(900, 600)

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.controller = None
        self.selected_id = None

        self.buat_tampilan()

    def set_controller(self, controller):
        self.controller = controller

    def buat_tampilan(self):
        judul = ctk.CTkLabel(
            self,
            text="TEMUKAN",
            font=ctk.CTkFont(size=30, weight="bold")
        )
        judul.pack(pady=(20, 5))

        subjudul = ctk.CTkLabel(
            self,
            text="Sistem Informasi Barang Hilang dan Temuan",
            font=ctk.CTkFont(size=15)
        )
        subjudul.pack(pady=(0, 20))

        form = ctk.CTkFrame(self)
        form.pack(fill="x", padx=25, pady=10)

        ctk.CTkLabel(
            form, text="Jenis Laporan"
        ).grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.jenis = ctk.CTkOptionMenu(
            form,
            values=["hilang", "temuan"],
            width=220
        )
        self.jenis.grid(row=0, column=1, padx=10, pady=10)

        ctk.CTkLabel(
            form, text="Nama Barang"
        ).grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.nama = ctk.CTkEntry(
            form, width=300, placeholder_text="Masukkan nama barang"
        )
        self.nama.grid(row=1, column=1, padx=10, pady=10)

        ctk.CTkLabel(
            form, text="Kategori"
        ).grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.kategori = ctk.CTkEntry(
            form, width=300, placeholder_text="Contoh: Elektronik"
        )
        self.kategori.grid(row=2, column=1, padx=10, pady=10)

        ctk.CTkLabel(
            form, text="Lokasi"
        ).grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.lokasi = ctk.CTkEntry(
            form, width=300, placeholder_text="Lokasi kejadian"
        )
        self.lokasi.grid(row=3, column=1, padx=10, pady=10)

        ctk.CTkLabel(
            form, text="Tanggal Kejadian"
        ).grid(row=4, column=0, padx=10, pady=10, sticky="w")

        self.tanggal = ctk.CTkEntry(
            form, width=300, placeholder_text="YYYY-MM-DD"
        )
        self.tanggal.grid(row=4, column=1, padx=10, pady=10)

        ctk.CTkLabel(
            form, text="Deskripsi"
        ).grid(row=5, column=0, padx=10, pady=10, sticky="w")

        self.deskripsi = ctk.CTkTextbox(
            form, width=300, height=70
        )
        self.deskripsi.grid(row=5, column=1, padx=10, pady=10)

        tombol = ctk.CTkFrame(self, fg_color="transparent")
        tombol.pack(pady=10)

        ctk.CTkButton(
            tombol,
            text="Tambah Laporan",
            command=self.aksi_tambah
        ).pack(side="left", padx=8)

        ctk.CTkButton(
            tombol,
            text="Hapus Laporan",
            fg_color="#C0392B",
            hover_color="#922B21",
            command=self.aksi_hapus
        ).pack(side="left", padx=8)

        ctk.CTkButton(
            tombol,
            text="Muat Ulang",
            command=self.aksi_muat_ulang
        ).pack(side="left", padx=8)

        tabel_frame = ctk.CTkFrame(self)
        tabel_frame.pack(fill="both", expand=True, padx=25, pady=15)

        kolom = (
            "id", "jenis", "nama", "kategori",
            "lokasi", "tanggal", "status"
        )

        self.tabel = ttk.Treeview(
            tabel_frame,
            columns=kolom,
            show="headings",
            height=10
        )

        judul_kolom = {
            "id": "ID",
            "jenis": "Jenis",
            "nama": "Nama Barang",
            "kategori": "Kategori",
            "lokasi": "Lokasi",
            "tanggal": "Tanggal",
            "status": "Status"
        }

        for nama_kolom, teks in judul_kolom.items():
            self.tabel.heading(nama_kolom, text=teks)
            self.tabel.column(nama_kolom, width=120, anchor="center")

        self.tabel.column("nama", width=180)
        self.tabel.column("lokasi", width=160)

        scrollbar = ttk.Scrollbar(
            tabel_frame,
            orient="vertical",
            command=self.tabel.yview
        )
        self.tabel.configure(yscrollcommand=scrollbar.set)

        self.tabel.pack(
            side="left", fill="both", expand=True, padx=5, pady=5
        )
        scrollbar.pack(side="right", fill="y", pady=5)

        self.tabel.bind(
            "<<TreeviewSelect>>", self.pilih_data
        )

    def aksi_tambah(self):
        data = {
            "jenis_laporan": self.jenis.get(),
            "nama_barang": self.nama.get(),
            "kategori": self.kategori.get(),
            "lokasi": self.lokasi.get(),
            "tanggal_kejadian": self.tanggal.get(),
            "deskripsi": self.deskripsi.get("1.0", "end-1c")
        }

        self.controller.tambah_laporan(data)

    def aksi_hapus(self):
        self.controller.hapus_laporan(self.selected_id)

    def aksi_muat_ulang(self):
        self.controller.tampilkan_data()

    def tampilkan_data(self, data):
        for item in self.tabel.get_children():
            self.tabel.delete(item)

        for baris in data:
            self.tabel.insert(
                "",
                "end",
                values=(
                    baris["id_laporan"],
                    baris["jenis_laporan"],
                    baris["nama_barang"],
                    baris["kategori"] or "",
                    baris["lokasi"] or "",
                    baris["tanggal_kejadian"] or "",
                    baris["status"]
                )
            )

    def pilih_data(self, event=None):
        pilihan = self.tabel.selection()

        if pilihan:
            nilai = self.tabel.item(pilihan[0], "values")
            self.selected_id = nilai[0]
        else:
            self.selected_id = None

    def kosongkan_form(self):
        self.nama.delete(0, "end")
        self.kategori.delete(0, "end")
        self.lokasi.delete(0, "end")
        self.tanggal.delete(0, "end")
        self.deskripsi.delete("1.0", "end")
        self.selected_id = None

    def tampilkan_pesan(self, judul, pesan):
        if judul == "Berhasil":
            messagebox.showinfo(judul, pesan, parent=self)
        elif judul == "Peringatan":
            messagebox.showwarning(judul, pesan, parent=self)
        else:
            messagebox.showerror(judul, pesan, parent=self)
