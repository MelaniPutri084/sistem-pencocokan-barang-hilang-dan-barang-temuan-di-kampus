from unittest.mock import MagicMock

from models.laporan_model import LaporanModel


def test_get_all_berhasil(monkeypatch):
    # Membuat database tiruan
    mock_connection = MagicMock()
    mock_cursor = MagicMock()

    data_dummy = [
        {
            "id_laporan": 1,
            "id_pengguna": 1,
            "jenis_laporan": "hilang",
            "nama_barang": "Dompet",
            "deskripsi": "Dompet warna hitam",
            "kategori": "Aksesori",
            "lokasi": "Kampus",
            "tanggal_kejadian": "2026-11-10",
            "status": "aktif"
        }
    ]

    mock_connection.cursor.return_value = mock_cursor
    mock_cursor.fetchall.return_value = data_dummy

    # Mengganti koneksi database asli
    monkeypatch.setattr(
        "models.laporan_model.get_connection",
        lambda: mock_connection
    )

    model = LaporanModel()

    hasil = model.get_all()

    assert len(hasil) == 1
    assert hasil[0]["nama_barang"] == "Dompet"

    mock_cursor.execute.assert_called_once()
    mock_cursor.close.assert_called_once()
    mock_connection.close.assert_called_once()


def test_get_all_koneksi_gagal(monkeypatch):
    monkeypatch.setattr(
        "models.laporan_model.get_connection",
        lambda: None
    )

    model = LaporanModel()

    hasil = model.get_all()

    assert hasil == []


def test_get_all_database_error(monkeypatch):
    mock_connection = MagicMock()
    mock_cursor = MagicMock()

    mock_connection.cursor.return_value = mock_cursor
    mock_cursor.execute.side_effect = Exception(
        "Database error"
    )

    monkeypatch.setattr(
        "models.laporan_model.get_connection",
        lambda: mock_connection
    )

    model = LaporanModel()

    hasil = model.get_all()

    assert hasil == []
    mock_connection.close.assert_called_once()
