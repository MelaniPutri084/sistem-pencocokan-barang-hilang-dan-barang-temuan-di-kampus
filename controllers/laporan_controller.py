from datetime import datetime


class LaporanController:

    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.set_controller(self)
        self.tampilkan_data()

    def tampilkan_data(self):
        data = self.model.get_all()
        self.view.tampilkan_data(data)

    def tambah_laporan(self, data):
        if not data["nama_barang"].strip():
            self.view.tampilkan_pesan(
                "Peringatan",
                "Nama barang wajib diisi."
            )
            return

        if not data["lokasi"].strip():
            self.view.tampilkan_pesan(
                "Peringatan",
                "Lokasi barang wajib diisi."
            )
            return

        try:
            datetime.strptime(
                data["tanggal_kejadian"], "%Y-%m-%d"
            )
        except ValueError:
            self.view.tampilkan_pesan(
                "Peringatan",
                "Format tanggal harus YYYY-MM-DD."
            )
            return

        # Untuk pengujian awal, pengguna dengan ID 1 digunakan.
        data["id_pengguna"] = 1

        berhasil = self.model.tambah(data)

        if berhasil:
            self.view.tampilkan_pesan(
                "Berhasil",
                "Laporan berhasil ditambahkan."
            )
            self.tampilkan_data()
            self.view.kosongkan_form()
        else:
            self.view.tampilkan_pesan(
                "Gagal",
                "Laporan gagal disimpan. Periksa database."
            )

    def hapus_laporan(self, id_laporan):
        if not id_laporan:
            self.view.tampilkan_pesan(
                "Peringatan",
                "Pilih laporan yang akan dihapus."
            )
            return

        berhasil = self.model.hapus(id_laporan)

        if berhasil:
            self.view.tampilkan_pesan(
                "Berhasil",
                "Laporan berhasil dihapus."
            )
            self.tampilkan_data()
            self.view.kosongkan_form()
        else:
            self.view.tampilkan_pesan(
                "Gagal",
                "Data gagal dihapus atau masih memiliki data terkait."
            )