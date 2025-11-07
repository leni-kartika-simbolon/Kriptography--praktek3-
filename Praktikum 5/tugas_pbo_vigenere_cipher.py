# Program: Implementasi Vigenere Cipher dengan PBO
class VigenereCipher:
    def __init__(self, kunci):     
           
        # ini untuk Inisialisasi objek dengan kunci (akan disimpan dalam huruf besar)
        self.kunci = kunci.upper()

#ENKRIPSI
    def enkripsi(self, teks):
        teks = teks.upper()
        hasil = ""
        kunci_index = 0
        proses = []

        print("\n=== PROSES ENKRIPSI ===")
        for huruf in teks:
            if huruf.isalpha():
                p = ord(huruf) - 65
                k = ord(self.kunci[kunci_index]) - 65
                c = (p + k) % 26
                hasil_huruf = chr(c + 65)
                hasil += hasil_huruf

                detail = f"{huruf} ({p}) + {self.kunci[kunci_index]} ({k}) = {hasil_huruf} ({c})"
                proses.append(detail)
                print(detail)

                kunci_index = (kunci_index + 1) % len(self.kunci)
            else:
                hasil += huruf
                proses.append(f"{huruf} (non-huruf, tidak berubah)")
                print(f"{huruf} (non-huruf, tidak berubah)")

        return hasil, proses

#DEKRIPSI
    def dekripsi(self, teks):
        teks = teks.upper()
        hasil = ""
        kunci_index = 0
        proses = []

        print("\n=== PROSES DEKRIPSI ===")
        for huruf in teks:
            if huruf.isalpha():
                c = ord(huruf) - 65
                k = ord(self.kunci[kunci_index]) - 65
                p = (c - k + 26) % 26
                hasil_huruf = chr(p + 65)
                hasil += hasil_huruf

                detail = f"{huruf} ({c}) - {self.kunci[kunci_index]} ({k}) = {hasil_huruf} ({p})"
                proses.append(detail)
                print(detail)

                kunci_index = (kunci_index + 1) % len(self.kunci)
            else:
                hasil += huruf
                proses.append(f"{huruf} (non-huruf, tidak berubah)")
                print(f"{huruf} (non-huruf, tidak berubah)")

        return hasil, proses


class ProgramVigenere:  
    def __init__(self):
        # iniuntuk menampilkan menu utama saat program pertama kali dijalankan
        print("===============================================")
        print("PROGRAM VIGENÈRE CIPHER DENGAN DETAIL PROSES (PBO)")
        print("===============================================")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Keluar")
        print("===============================================")

#ini untuk menjalankan menu interaktif program
    def jalankan(self):

    #MENJALANKAN MENU UTAMA
        while True:
            pilihan = input("Pilih menu (1/2/3): ").strip()

            if pilihan == "1":
                teks = input("\nMasukkan teks yang ingin dienkripsi: ")
                kunci = input("Masukkan kunci                     : ")
                cipher = VigenereCipher(kunci)
                hasil, _ = cipher.enkripsi(teks)
                print("\n-----------------------------------------------")
                print("🔸 Hasil Enkripsi:", hasil)
                print("-----------------------------------------------\n")

            elif pilihan == "2":
                teks = input("\nMasukkan teks yang ingin dienkripsi: ")
                kunci = input("Masukkan kunci                     : ")
                cipher = VigenereCipher(kunci)
                hasil, _ = cipher.dekripsi(teks)
                print("\n-----------------------------------------------")
                print("🔹 Hasil Dekripsi:", hasil)
                print("-----------------------------------------------\n")

            elif pilihan == "3":
                print("Terima kasih telah menggunakan program ini! 👋")
                break

            else:
                print("Pilihan tidak valid, silakan coba lagi.")
            print("===============================================\n")


#JALANKAN PROGRAM
if __name__ == "__main__":
    program = ProgramVigenere()
    program.jalankan()
