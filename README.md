# TEMUKAN

**TEMUKAN** merupakan aplikasi berbasis Python yang dikembangkan dengan menerapkan arsitektur Model-View-Controller (MVC). Aplikasi ini dirancang untuk membantu pengguna dalam menggunakan fitur-fitur yang tersedia melalui antarmuka aplikasi yang terintegrasi dengan pengelolaan data dan database.

## Deskripsi Proyek

Proyek TEMUKAN dikembangkan menggunakan bahasa pemrograman Python dengan pendekatan arsitektur MVC. Arsitektur ini memisahkan bagian pengelolaan data, tampilan, dan pengendalian alur aplikasi agar kode program lebih terstruktur, mudah dipahami, serta lebih mudah dikembangkan dan dipelihara.

Aplikasi ini juga dilengkapi dengan pengujian menggunakan Pytest serta pemeriksaan kualitas kode menggunakan Flake8 yang diintegrasikan ke dalam GitHub Actions.

## Teknologi yang Digunakan

- **Bahasa Pemrograman:** Python
- **Arsitektur:** Model-View-Controller (MVC)
- **Database:** MySQL
- **Pengujian:** Pytest
- **Pemeriksaan Kualitas Kode:** Flake8
- **Version Control:** Git dan GitHub
- **CI/CD:** GitHub Actions
- **Packaging Aplikasi:** PyInstaller

## Struktur Direktori

Berikut merupakan struktur direktori utama proyek TEMUKAN:

```text
TEMUKAN/
│
├── .github/
│   └── workflows/
│       └── ci_pipeline.yml
│
├── controllers/
│   └── File pengendali aplikasi
│
├── models/
│   └── File pengelolaan data
│
├── views/
│   └── File tampilan aplikasi
│
├── tests/
│   └── File pengujian aplikasi
│
├── dist/
│   └── File aplikasi hasil build
│
├── main.py
├── database.py
├── requirements.txt
├── AplikasiTemukan.spec
└── README.md
```

### Penjelasan Direktori

- **controllers/**: Berisi kode program yang mengatur alur aplikasi dan menghubungkan model dengan tampilan.
- **models/**: Berisi kode yang menangani pengelolaan data dan proses yang berkaitan dengan database.
- **views/**: Berisi komponen yang bertanggung jawab terhadap tampilan antarmuka aplikasi.
- **tests/**: Berisi kode pengujian untuk memastikan fungsi aplikasi berjalan sesuai harapan.
- **.github/workflows/**: Berisi konfigurasi GitHub Actions untuk menjalankan proses pemeriksaan dan pengujian otomatis.
- **dist/**: Menyimpan hasil proses build aplikasi yang dibuat menggunakan PyInstaller.

## Persyaratan Sistem

Sebelum menjalankan aplikasi, pastikan perangkat telah memiliki:

1. Python.
2. MySQL Server.
3. Git (jika ingin mengambil proyek dari GitHub).
4. Library yang tercantum dalam `requirements.txt`.

## Instalasi dan Persiapan

### 1. Mengambil Proyek

Clone repository TEMUKAN dari GitHub:

```bash
git clone URL_REPOSITORY_TEMUKAN
```

Masuk ke direktori proyek:

```bash
cd TEMUKAN
```

Ganti `URL_REPOSITORY_TEMUKAN` dengan alamat repository GitHub proyek yang sebenarnya.

### 2. Membuat Virtual Environment

Buat lingkungan virtual Python:

```bash
python -m venv .venv
```

Aktifkan virtual environment pada Windows PowerShell:

```powershell
.venv\Scripts\Activate
```

### 3. Menginstal Library

Instal seluruh dependensi yang dibutuhkan:

```bash
pip install -r requirements.txt
```

## Konfigurasi Database

Aplikasi menggunakan MySQL sebagai sistem pengelolaan database.

Sebelum menjalankan aplikasi, lakukan langkah berikut:

1. Pastikan MySQL Server sudah aktif.
2. Siapkan database yang dibutuhkan oleh aplikasi.
3. Periksa konfigurasi koneksi database pada file `database.py`.
4. Sesuaikan host, username, password, dan nama database berdasarkan konfigurasi MySQL pada perangkat masing-masing.

Pastikan konfigurasi database sudah benar agar aplikasi dapat terhubung dengan database.

## Menjalankan Aplikasi

Setelah proses instalasi dan konfigurasi selesai, jalankan aplikasi melalui terminal dengan perintah:

```bash
python main.py
```

## Pengujian Aplikasi

Pengujian dilakukan menggunakan Pytest untuk memeriksa fungsi-fungsi aplikasi.

Jalankan perintah berikut:

```bash
pytest
```

## Pemeriksaan Kualitas Kode

Proyek TEMUKAN menggunakan Flake8 untuk melakukan pemeriksaan kualitas kode Python.

Jalankan perintah:

```bash
flake8 models/ controllers/ --count --select=E9,F63,F7,F82 --show-source --statistics
```

Pemeriksaan ini membantu mendeteksi kesalahan kode yang berpotensi mengganggu jalannya aplikasi.

## Continuous Integration (CI)

Proyek TEMUKAN menggunakan GitHub Actions untuk menjalankan proses pemeriksaan kode dan pengujian secara otomatis.

Pipeline CI mencakup:
1. Menyiapkan lingkungan Python.
2. Menginstal dependensi proyek.
3. Melakukan pemeriksaan kualitas kode menggunakan Flake8.
4. Menjalankan pengujian menggunakan Pytest.

Proses ini membantu memastikan bahwa perubahan kode dapat diperiksa secara otomatis sebelum digunakan lebih lanjut.

## Versi Aplikasi

**Versi:** 1.0.0

**Nama Aplikasi:** TEMUKAN

**Format Distribusi:** Executable (.exe)

---

**TEMUKAN - Project Documentation**
