from unittest.mock import MagicMock

from controllers.laporan_controller import LaporanController


def buat_controller():
    model = MagicMock()
    view = MagicMock()

    controller = LaporanController(model, view)

    return controller, model, view


def data_laporan():
    return {
        "jenis_laporan": "hilang",
        "nama_barang": "Dompet",
        "kategori": "Aksesori",
        "lokasi": "Kampus",
        "tanggal_kejadian": "2026-11-10",
        "deskripsi": "Dompet warna hitam"
    }


def test_tambah_laporan_berhasil():
    controller, model, view = buat_controller()

    model.tambah.return_value = True

    controller.tambah_laporan(data_laporan())

    model.tambah.assert_called_once()
    view.kosongkan_form.assert_called_once()


def test_tambah_laporan_nama_kosong():
    controller, model, view = buat_controller()

    data = data_laporan()
    data["nama_barang"] = ""

    controller.tambah_laporan(data)

    model.tambah.assert_not_called()
    view.tampilkan_pesan.assert_called_with(
        "Peringatan",
        "Nama barang wajib diisi."
    )


def test_ubah_laporan_berhasil():
    controller, model, view = buat_controller()

    model.update.return_value = True

    controller.ubah_laporan(
        1, data_laporan()
    )

    model.update.assert_called_once_with(
        1, data_laporan()
    )

    view.kosongkan_form.assert_called_once()


def test_hapus_laporan_berhasil():
    controller, model, view = buat_controller()

    model.hapus.return_value = True

    controller.hapus_laporan(1)

    model.hapus.assert_called_once_with(1)
    view.kosongkan_form.assert_called_once()
