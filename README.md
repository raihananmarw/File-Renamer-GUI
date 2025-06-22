# 📁 File Renamer GUI

**File Renamer GUI** adalah aplikasi desktop berbasis Python yang memungkinkan pengguna untuk melakukan rename banyak file sekaligus dalam sebuah folder. Aplikasi ini dilengkapi dengan antarmuka grafis (GUI) sederhana menggunakan Tkinter, serta fitur filter ekstensi, prefix kustom, dan undo rename.

---

## ✨ Fitur Utama

- ✅ Rename banyak file otomatis dalam folder
- ✅ Filter file berdasarkan ekstensi (cth: `.jpg`, `.pdf`)
- ✅ Tambahkan prefix kustom (cth: `foto_1.jpg`)
- ✅ Pilihan rename semua file tanpa filter
- ✅ Undo rename: kembalikan nama file ke kondisi awal
- ✅ Antarmuka GUI sederhana dan mudah digunakan

---

## 🧰 Teknologi yang Digunakan

- Python 3.x
- Tkinter (GUI default Python)
- Modul bawaan: `os`, `json`, `tkinter`

---

## ▶️ Cara Menjalankan

1. **Clone repositori ini** atau unduh file `rename_gui.py`
2. Pastikan Python 3 sudah terinstall
3. Jalankan dengan perintah:
   ```bash
   python rename_gui.py
4. Aplikasi GUI akan muncul dan kamu bisa:
- Menentukan prefix
- Mengaktifkan atau menonaktifkan filter ekstensi
- Memilih folder target
- Melakukan rename file
- Meng-undo rename terakhir

file-renamer-gui/
├── file_renamer.py        # File utama aplikasi
├── rename_log.json        # (Dibuat otomatis untuk menyimpan data undo)
└── README.md              # Dokumentasi proyek

⚠️ Catatan
- File rename_log.json hanya menyimpan data untuk satu kali undo terakhir.
- File hanya diproses di folder utama (tidak mencakup subfolder).
- Undo hanya bisa dilakukan sebelum rename berikutnya.

💡 Contoh Output
Jika prefix = gambar dan ekstensi = .jpg, maka:

python-repl
Copy
Edit
gambar_1.jpg
gambar_2.jpg
gambar_3.jpg
...

📜 Lisensi
Proyek ini bebas digunakan dan dimodifikasi untuk keperluan pribadi atau pembelajaran.
