import os
import json
import tkinter as tk
from tkinter import filedialog, messagebox

LOG_FILE = "rename_log.json"

def rename_files():
    folder = filedialog.askdirectory()
    if not folder:
        return

    prefix = entry_prefix.get().strip()
    if not prefix:
        messagebox.showerror("Error", "Prefix tidak boleh kosong!")
        return

    use_filter = var_filter.get()
    ext = entry_ext.get().strip().lower()
    if use_filter and ext:
        if not ext.startswith("."):
            ext = f".{ext}"
        files = [f for f in os.listdir(folder) if f.lower().endswith(ext)]
    else:
        files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

    if not files:
        messagebox.showinfo("Info", "Tidak ada file yang cocok untuk di-rename.")
        return

    rename_map = []
    for i, filename in enumerate(files):
        file_ext = os.path.splitext(filename)[1]
        new_name = f"{prefix}_{i + 1}{file_ext}"
        old_path = os.path.join(folder, filename)
        new_path = os.path.join(folder, new_name)
        try:
            os.rename(old_path, new_path)
            rename_map.append({"old": filename, "new": new_name, "folder": folder})
        except Exception as e:
            print(f"Gagal rename {filename}: {e}")

    # Simpan log untuk undo
    with open(LOG_FILE, "w") as f:
        json.dump(rename_map, f)

    messagebox.showinfo("Sukses", f"Berhasil rename {len(rename_map)} file. Log tersimpan untuk undo.")

def undo_rename():
    if not os.path.exists(LOG_FILE):
        messagebox.showerror("Error", "Tidak ada log rename untuk di-undo.")
        return

    with open(LOG_FILE, "r") as f:
        rename_map = json.load(f)

    undo_count = 0
    for item in rename_map:
        old_path = os.path.join(item["folder"], item["new"])
        new_path = os.path.join(item["folder"], item["old"])
        if os.path.exists(old_path):
            try:
                os.rename(old_path, new_path)
                undo_count += 1
            except Exception as e:
                print(f"Gagal undo {item['new']}: {e}")

    os.remove(LOG_FILE)
    messagebox.showinfo("Undo Selesai", f"Berhasil mengembalikan {undo_count} file ke nama asal.")

# GUI
root = tk.Tk()
root.title("Rename File + Undo")
root.geometry("420x320")

tk.Label(root, text="Prefix nama file (cth: dokumen, foto):").pack(pady=5)
entry_prefix = tk.Entry(root, width=30)
entry_prefix.pack()
entry_prefix.insert(0, "file")

var_filter = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Gunakan filter ekstensi", variable=var_filter).pack(pady=10)

entry_ext = tk.Entry(root, width=20)
entry_ext.pack()
entry_ext.insert(0, "jpg")

tk.Button(root, text="Pilih Folder & Rename", command=rename_files).pack(pady=15)
tk.Button(root, text="Undo Rename", command=undo_rename).pack()

root.mainloop()