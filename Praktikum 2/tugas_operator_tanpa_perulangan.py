# Program Kalkulator Sederhana

print("=== PROGRAM KALKULATOR SEDERHANA ===")

# Input nilai dari pengguna
a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
operator = input("Masukkan operator (+, -, *, /): ")

# Proses perhitungan berdasarkan operator
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
    if b != 0:
        hasil = a / b
        print(f"Hasil dari {a} / {b} = {hasil}")
    else:
        print("Error: Pembagian dengan nol tidak diperbolehkan!")
else:
    print("Operator tidak valid! Gunakan salah satu dari +, -, *, /")

print("Program selesai. Terima kasih!")