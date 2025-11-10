# === PROGRAM KALKULATOR SEDERHANA ===

print("=== PROGRAM KALKULATOR SEDERHANA ===")

# Input nilai dari pengguna
a = float(input("Ma12sukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
operator = input("Masukkan operator (+, -, *, /): ")

# Menggunakan struktur IF, ELIF, ELSE
if operator == '+':
    hasil = a + b
    print(f"Hasil dari {a} + {b} = {hasil}")
elif operator == '-':
    hasil = a - b
    print(f"Hasil dari {a} - {b} = {hasil}")
elif operator == '*':
    hasil = a * b
    print(f"Hasil dari {a} * {b} = {hasil}")
elif operator == '/':
    # Tambahkan pengecekan pembagian nol
    if b != 0:
        hasil = a / b
        print(f"Hasil dari {a} / {b} = {hasil}")
    else:
        print("Error: Pembagian dengan nol tidak diperbolehkan!")
else:
    print("Operator tidak valid! Gunakan salah satu dari +, -, *, atau /")

print("Program selesai. Terima kasih!")