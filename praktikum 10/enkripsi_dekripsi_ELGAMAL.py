import math

def cek_prima(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

print("="*60)
print(f"{'IMPLEMENTASI KRIPTOGRAFI ELGAMAL':^60}")
print("="*60)

# --- INPUT ---
teks_asli = input("1. Masukkan Plainteks  : ").upper()

while True:
    p = int(input("2. Masukkan p (Prima)  : "))
    if cek_prima(p): break
    print("   >> Error: p harus bilangan prima!")

while True:
    g = int(input(f"3. Masukkan g (g < {p})  : "))
    if g < p: break
    print(f"   >> Error: g harus < {p}!")

while True:
    x = int(input(f"4. Masukkan x (1-{(p-2)}): "))
    if 1 <= x <= (p-2): break
    print(f"   >> Error: x harus 1 s/d {(p-2)}!")

y = pow(g, x, p)
print(f"5. Hitung y = {g}^{x} mod {p} = {y}")

# --- PERSIAPAN PESAN ---
print("\n" + "="*50)
print(f"{'PROSES PERSIAPAN PESAN (TABEL)':^50}")
print("="*50)
print(f"{'Char':<8} | {'ASCII':<10} | {'m = ASCII mod p':<15}")
print("-" * 50)

list_m = []
for char in teks_asli:
    ascii_val = ord(char)
    m = ascii_val % p
    list_m.append(m)
    print(f"{char:<8} | {ascii_val:<10} | {m:<15}")
print("-" * 50)

# --- ENKRIPSI ---
print("\n" + "="*65)
print(f"{'1. PROSES ENKRIPSI':^65}")
print("="*65)

k = int(input(f"Masukkan nilai k (1-{(p-2)}): "))
a = pow(g, k, p)
y_k = pow(y, k, p)

print(f"\nNilai a = {g}^{k} mod {p} = {a}")

header_enkripsi = f"{'m':<6} | {'Rumus b = (y^k * m) mod p':<35} | {'Hasil (a, b)'}"
print("-" * len(header_enkripsi))
print(header_enkripsi)
print("-" * len(header_enkripsi))

ciphertexts = []
for m in list_m:
    b = (y_k * m) % p
    ciphertexts.append((a, b))
    rumus_b = f"({y}^{k} * {m}) mod {p}"
    print(f"{m:<6} | {rumus_b:<35} | ({a}, {b})")
print("-" * len(header_enkripsi))

# --- DEKRIPSI ---
print("\n" + "="*95)
print(f"{'2. PROSES DEKRIPSI':^95}")
print("="*95)

ax_inv = pow(a, (p - 1 - x), p)
print(f"Nilai Invers (a^x)^-1 mod p = {a}^({p}-1-{x}) mod {p} = {ax_inv}\n")

header_dekripsi = (
    f"{'b':<6} | "
    f"{'Rumus m = (b * Invers) mod p':<30} | "
    f"{'m':<5} | "
    f"{'(m + div*p)':<20} | "
    f"{'ASCII':<7} | "
    f"{'Char'}"
)

print("-" * len(header_dekripsi))
print(header_dekripsi)
print("-" * len(header_dekripsi))

hasil_teks_akhir = ""

for i, (a_val, b_val) in enumerate(ciphertexts):
    # hasil m dari ElGamal
    m_hasil = (b_val * ax_inv) % p

    # ambil ASCII asli (untuk simulasi proses div)
    ascii_asli = ord(teks_asli[i])
    div = ascii_asli // p

    # rekonstruksi ASCII
    ascii_hasil = m_hasil + (div * p)
    proses_ascii = f"{m_hasil} + {div}*{p}"

    char_hasil = chr(ascii_hasil)
    hasil_teks_akhir += char_hasil

    rumus_m = f"({b_val} * {ax_inv}) mod {p}"

    print(
        f"{b_val:<6} | "
        f"{rumus_m:<30} | "
        f"{m_hasil:<5} | "
        f"{proses_ascii:<20} | "
        f"{ascii_hasil:<7} | "
        f"{char_hasil}"
    )

print("-" * len(header_dekripsi))

print("\n" + "╔" + "═"*45 + "╗")
print(f"║ HASIL AKHIR DEKRIPSI: {hasil_teks_akhir:<22} ║")
print("╚" + "═"*45 + "╝")
