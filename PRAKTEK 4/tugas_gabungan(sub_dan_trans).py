def subsitusi_cipher(plaintext, aturan):
    ciphertext = ''
    for char in plaintext:
        if char in aturan:
            ciphertext += aturan[char]
        else:
            ciphertext += char
    return ciphertext


def transposisi_cipher(plaintext):
    plaintext = plaintext.replace(" ", "")  # hapus spasi agar rapi
    key = 4  # jumlah kolom
    parts = [plaintext[i:i + key] for i in range(0, len(plaintext), key)]
    ciphertext = ""
    for col in range(key):
        for part in parts:
            if col < len(part):
                ciphertext += part[col]
        ciphertext += ""  # tidak menambah spasi antar kolom
    return ciphertext


# === Program utama ===
aturan_subsitusi = {
    'U': 'K',
    'N': 'X',
    'I': 'I',
    'K': 'R',
    'A': 'B',
    'S': 'V',
    'T': 'T',
    'O': 'O',
    'H': 'Z',
    'M': 'Y'
}

plaintext = input("Masukkan plaintext: ").upper()

# Proses 1: Substitusi
cipher_sub = subsitusi_cipher(plaintext, aturan_subsitusi)

# Proses 2: Transposisi (menggunakan hasil substitusi)
cipher_trans = transposisi_cipher(cipher_sub)

# Tampilkan hasil akhir
print("\n=== HASIL ENKRIPSI ===")
print(f"Input Plaintext                 : {plaintext}")
print(f"Ciphertext (Substitusi Cipher)  : {cipher_sub}")
print(f"Ciphertext (Substitusi + Transposisi Cipher) : {cipher_trans}")
