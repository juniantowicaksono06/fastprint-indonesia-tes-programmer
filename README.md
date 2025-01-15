## Tes Junianto Ichwan Dwi Wicaksono

Untuk menjalankan project ini bisa melakukan:

1. Pastikan Python, git, dan MySQL sudah terinstall dan sudah terhubung dengan internet.
2. Install package yang diperlukan dengan menggunakan terminal atau cmd:

```bash
pip install -r requirements.txt
```

3. Lalu silahkan buat database di mysql terlebih dahulu terserah namanya apa.

4. Kemudian clone git ini menggunakan command
```bash
git clone https://github.com/juniantowicaksono06/fastprint-indonesia-tes-programmer
```

5. Jika sudah di clone buka codenya dan copy file .env.example ke .env

6. Jika sudah silahkan buka filenya dan sesuaikan dengan konfigurasi database MySQL anda.

7. Jika sudah silahkan jalankan command berikut di cmd atau terminal:
```bash
python manage.py makemigrations # Membuat konfigurasi migrasi ke database
python manage.py apptest # Migrasi database
```

8. Lalu seed tablenya dengan command berikut:
```bash
# Silahkan ganti "\" menjadi "/" jika mengguakan linux
python manage.py loaddata fixtures\kategori.json # Seeding table kategori
python manage.py loaddata fixtures\status.json # Seeding table status
python manage.py loaddata fixtures\produk.json # Seeding table produk
```

9. Jika sudah silahkan jalankan projectnya dengan command berikut:
```bash
python manage.py runserve
```

10. Selesai