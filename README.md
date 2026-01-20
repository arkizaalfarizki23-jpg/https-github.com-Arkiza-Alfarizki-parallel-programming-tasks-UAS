# Aplikasi Web Pemrosesan Paralel Menggunakan Dask

## Deskripsi Singkat
Aplikasi ini merupakan aplikasi web sederhana yang dibuat untuk menampilkan seluruh isi tabel database melalui endpoint web. Data diambil dari database menggunakan **Dask DataFrame** sehingga proses pembacaan dan pengolahan data dilakukan secara **paralel**.

Aplikasi dijalankan di dalam **Docker container** dan dapat diakses melalui browser.

---

## Teknologi yang Digunakan
- Python
- FastAPI
- Dask DataFrame
- SQLAlchemy
- SQLite
- Docker

---

## Desain Database
Aplikasi menggunakan **1 tabel database** dengan nama:

**`sensor_log`**

Struktur tabel:
| Kolom | Tipe Data |
|------|----------|
| id | Integer (Primary Key) |
| lokasi | String |
| suhu | Float |
| kelembapan | Float |

Database yang digunakan adalah **SQLite** dengan dialek SQL standar.

---

## Pemrosesan Paralel Menggunakan Dask
Pengambilan data dari database dilakukan menggunakan **Dask DataFrame** dengan fungsi berikut:

```python
dask.dataframe.read_sql_table(
    table_name="sensor_log",
    uri=DATABASE_URL,
    index_col="id",
    npartitions=2
)
