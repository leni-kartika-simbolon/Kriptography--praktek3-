import random
import math

# fungsi 

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def random_prime(min_val=50, max_val=200):
    primes = [x for x in range(min_val, max_val + 1) if is_prime(x)]
    return random.choice(primes)

def random_e(phi_n):
    while True:
        e = random.randint(50, 200) # e dibatasi dengan bil.prima antara 50–200
        if is_prime(e) and math.gcd(e, phi_n) == 1:
            return e

# RSA core

def rsa_keygen():
    p = random_prime()
    q = random_prime()

    while p == q:
        q = random_prime()

    n = p * q
    phi_n = (p - 1) * (q - 1)

    e = random_e(phi_n)

    d = pow(e, -1, phi_n)  # invers modular

    return p, q, n, phi_n, e, d

def rsa_encrypt_number(m, e, n):
    return pow(m, e, n)

def rsa_decrypt_number(c, d, n):
    return pow(c, d, n)

def text_to_numbers(text):
    return [ord(ch) for ch in text]

def numbers_to_text(nums):
    return ''.join(chr(n) for n in nums)

# program utamanya

def main():
    print("===== GENERATE KUNCI RSA (p, q, e acak (bil.prima 50-200)) =====")

    p, q, n, phi_n, e, d = rsa_keygen()

    print(f"1. Bilangan prima p  = {p}")
    print(f"2. Bilangan prima q  = {q}")
    print(f"3. Nilai modulus n   = p × q = {n}")
    print(f"4. Fungsi Euler φ(n) = (p-1)(q-1) = {phi_n}")
    print(f"5. Eksponen publik e (prime/bil.prima 50–200 & coprime/saling_prima φ(n)) = {e}")
    print(f"6. Eksponen privat d = invers e mod φ(n) = {d}")

    print("\n===== INPUT PLAINTEXT =====")
    plaintext = input("Masukkan plaintext (angka atau teks): ")

    # untuk plainteks angka
    if plaintext.isdigit():
        m = int(plaintext)
        print("\n--- MODE ANGKA ---")
        print(f"Plaintext M = {m}")

        c = rsa_encrypt_number(m, e, n)
        print(f"\n7. Proses Enkripsi: c = m^e mod n")
        print(f"   c = {m}^{e} mod {n} = {c}")

        m_decrypted = rsa_decrypt_number(c, d, n)
        print(f"\n8. Proses Dekripsi: m = c^d mod n")
        print(f"   m = {c}^{d} mod {n} = {m_decrypted}")

        print("\n===== HASIL AKHIR =====")
        print(f"Ciphertext : {c}")
        print(f"Plaintext kembali : {m_decrypted}")

    # untuk plainteks huruf/teks
    else:
        print("\n--- MODE TEKS ---")
        text_nums = text_to_numbers(plaintext)
        print(f"Konversi plaintext ke ASCII: {text_nums}")

        ciphertext = []
        print("\n7. Proses Enkripsi per karakter:")
        for num in text_nums:
            c = rsa_encrypt_number(num, e, n)
            ciphertext.append(c)
            print(f"  {num}^{e} mod {n} = {c}")

        print(f"\nCiphertext (blok): {ciphertext}")

        print("\n8. Proses Dekripsi per blok:")
        decrypted_nums = []
        for c in ciphertext:
            m = rsa_decrypt_number(c, d, n)
            decrypted_nums.append(m)
            print(f"  {c}^{d} mod {n} = {m}")

        decrypted_text = numbers_to_text(decrypted_nums)

        print("\n===== HASIL AKHIR =====")
        print(f"Ciphertext blok : {ciphertext}")
        print(f"Plaintext kembali : {decrypted_text}")


main()
