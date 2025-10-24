import tkinter as tk
from tkinter import messagebox

# Fungsi untuk memproses ekspresi matematika
def hitung():
    ekspresi = entry_input.get()
    try:
        # Menghapus spasi agar bisa memproses baik dengan atau tanpa spasi
        ekspresi_bersih = ekspresi.replace(" ", "")
        hasil = eval(ekspresi_bersih)  # Menggunakan eval() untuk menghitung ekspresi langsung
        label_hasil.config(text=f"Hasil: {hasil}")
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

# Membuat jendela utama
root = tk.Tk()
root.title("Kalkulator Hybrid")
root.geometry("400x250")
root.config(bg="#f0f0f0")

# Judul
judul = tk.Label(root, text="=== KALKULATOR HYBRID ===", font=("Arial", 14, "bold"), bg="#f0f0f0")
judul.pack(pady=10)

# Label dan Entry Input
label_input = tk.Label(root, text="Masukkan Ekspresi (contoh: 4+4-3 atau 5 - 3 * 4):", bg="#f0f0f0")
label_input.pack()

entry_input = tk.Entry(root, font=("Arial", 12), width=30)
entry_input.pack(pady=5)

# Tombol Hasilkan
btn_hitung = tk.Button(root, text="Hitung", font=("Arial", 12), bg="#4CAF50", fg="white", command=hitung)
btn_hitung.pack(pady=10)

# Label Hasil
label_hasil = tk.Label(root, text="Hasil: ", font=("Arial", 12, "bold"), bg="#f0f0f0")
label_hasil.pack(pady=10)

# Jalankan program
root.mainloop()
