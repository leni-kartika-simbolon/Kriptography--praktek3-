import itertools

def permutasi_sebagian(arr, k):
    return list(itertools.permutations(arr, k))

def permutasi_menyeluruh(arr):
    return list(itertools.permutations(arr))

def permutasi_keliling(arr):
    if len(arr) == 1:
        return [arr]
    pertama = arr[0]
    permutasi_penuh = list(itertools.permutations(arr[1:]))
    return [[pertama] + list(perm) for perm in permutasi_penuh]

def permutasi_berkelompok(grup):
    hasil = [[]]
    for kelompok in grup:
        hasil_baru = []
        for hsl in hasil:
            for perm in itertools.permutations(kelompok):
                hasil_baru.append(hsl + list(perm))
        hasil = hasil_baru
    return hasil


# === Program Utama ===
print("=== PROGRAM PERMUTASI ===")
print("1. Permutasi Sebagian")
print("2. Permutasi Menyeluruh")
print("3. Permutasi Keliling")
print("4. Permutasi Berkelompok")

pilih = int(input("Pilih jenis permutasi (1-4): "))

if pilih == 1:
    data = input("Masukkan elemen (pisahkan dengan spasi): ").split()
    k = int(input("Masukkan panjang permutasi (k): "))
    print(permutasi_sebagian(data, k))

elif pilih == 2:
    data = input("Masukkan elemen (pisahkan dengan spasi): ").split()
    print(permutasi_menyeluruh(data))

elif pilih == 3:
    data = input("Masukkan elemen (pisahkan dengan spasi): ").split()
    print(permutasi_keliling(data))

elif pilih == 4:
    n = int(input("Berapa jumlah grup? "))
    grup = []
    for i in range(n):
        g = input(f"Masukkan elemen grup {i+1} (pisahkan dengan spasi): ").split()
        grup.append(g)
    print(permutasi_berkelompok(grup))

else:
    print("Pilihan tidak valid.")
