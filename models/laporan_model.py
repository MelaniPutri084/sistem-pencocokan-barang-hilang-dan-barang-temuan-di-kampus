from database import get_connection


class LaporanModel:

    def get_all(self):
        connection = get_connection()

        if connection is None:
            return []

        cursor = None

        try:
            cursor = connection.cursor(dictionary=True)

            query = """
                SELECT
                    id_laporan,
                    id_pengguna,
                    jenis_laporan,
                    nama_barang,
                    deskripsi,
                    kategori,
                    lokasi,
                    tanggal_kejadian,
                    status
                FROM laporan
                ORDER BY id_laporan DESC
            """

            cursor.execute(query)
            data = cursor.fetchall()

            return data

        except Exception as e:
            print("ERROR DATABASE SAAT MENGAMBIL DATA:", repr(e))
            return []

        finally:
            if cursor is not None:
                cursor.close()

            connection.close()

    def tambah(self, data):
        connection = get_connection()

        if connection is None:
            print("ERROR: Koneksi database gagal.")
            return False

        cursor = None

        try:
            cursor = connection.cursor()

            query = """
                INSERT INTO laporan (
                    id_pengguna,
                    jenis_laporan,
                    nama_barang,
                    deskripsi,
                    kategori,
                    lokasi,
                    tanggal_kejadian,
                    status
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """

            nilai = (
                data["id_pengguna"],
                data["jenis_laporan"],
                data["nama_barang"],
                data["deskripsi"],
                data["kategori"],
                data["lokasi"],
                data["tanggal_kejadian"],
                "aktif"
            )

            cursor.execute(query, nilai)
            connection.commit()

            print("Laporan berhasil disimpan.")
            return True

        except Exception as e:
            print(
                "ERROR DATABASE SAAT MENAMBAH LAPORAN:",
                repr(e)
            )

            connection.rollback()
            return False

        finally:
            if cursor is not None:
                cursor.close()

            connection.close()

    def hapus(self, id_laporan):
        connection = get_connection()

        if connection is None:
            print("ERROR: Koneksi database gagal.")
            return False

        cursor = None

        try:
            cursor = connection.cursor()

            query = """
                DELETE FROM laporan
                WHERE id_laporan = %s
            """

            cursor.execute(query, (id_laporan,))
            jumlah_data = cursor.rowcount

            connection.commit()

            if jumlah_data > 0:
                print("Laporan berhasil dihapus.")
                return True

            print("Laporan tidak ditemukan.")
            return False

        except Exception as e:
            print(
                "ERROR DATABASE SAAT MENGHAPUS LAPORAN:",
                repr(e)
            )

            connection.rollback()
            return False

        finally:
            if cursor is not None:
                cursor.close()

            connection.close()
