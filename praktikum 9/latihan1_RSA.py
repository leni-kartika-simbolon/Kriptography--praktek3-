import math
#hanya ENKRISPI RSA
# --- Parameter Tetap ---
p = 17
q = 11
e = 7

def main():
    print("=== PROSES PERHITUNGAN RSA ===")
    print(f"p = {p}")
    print(f"q = {q}")
    print(f"e = {e}")
    print("-------------------------------------------")

    # 1. Hitung n = p * q
    n = p * q
    print(f"1. Nilai modulus n = p × q = {p} × {q} = {n}")

    # 2. Hitung fungsi Euler phi(n)
    phi = (p - 1) * (q - 1)
    print(f"2. Fungsi Euler φ(n) = (p - 1)(q - 1) = {p-1} × {q-1} = {phi}")

    # 3. Hitung eksponen privat d
    d = pow(e, -1, phi)
    print(f"3. Hitung eksponen privat d sehingga d·e ≡ 1 (mod φ(n))")
    print(f"   d = {d}   (karena {d} × {e} mod {phi} = 1)")

    print("-------------------------------------------")
    
    # Input plaintext
    plaintext = input("Masukkan plaintext (angka atau teks): ")

    # Jika plaintext berupa ANGKA
    if plaintext.isdigit():
        m = int(plaintext)
        print("\nPlaintext berupa ANGKA")
        print(f"m = {m}")

        # 4. Enkripsi
        print("\n4. Proses Enkripsi RSA")
        print(f"   Rumus: c = m^e mod n = {m}^{e} mod {n}")
        c = pow(m, e, n)
        print(f"   Hasil ciphertext = {c}")

    else:
        # plaintext berupa TEKS --> konversi ASCII
        print("\nPlaintext berupa TEKS")
        print(f"Teks: \"{plaintext}\"")

        print("\nKonversi ke ASCII:")
        ascii_list = []
        for ch in plaintext:
            code = ord(ch)
            ascii_list.append(code)
            print(f"   '{ch}' → {code}")

        print("\n4. Proses Enkripsi RSA per karakter:")
        cipher_list = []
        for code in ascii_list:
            print(f"   Enkripsi {code}: c = {code}^{e} mod {n}")
            cipher_val = pow(code, e, n)
            print(f"     → Cipher: {cipher_val}")
            cipher_list.append(cipher_val)

        print("\nHASIL ENKRIPSI AKHIR:")
        print(cipher_list)

    print("\n=== ENKRIPSI SELESAI ===")


if __name__ == "__main__":
    main()
