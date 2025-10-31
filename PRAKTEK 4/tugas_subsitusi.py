def subsitusi_cipher(plaintext, aturan):
    ciphertext = ''
    for char in plaintext:
        if char in aturan:
            ciphertext += aturan[char]
        else:
            ciphertext += char
    return ciphertext

# menginput plaintext
plaintext = input("Masukkan plaintext: ").upper()
print("Masukkan aturan substitusi (contoh: A=B).")
print("Ketik 'selesai' jika semua aturan sudah dimasukkan.\n")

aturan_subsitusi = {}
while True:
    aturan_input = input("Masukkan aturan (huruf_asli=huruf_baru): ").upper()
    if aturan_input == "SELESAI":
        break
    if "=" in aturan_input:
        huruf_asli, huruf_baru = aturan_input.split("=")
        aturan_subsitusi[huruf_asli.strip()] = huruf_baru.strip()
    else:
        print("Format salah! Gunakan format seperti A=B")
ciphertext = subsitusi_cipher(plaintext, aturan_subsitusi)

# menampilkan hasil
print("\n=== HASIL SUBSTITUSI CIPHER ===")
print(f"Plaintext: {plaintext}")
print(f"Aturan substitusi: {aturan_subsitusi}")
print(f"Ciphertext: {ciphertext}")
