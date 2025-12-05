import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
import traceback

SBOX = [0x63,0x7c,0x77,0x7b,0xf2,0x6b,0x6f,0xc5,0x30,0x01,0x67,0x2b,0xfe,0xd7,0xab,0x76,0xca,0x82,0xc9,0x7d,0xfa,0x59,0x47,0xf0,0xad,0xd4,0xa2,0xaf,0x9c,0xa4,0x72,0xc0,0xb7,0xfd,0x93,0x26,0x36,0x3f,0xf7,0xcc,0x34,0xa5,0xe5,0xf1,0x71,0xd8,0x31,0x15,0x04,0xc7,0x23,0xc3,0x18,0x96,0x05,0x9a,0x07,0x12,0x80,0xe2,0xeb,0x27,0xb2,0x75,0x09,0x83,0x2c,0x1a,0x1b,0x6e,0x5a,0xa0,0x52,0x3b,0xd6,0xb3,0x29,0xe3,0x2f,0x84,0x53,0xd1,0x00,0xed,0x20,0xfc,0xb1,0x5b,0x6a,0xcb,0xbe,0x39,0x4a,0x4c,0x58,0xcf,0xd0,0xef,0xaa,0xfb,0x43,0x4d,0x33,0x85,0x45,0xf9,0x02,0x7f,0x50,0x3c,0x9f,0xa8,0x51,0xa3,0x40,0x8f,0x92,0x9d,0x38,0xf5,0xbc,0xb6,0xda,0x21,0x10,0xff,0xf3,0xd2,0xcd,0x0c,0x13,0xec,0x5f,0x97,0x44,0x17,0xc4,0xa7,0x7e,0x3d,0x64,0x5d,0x19,0x73,0x60,0x81,0x4f,0xdc,0x22,0x2a,0x90,0x88,0x46,0xee,0xb8,0x14,0xde,0x5e,0x0b,0xdb,0xe0,0x32,0x3a,0x0a,0x49,0x06,0x24,0x5c,0xc2,0xd3,0xac,0x62,0x91,0x95,0xe4,0x79,0xe7,0xc8,0x37,0x6d,0x8d,0xd5,0x4e,0xa9,0x6c,0x56,0xf4,0xea,0x65,0x7a,0xae,0x08,0xba,0x78,0x25,0x2e,0x1c,0xa6,0xb4,0xc6,0xe8,0xdd,0x74,0x1f,0x4b,0xbd,0x8b,0x8a,0x70,0x3e,0xb5,0x66,0x48,0x03,0xf6,0x0e,0x61,0x35,0x57,0xb9,0x86,0xc1,0x1d,0x9e,0xe1,0xf8,0x98,0x11,0x69,0xd9,0x8e,0x94,0x9b,0x1e,0x87,0xe9,0xce,0x55,0x28,0xdf,0x8c,0xa1,0x89,0x0d,0xbf,0xe6,0x42,0x68,0x41,0x99,0x2d,0x0f,0xb0,0x54,0xbb,0x16
]

INV_SBOX = [0x52,0x09,0x6a,0xd5,0x30,0x36,0xa5,0x38,0xbf,0x40,0xa3,0x9e,0x81,0xf3,0xd7,0xfb,0x7c,0xe3,0x39,0x82,0x9b,0x2f,0xff,0x87,0x34,0x8e,0x43,0x44,0xc4,0xde,0xe9,0xcb,0x54,0x7b,0x94,0x32,0xa6,0xc2,0x23,0x3d,0xee,0x4c,0x95,0x0b,0x42,0xfa,0xc3,0x4e,0x08,0x2e,0xa1,0x66,0x28,0xd9,0x24,0xb2,0x76,0x5b,0xa2,0x49,0x6d,0x8b,0xd1,0x25,0x72,0xf8,0xf6,0x64,0x86,0x68,0x98,0x16,0xd4,0xa4,0x5c,0xcc,0x5d,0x65,0xb6,0x92,0x6c,0x70,0x48,0x50,0xfd,0xed,0xb9,0xda,0x5e,0x15,0x46,0x57,0xa7,0x8d,0x9d,0x84,0x90,0xd8,0xab,0x00,0x8c,0xbc,0xd3,0x0a,0xf7,0xe4,0x58,0x05,0xb8,0xb3,0x45,0x06,0xd0,0x2c,0x1e,0x8f,0xca,0x3f,0x0f,0x02,0xc1,0xaf,0xbd,0x03,0x01,0x13,0x8a,0x6b,0x3a,0x91,0x11,0x41,0x4f,0x67,0xdc,0xea,0x97,0xf2,0xcf,0xce,0xf0,0xb4,0xe6,0x73,0x96,0xac,0x74,0x22,0xe7,0xad,0x35,0x85,0xe2,0xf9,0x37,0xe8,0x1c,0x75,0xdf,0x6e,0x47,0xf1,0x1a,0x71,0x1d,0x29,0xc5,0x89,0x6f,0xb7,0x62,0x0e,0xaa,0x18,0xbe,0x1b,0xfc,0x56,0x3e,0x4b,0xc6,0xd2,0x79,0x20,0x9a,0xdb,0xc0,0xfe,0x78,0xcd,0x5a,0xf4,0x1f,0xdd,0xa8,0x33,0x88,0x07,0xc7,0x31,0xb1,0x12,0x10,0x59,0x27,0x80,0xec,0x5f,0x60,0x51,0x7f,0xa9,0x19,0xb5,0x4a,0x0d,0x2d,0xe9,0x7a,0x9f,0x93,0xc9,0x9c,0xef,0xa0,0xe0,0x3b,0x4d,0xae,0x2a,0xf5,0xb0,0xc8,0xeb,0xbb,0x3c,0x83,0x53,0x99,0x61,0x17,0x2b,0x04,0x7e,0xba,0x77,0xd6,0x26,0xe1,0x69,0x14,0x63,0x55,0x21,0x0c,0x7d
]

RCON = [1, 2, 4, 8, 16, 32, 64, 128, 27, 54]

def pad_pkcs7(data): # Menerima list of integers/bytes
    pad_len = 16 - (len(data) % 16)
    return data + [pad_len] * pad_len

def unpad_pkcs7(data): # Menerima list of integers/bytes
    if not data: return data
    pad = data[-1]
    if pad < 1 or pad > 16: raise ValueError("Invalid PKCS#7 padding length.")
    if data[-pad:] != [pad]*pad: raise ValueError("Invalid PKCS#7 padding bytes.")
    return data[:-pad]

def bytes_to_matrix(b):
    """Mengubah 16-byte list menjadi State Matrix 4x4."""
    return [b[i:i+4] for i in range(0, 16, 4)]

def matrix_to_bytes(m):
    """Mengubah State Matrix 4x4 menjadi 16-byte list."""
    return [b for r in m for b in r]

# --- Round Operations ---
def add_round_key(s, k):
    """XOR State Matrix s (4x4) dengan Round Key k (4x4)."""
    return [[a ^ b for a, b in zip(x, y)] for x, y in zip(s, k)]

def sub_bytes(s):
    return [[SBOX[b] for b in row] for row in s]

def inv_sub_bytes(s):
    return [[INV_SBOX[b] for b in row] for row in s]

def shift_rows(s):
    return [
        s[0],
        s[1][1:] + s[1][:1],
        s[2][2:] + s[2][:2],
        s[3][3:] + s[3][:3],
    ]

def inv_shift_rows(s):
    return [
        s[0],
        s[1][-1:] + s[1][:-1],
        s[2][-2:] + s[2][:-2],
        s[3][-3:] + s[3][:-3],
    ]

# --- MixColumns Utilities ---
def xtime(a):
    return ((a << 1) ^ 0x1B) & 0xFF if a & 0x80 else (a << 1) & 0xFF

def mix_single_column(c):
    a = c
    b = [xtime(x) for x in a]
    return [
        b[0] ^ a[3] ^ a[2] ^ b[1] ^ a[1],
        b[1] ^ a[0] ^ a[3] ^ b[2] ^ a[2],
        b[2] ^ a[1] ^ a[0] ^ b[3] ^ a[3],
        b[3] ^ a[2] ^ a[1] ^ b[0] ^ a[0],
    ]

def mix_columns(s):
    cols = list(zip(*s))
    mixed = [mix_single_column(list(c)) for c in cols]
    return [list(col) for col in zip(*mixed)]

# --- InvMixColumns Utilities ---
def mul(a, b):
    r = 0
    for _ in range(8):
        if b & 1: r ^= a
        h = a & 0x80
        a = (a << 1) & 0xFF
        if h: a ^= 0x1B
        b >>= 1
    return r

def inv_mix_single_column(c):
    return [
        mul(c[0], 14) ^ mul(c[1], 11) ^ mul(c[2], 13) ^ mul(c[3], 9),
        mul(c[0], 9) ^ mul(c[1], 14) ^ mul(c[2], 11) ^ mul(c[3], 13),
        mul(c[0], 13) ^ mul(c[1], 9) ^ mul(c[2], 14) ^ mul(c[3], 11),
        mul(c[0], 11) ^ mul(c[1], 13) ^ mul(c[2], 9) ^ mul(c[3], 14),
    ]

def inv_mix_columns(s):
    cols = list(zip(*s))
    mixed = [inv_mix_single_column(list(c)) for c in cols]
    return [list(c) for c in zip(*mixed)]

# ================= 2. FUNGSI KEY EXPANSION (W0 s/d W43) =================
def key_expansion(key):
    """
    Menghasilkan 44 kata W (W0 sampai W43) dari 16-byte Cipher Key.
    Input: key (list 16 integer/byte)
    Output: list dari 44 kata (list of lists, setiap sub-list berisi 4 byte)
    """
    w = [key[i:i+4] for i in range(0, 16, 4)] # Membagi kunci awal menjadi 4 kata (w0, w1, w2, w3)
    
    # Loop untuk menghasilkan 40 kata tambahan (w4 sampai w43)
    for i in range(4, 44):
        t = w[i-1]
        if i % 4 == 0:
            # SubWord, RotWord, dan XOR RCon
            t = t[1:] + t[:1] # RotWord
            t = [SBOX[x] for x in t] # SubWord
            t[0] ^= RCON[(i//4)-1] # XOR RCon
        # XOR dengan w[i-4]
        w.append([t[j] ^ w[i-4][j] for j in range(4)])
        
    # Mengembalikan semua 44 kata W
    return w

# ================= 3. FUNGSI ENKRIPSI & DEKRIPSI (MENGGUNAKAN W) =================
def aes_encrypt_block(b, w_all):
    """
    Melakukan proses Enkripsi AES-128 pada satu blok (16 byte).
    Input: b (list 16 integer/byte blok Plaintext), w_all (list 44 kata W dari key_expansion)
    Output: list 16 integer/byte blok Ciphertext
    """
    s = bytes_to_matrix(b)
    
    # Round Key 0 (w0, w1, w2, w3)
    rk0 = w_all[0:4] # 4 kata pertama membentuk RK0
    s = add_round_key(s, rk0)
    
    # Rounds 1 sampai 9
    for r in range(1, 10):
        start_index = r * 4
        rk = w_all[start_index : start_index + 4] # Ambil 4 kata untuk Round Key r
        
        s = sub_bytes(s)
        s = shift_rows(s)
        s = mix_columns(s)
        s = add_round_key(s, rk)
        
    # Round 10: Final Round
    rk10 = w_all[40:44] # Ambil 4 kata terakhir (w40, w41, w42, w43)
    s = sub_bytes(s)
    s = shift_rows(s)
    s = add_round_key(s, rk10)
    
    return matrix_to_bytes(s)

def aes_decrypt_block(b, w_all):
    """
    Melakukan proses Dekripsi AES-128 pada satu blok (16 byte).
    Input: b (list 16 integer/byte blok Ciphertext), w_all (list 44 kata W dari key_expansion)
    Output: list 16 integer/byte blok Plaintext terdekripsi
    """
    s = bytes_to_matrix(b)
    
    # Round Key 10 (w40, w41, w42, w43)
    rk10 = w_all[40:44]
    s = add_round_key(s, rk10)
    
    # Rounds 9 Inverse sampai 1 Inverse
    for r_inv in range(9, 0, -1):
        start_index = r_inv * 4
        rk = w_all[start_index : start_index + 4] # Ambil 4 kata untuk Round Key r
        
        s = inv_shift_rows(s)
        s = inv_sub_bytes(s)
        s = add_round_key(s, rk)
        s = inv_mix_columns(s)
        
    # Round 0 Inverse: Final Decryption Round (w0, w1, w2, w3)
    rk0 = w_all[0:4]
    s = inv_shift_rows(s)
    s = inv_sub_bytes(s)
    s = add_round_key(s, rk0)
    
    return matrix_to_bytes(s)


# ================= UTILITIES UNTUK GUI =================
def fmt_hex_bytes(lst):
    return ' '.join(f"{b:02X}" for b in lst)

def fmt_decimal_bytes(lst):
    return ' '.join(str(b) for b in lst)

def bytes_from_ascii_no_space(s):
    # Mengonversi string ke list integer (desimal)
    if ' ' in s:
        raise ValueError("ASCII input tidak boleh mengandung spasi.")
    return [ord(c) for c in s]

def bytes_from_hex_spaced(s):
    # Mengonversi HEX spaced ke list integer (desimal)
    parts = s.strip().split()
    if not parts:
        return []
    try:
        return [int(p, 16) & 0xFF for p in parts]
    except Exception:
        raise ValueError("Gagal parse HEX. Pastikan format 'AA BB CC ...' (spasi antar byte).")

# ================= GUI & WIRING =================
class AESVerboseApp:
    def __init__(self, master):
        self.master = master
        master.title("AES-128 Verbose: ENKRIPSI & DEKRIPSI (LOGIKA INTISARI ANDA)")
        master.geometry("980x720")

        frm_top = tk.Frame(master)
        frm_top.pack(fill=tk.X, padx=8, pady=6)

        tk.Label(frm_top, text="Mode Input:").grid(row=0, column=0, sticky='w')
        self.mode_var = tk.StringVar(value="ASCII")
        tk.OptionMenu(frm_top, self.mode_var, "ASCII", "HEX").grid(row=0, column=1, sticky='w')

        tk.Label(frm_top, text="Plaintext (ASCII OR 16/32/.. byte HEX spaced):").grid(row=1, column=0, sticky='w')
        self.ent_pt = tk.Entry(frm_top, width=70)
        self.ent_pt.grid(row=1, column=1, columnspan=4, sticky='ew', padx=6)

        tk.Label(frm_top, text="Cipher Key (ASCII OR 16-byte HEX spaced):").grid(row=2, column=0, sticky='w')
        self.ent_key = tk.Entry(frm_top, width=70)
        self.ent_key.grid(row=2, column=1, columnspan=4, sticky='ew', padx=6)

        btns = tk.Frame(frm_top)
        btns.grid(row=3, column=0, columnspan=5, sticky='ew', pady=5)
        btns.columnconfigure(0, weight=1) 
        btns.columnconfigure(1, weight=1) 
        btns.columnconfigure(2, weight=1) 
        btns.columnconfigure(3, weight=1) 

        tk.Button(btns, text="PROSES ENKRIPSI & DEKRIPSI (Verbose)", command=self.action_dual_process, bg='lightgreen').grid(row=0, column=0, sticky='ew', padx=2)
        tk.Button(btns, text="Clear Output", command=self.clear_output).grid(row=0, column=1, sticky='ew', padx=2)
        tk.Button(btns, text="Save Output...", command=self.save_output).grid(row=0, column=2, sticky='ew', padx=2)
        tk.Button(btns, text="Copy Ciphertext (Hex)", command=self.copy_ciphertext).grid(row=0, column=3, sticky='ew', padx=2)

        self.txt = scrolledtext.ScrolledText(master, wrap=tk.WORD, font=("Courier", 10))
        self.txt.pack(fill=tk.BOTH, expand=True, padx=8, pady=6)

        self.last_cipher_hex = ""

    def print(self, line=""):
        self.txt.insert(tk.END, line + "\n")
        self.txt.see(tk.END)

    def clear_output(self):
        self.txt.delete('1.0', tk.END)
        self.last_cipher_hex = ""

    def save_output(self):
        data = self.txt.get('1.0', tk.END)
        if not data.strip():
            messagebox.showinfo("Save", "Tidak ada output untuk disimpan.")
            return
        path = filedialog.asksaveasfilename(defaultextension=".txt",
                                              filetypes=[("Text files","*.txt"), ("All files","*.*")])
        if path:
            with open(path, "w", encoding="utf-8") as f:
                f.write(data)
            messagebox.showinfo("Save", f"Output tersimpan di:\n{path}")

    def copy_ciphertext(self):
        if not self.last_cipher_hex:
            messagebox.showinfo("Copy", "Tidak ada ciphertext untuk disalin. Jalankan proses dulu.")
            return
        self.master.clipboard_clear()
        self.master.clipboard_append(self.last_cipher_hex)
        messagebox.showinfo("Copy", "Ciphertext (hex) disalin ke clipboard.")

    def parse_inputs(self):
        mode = self.mode_var.get()
        pt_raw = self.ent_pt.get().strip()
        key_raw = self.ent_key.get().strip()
        if not pt_raw or not key_raw:
            raise ValueError("Masukkan Plaintext dan Cipher Key.")

        if mode == "ASCII":
            # Plaintext
            pt_bytes = bytes_from_ascii_no_space(pt_raw)
            pt_bytes = pad_pkcs7(pt_bytes) # PADDING DILAKUKAN PADA LIST INTEGER
            
            # Key
            key_bytes = bytes_from_ascii_no_space(key_raw)
            key_bytes = (key_bytes + [0] * 16)[:16]
        else:  # HEX
            # Plaintext
            pt_bytes = bytes_from_hex_spaced(pt_raw)
            if len(pt_bytes) % 16 != 0:
                raise ValueError("Plaintext HEX harus kelipatan 16 byte (16,32,...).")
                
            # Key
            key_bytes = bytes_from_hex_spaced(key_raw)
            if len(key_bytes) != 16:
                raise ValueError("Key HEX harus 16 byte.")
        
        return pt_bytes, key_bytes

    def action_dual_process(self):
        self.txt.delete('1.0', tk.END)
        self.last_cipher_hex = ""
        
        try:
            # --- PHASE 1: PARSING AND KEY EXPANSION ---
            input_pt_bytes, key_bytes = self.parse_inputs()
            
            self.print("==================================================")
            self.print("        AES-128 DUAL PROCESS (ENKRIPSI -> DEKRIPSI)        ")
            self.print("==================================================")
            self.print(f"Input Mode: {self.mode_var.get()}")
            self.print(f"Key (Hex): {fmt_hex_bytes(key_bytes)}")
            self.print(f"Plaintext Input (Padded Hex for Enc): {fmt_hex_bytes(input_pt_bytes)}")
            
            # Key expansion (menghasilkan 44 kata W)
            w_all = key_expansion(key_bytes)
            
            # =================================================================
            # MODIFIKASI: Menghapus Tampilan Key Expansion (W0 s/d W43/Round Keys)
            # Bagian kode yang dihapus/dibuat komentar ada di sini:
            #
            # self.print("\n\n################ KEY EXPANSION (W0 s/d W43) ################")
            # for i, w_word in enumerate(w_all):
            #     if i % 4 == 0:
            #         rk_index = i // 4
            #         if rk_index < 11:
            #             rk_bytes = matrix_to_bytes(w_all[i:i+4])
            #             self.print(f"Round Key {rk_index:02d} (W{i:02d}-W{i+3:02d}): " + fmt_hex_bytes(rk_bytes))
            #         else:
            #             break
            # 
            # =================================================================
            
            # --- PHASE 2: ENKRIPSI (VERBOSE STEP-BY-STEP) ---
            self.print("\n\n" + "="*80)
            self.print("################ START AES ENKRIPSI PROCESS ################")
            self.print("="*80)
            
            cipher_all = []
            
            # Encrypting block by block (Verbose)
            for blk_idx in range(0, len(input_pt_bytes), 16):
                block = input_pt_bytes[blk_idx:blk_idx+16]
                self.print(f"\n\n======== Encrypting Block index {blk_idx//16} (Input: {fmt_hex_bytes(block)}) ========")
                
                s = bytes_to_matrix(block)
                
                # Round 0: Initial AddRoundKey (RK0 = W0-W3)
                rk0 = w_all[0:4]
                s = add_round_key(s, rk0)
                self.print("\n[R0] After AddRoundKey: \n" + '\n'.join([fmt_hex_bytes(r) for r in s]))

                # Rounds 1 to 9 
                for r in range(1, 10):
                    self.print(f"\n--- Round {r} ---")
                    rk = w_all[r*4 : r*4 + 4] # RKr = W(4r) - W(4r+3)
                    
                    s = sub_bytes(s)
                    self.print("After SubBytes: \n" + '\n'.join([fmt_hex_bytes(r) for r in s]))
                    s = shift_rows(s)
                    self.print("After ShiftRows: \n" + '\n'.join([fmt_hex_bytes(r) for r in s]))
                    s = mix_columns(s) 
                    self.print("After MixColumns: \n" + '\n'.join([fmt_hex_bytes(r) for r in s]))
                    s = add_round_key(s, rk)
                    self.print(f"After AddRoundKey (R{r}): \n" + '\n'.join([fmt_hex_bytes(r) for r in s]))

                # Round 10 (Final)
                self.print("\n--- Round 10 (Final) ---")
                rk10 = w_all[40:44] # RK10 = W40-W43
                
                s = sub_bytes(s)
                self.print("After SubBytes: \n" + '\n'.join([fmt_hex_bytes(r) for r in s]))
                s = shift_rows(s)
                self.print("After ShiftRows: \n" + '\n'.join([fmt_hex_bytes(r) for r in s]))
                s = add_round_key(s, rk10)
                self.print("After AddRoundKey (Ciphertext): \n" + '\n'.join([fmt_hex_bytes(r) for r in s]))
                
                cblock = matrix_to_bytes(s)
                self.print("\nBlock Ciphertext (Hex): " + fmt_hex_bytes(cblock))
                cipher_all.extend(cblock)


            final_ciphertext_bytes = cipher_all
            
            # --- MENAMPILKAN CIPHERTEXT AKHIR DALAM 3 FORMAT ---
            self.print("\n\n=== HASIL AKHIR CIPHERTEXT ===")
            
            hex_output = fmt_hex_bytes(final_ciphertext_bytes)
            self.print("**1. HEXA** : " + hex_output)
            self.last_cipher_hex = hex_output
            
            self.print("**2. DESIMAL** : " + fmt_decimal_bytes(final_ciphertext_bytes))
            
            try:
                # Konversi langsung dari byte (list integer) ke string Latin-1/ASCII
                ascii_output = "".join([chr(b) for b in final_ciphertext_bytes])
                printable_ascii = ''.join([c if (32 <= ord(c) <= 126) else f'[{ord(c)}]' for c in ascii_output])
                self.print("**3. ASCII** : " + printable_ascii)
            except Exception:
                self.print("3. ASCII     : [Gagal konversi ke ASCII/Latin-1]")
            
            
            # --- PHASE 3: DEKRIPSI (VERBOSE STEP-BY-STEP) ---
            self.print("\n\n" + "="*80)
            self.print("################ START AES DEKRIPSI PROCESS ################")
            self.print(f"Input Ciphertext for Decryption (Hex): {self.last_cipher_hex}")
            self.print("="*80)
            
            plain_all = []
            
            # Decrypting block by block (Verbose)
            for blk_idx in range(0, len(final_ciphertext_bytes), 16):
                block = final_ciphertext_bytes[blk_idx:blk_idx+16]
                self.print(f"\n\n======== Decrypting Block index {blk_idx//16} (Input: {fmt_hex_bytes(block)}) ========")
                
                s = bytes_to_matrix(block)
                
                # Round 10 Invers: Initial AddRoundKey (RK10 = W40-W43)
                rk10 = w_all[40:44]
                s = add_round_key(s, rk10)
                self.print("\n[R10 Inv] After AddRoundKey: \n" + '\n'.join([fmt_hex_bytes(r) for r in s]))

                # Rounds 9 to 1 Invers
                for r_inv in range(9, 0, -1):
                    self.print(f"\n--- Inv Round {r_inv} ---")
                    rk = w_all[r_inv*4 : r_inv*4 + 4] # RKr = W(4r) - W(4r+3)
                    
                    s = inv_shift_rows(s)
                    self.print("After InvShiftRows: \n" + '\n'.join([fmt_hex_bytes(r) for r in s]))
                    s = inv_sub_bytes(s)
                    self.print("After InvSubBytes: \n" + '\n'.join([fmt_hex_bytes(r) for r in s]))
                    s = add_round_key(s, rk)
                    self.print(f"After AddRoundKey (R{r_inv}): \n" + '\n'.join([fmt_hex_bytes(r) for r in s]))
                    s = inv_mix_columns(s)
                    self.print("After InvMixColumns: \n" + '\n'.join([fmt_hex_bytes(r) for r in s]))

                # Round 0 Invers (Final Decryption)
                self.print("\n--- Inv Round 0 (Final Decryption) ---")
                rk0 = w_all[0:4] # RK0 = W0-W3
                
                s = inv_shift_rows(s)
                self.print("After InvShiftRows: \n" + '\n'.join([fmt_hex_bytes(r) for r in s]))
                s = inv_sub_bytes(s)
                self.print("After InvSubBytes: \n" + '\n'.join([fmt_hex_bytes(r) for r in s]))
                s = add_round_key(s, rk0)
                self.print("After AddRoundKey (Plaintext): \n" + '\n'.join([fmt_hex_bytes(r) for r in s]))
                
                pblock = matrix_to_bytes(s)
                self.print("\nBlock Decrypted Bytes (Hex): " + fmt_hex_bytes(pblock))
                plain_all.extend(pblock)

            # Final Decryption Result
            self.print("\n\n=== HASIL AKHIR DEKRIPSI ===")
            decrypted_bytes = plain_all
            self.print("PLAIN BYTES (HEX, sebelum unpad): " + fmt_hex_bytes(decrypted_bytes))

            if self.mode_var.get() == "ASCII":
                try:
                    unp = unpad_pkcs7(decrypted_bytes)
                    text_output = "".join([chr(b) for b in unp])
                    
                    self.print(f"PLAIN BYTES (HEX, setelah unpad): {fmt_hex_bytes(unp)}")
                    self.print("================================================")
                    self.print("**PLAINTEXT (HASIL DEKRIPSI AKHIR - TEKS ASCII):**")
                    self.print(text_output)
                    self.print("================================================")
                except ValueError as ve:
                    self.print(f"[WARNING] Gagal unpad PKCS7: {str(ve)}. Menampilkan data raw.")
                except Exception as e:
                    self.print(f"[WARNING] Gagal konversi ke teks: {str(e)}. Menampilkan data raw.")
            else:
                self.print("Mode HEX dipilih, tidak ada konversi ke teks ASCII atau unpad.")

        except ValueError as ve:
            messagebox.showerror("Input Error", str(ve))
            self.print("\n[ERROR] " + str(ve))
        except Exception as e:
            messagebox.showerror("Process Error", f"Terjadi kesalahan saat pemrosesan:\n{str(e)}")
            self.print(f"\n[ERROR] Terjadi kesalahan saat pemrosesan: " + str(e))
            self.print(traceback.format_exc())


# -----------------------
# Run app
# -----------------------
if __name__ == "__main__":
    try:
        root = tk.Tk()
    except Exception as e:
        print("Failed to open Tkinter GUI. Make sure you run this on a local machine with display.")
        raise
    app = AESVerboseApp(root)
    root.mainloop()