import itertools

def atur_buku(buku, r):
    hasil = []
    rak_labels = [f"Rak{i+1}" for i in range(r)]

    # Buat semua kombinasi penempatan buku ke rak
    for penempatan in itertools.product(rak_labels, repeat=len(buku)):
        rak = {rak_label: [] for rak_label in rak_labels}
        for i, rak_ke in enumerate(penempatan):
            rak[rak_ke].append(buku[i])
        hasil.append(rak)
    return hasil

# === Program utama ===
n = int(input("Masukkan jumlah buku: "))
r = int(input("Masukkan jumlah rak: "))

buku = [f"Buku{i+1}" for i in range(n)]

hasil = atur_buku(buku, r)

print(f"\nTerdapat {len(hasil)} cara penempatan buku ke rak.\n")
for i, h in enumerate(hasil[:10], start=1):  # tampilkan 10 contoh
    print(f"Cara {i}: {h}")
