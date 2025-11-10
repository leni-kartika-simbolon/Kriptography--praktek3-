import operator

# Daftar operator yang tersedia
ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

while True:
    print("\n=== PROGRAM PERHITUNGAN SEDERHANA ===")
    try:
        a = float(input("Masukkan nilai a: "))
        b = float(input("Masukkan nilai b: "))
        c = input("Masukkan operator (+, -, *, /): ")

        if c in ops:
            hasil = ops[c](a, b)
            print(f"Hasil dari {a} {c} {b} = {hasil}")
        else:
            print("Operator tidak valid. Gunakan hanya +, -, *, atau /.")

    except ValueError:
        print("Input tidak valid! Harap masukkan angka.")
    except ZeroDivisionError:
        print("Pembagian dengan nol tidak diperbolehkan.")

    # Tanya apakah ingin menghitung lagi
    ulang = input("\nApakah Anda ingin melakukan perhitungan lagi? (Y/T): ").lower()
    if ulang != 'y':
        print("\nProgram selesai. Terima kasih!")
        break