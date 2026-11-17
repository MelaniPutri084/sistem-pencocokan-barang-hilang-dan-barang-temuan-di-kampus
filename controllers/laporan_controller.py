
class LaporanController:
    def __init__(self, model, view, current_user_id=1, is_admin=False, on_logout=None):
        self.model = model
        self.view = view
        self.current_user_id = current_user_id
        self.is_admin = is_admin
        self.on_logout = on_logout

        if hasattr(self.view, "set_controller"):
            self.view.set_controller(self)

        self.refresh_data()

    def refresh_data(self):
        """Mengambil dan menampilkan seluruh data laporan."""
        try:
            if hasattr(self.model, "ambil_semua"):
                data_laporan = self.model.ambil_semua()
            else:
                data_laporan = self.model.get_all()

            if not self.is_admin:
                filtered_data = [
                    laporan for laporan in data_laporan
                    if str(laporan.get("id_pengguna", "1"))
                    == str(self.current_user_id)
                ]
                data_laporan = filtered_data if filtered_data else data_laporan

            if hasattr(self.view, "tampilkan_data"):
                self.view.tampilkan_data(data_laporan)

        except Exception as e:
            print(f"Error pada refresh_data controller: {e}")

    def tambah_laporan(self, data_form):
        """Menambahkan laporan baru dengan validasi."""
        try:
            # Validasi nama barang
            nama_barang = data_form.get("nama_barang", "")

            if not isinstance(nama_barang, str) or not nama_barang.strip():
                if hasattr(self.view, "tampilkan_pesan"):
                    self.view.tampilkan_pesan(
                        "Peringatan",
                        "Nama barang wajib diisi."
                    )
                return

            # Salin data agar data asli tidak berubah
            data_form = data_form.copy()

            data_form["id_pengguna"] = self.current_user_id

            if not data_form.get("status"):
                data_form["status"] = (
                    "PENDING" if not self.is_admin else "AKTIF"
                )

            # Simpan laporan
            if hasattr(self.model, "tambah"):
                berhasil = self.model.tambah(data_form)
            else:
                berhasil = self.model.simpan(data_form)

            if berhasil:
                self.refresh_data()

                if hasattr(self.view, "kosongkan_form"):
                    self.view.kosongkan_form()

                if hasattr(self.view, "tampilkan_pesan"):
                    self.view.tampilkan_pesan(
                        "Berhasil",
                        "Laporan berhasil disimpan dan menunggu verifikasi Admin!"
                    )
            else:
                if hasattr(self.view, "tampilkan_pesan"):
                    self.view.tampilkan_pesan(
                        "Gagal",
                        "Terjadi kesalahan saat menyimpan laporan."
                    )

        except Exception as e:
            print(f"Error tambah_laporan: {e}")

    def ubah_laporan(self, id_laporan, data_form):
        """Mengubah data laporan."""
        try:
            berhasil = self.model.update(id_laporan, data_form)

            if berhasil:
                self.refresh_data()

                if hasattr(self.view, "kosongkan_form"):
                    self.view.kosongkan_form()

                if hasattr(self.view, "tampilkan_pesan"):
                    self.view.tampilkan_pesan(
                        "Berhasil",
                        "Laporan berhasil diubah!"
                    )
            else:
                if hasattr(self.view, "tampilkan_pesan"):
                    self.view.tampilkan_pesan(
                        "Gagal",
                        "Gagal mengubah laporan."
                    )

        except Exception as e:
            print(f"Error ubah_laporan: {e}")

    def hapus_laporan(self, id_laporan):
        """Menghapus laporan berdasarkan ID."""
        try:
            berhasil = self.model.hapus(id_laporan)

            if berhasil:
                self.refresh_data()

                if hasattr(self.view, "kosongkan_form"):
                    self.view.kosongkan_form()

                if hasattr(self.view, "tampilkan_pesan"):
                    self.view.tampilkan_pesan(
                        "Berhasil",
                        "Laporan berhasil dihapus!"
                    )
            else:
                print("Gagal menghapus laporan.")

        except Exception as e:
            print(f"Error hapus_laporan: {e}")

    def ubah_status_laporan(self, id_laporan, status_baru):
        """Mengubah status laporan oleh Admin."""
        try:
            if not self.is_admin:
                print("Akses ditolak: Hanya admin yang dapat mengubah status.")
                return

            berhasil = self.model.update_status(
                id_laporan,
                status_baru
            )

            if berhasil:
                self.refresh_data()
            else:
                print("Gagal memperbarui status laporan.")

        except Exception as e:
            print(f"Error ubah_status_laporan: {e}")

    def logout(self):
        """Menangani proses logout."""
        if self.on_logout:
            if hasattr(self.view, "destroy"):
                self.view.destroy()

            self.on_logout()
