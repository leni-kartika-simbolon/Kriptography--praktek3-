#enkripsi_DES
import tkinter as tk
from tkinter import scrolledtext, messagebox

PC1 = [
    57,49,41,33,25,17,9,
    1,58,50,42,34,26,18,
    10,2,59,51,43,35,27,
    19,11,3,60,52,44,36,
    63,55,47,39,31,23,15,
    7,62,54,46,38,30,32, # (DIPERBAIKI) awalnya 22 menjadi 32
    14,6,61,53,45,37,29,
    21,13,5,28,20,12,4
]

PC2 = [
    14,17,11,24,1,5,
    3,28,15,6,21,10,
    23,19,12,4,26,8,
    16,7,27,20,13,2,
    41,52,31,37,47,55,
    30,40,51,45,33,48,
    44,49,39,56,34,53,
    46,42,50,36,29,32
]

E = [
    32,1,2,3,4,5,
    4,5,6,7,8,9,
    8,9,10,11,12,13,
    12,13,14,15,16,17,
    16,17,18,19,20,21,
    20,21,22,23,24,25,
    24,25,26,27,28,29,
    28,29,30,31,32,1
]

P = [
    16,7,20,21,29,12,28,17,
    1,15,23,26,5,18,31,10,
    2,8,24,14,32,27,3,9,
    19,13,30,6,22,11,4,25
]

IP = [
    58,50,42,34,26,18,10,2,
    60,52,44,36,28,20,12,4,
    62,54,46,38,30,22,14,6,
    64,56,48,40,32,24,16,8,
    57,49,41,33,25,17,9,1,
    59,51,43,35,27,19,11,3,
    61,53,45,37,29,21,13,5,
    63,55,47,39,31,23,15,7
]

IP_INV = [
    40,8,48,16,56,24,64,32,
    39,7,47,15,55,23,63,31,
    38,6,46,14,54,22,62,30,
    37,5,45,13,53,21,61,29,
    36,4,44,12,52,20,60,28,
    35,3,43,11,51,19,59,27,
    34,2,42,10,50,18,58,26,
    33,1,41,9,49,17,57,25
]

SBOX = [
    [
      [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
      [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
      [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
      [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
    ],
    [
      [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
      [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
      [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
      [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]
    ],
    [
      [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
      [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
      [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
      [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]
    ],
    [
      [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
      [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
      [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
      [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]
    ],
    [
      [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
      [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
      [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
      [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]
    ],
    [
      [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
      [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
      [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
      [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]
    ],
    [
      [4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
      [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
      [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
      [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]
    ],
    [
      [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
      [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
      [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
      [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]
    ]
]

ROTATIONS = [1, 1, 2, 2, 2, 2, 2, 2,
             1, 2, 2, 2, 2, 2, 2, 1]

# fungsi
def str_to_bin(text):
    return ''.join(f"{ord(c):08b}" for c in text)

def permute(block, table):
    return ''.join(block[i-1] for i in table)

def left_rotate(bits, n):
    return bits[n:] + bits[:n]

def xor(a, b):
    return ''.join('1' if i != j else '0' for i, j in zip(a, b))

def sbox_substitution(bits):
    output = ""
    for i in range(8):
        block = bits[i*6:(i+1)*6]
        row = int(block[0] + block[5], 2)
        col = int(block[1:5], 2)
        val = SBOX[i][row][col]
        output += f"{val:04b}"
    return output

def pad64(bitstring):
    pad_len = 64 - (len(bitstring) % 64)
    if pad_len == 64:
        return bitstring
    return bitstring + ("0" * pad_len)


#enkripsi_DES
def generate_keys(key):
    key_bin = str_to_bin(key)
    key_bin = key_bin[:64].ljust(64, "0")
    
    perm_key = permute(key_bin, PC1)
    C = perm_key[:28]
    D = perm_key[28:]

    keys = []
    for r in ROTATIONS:
        C = left_rotate(C, r)
        D = left_rotate(D, r)
        subkey = permute(C + D, PC2)
        keys.append(subkey)

    return keys

def feistel(R, K):
    expanded = permute(R, E)
    xored = xor(expanded, K)
    sbox_out = sbox_substitution(xored)
    return permute(sbox_out, P)

def des_encrypt(plaintext, key):
    bit_plain = str_to_bin(plaintext)
    bit_plain = pad64(bit_plain)

    keys = generate_keys(key)

    block = bit_plain[:64]
    block = permute(block, IP)

    L = block[:32]
    R = block[32:]

    for i in range(16):
        new_L = R
        new_R = xor(L, feistel(R, keys[i]))
        L, R = new_L, new_R

    final = permute(R + L, IP_INV)
    return final, keys


#TKINTER GUI 

def encrypt_gui():
    plaintext = entry_plain.get()
    key = entry_key.get()

    if len(key) > 8:
        messagebox.showerror("Error", "Key harus maksimal 8 karakter!")
        return
    
    cipher_bin, subkeys = des_encrypt(plaintext, key)

    # Tampilkan Subkeys
    text_subkeys.delete("1.0", tk.END)
    for i, k in enumerate(subkeys):
        text_subkeys.insert(tk.END, f"K{i+1}: {k}\n")

    # Cipher outputs
    text_cipher.delete("1.0", tk.END)
    text_cipher.insert(tk.END, f"Ciphertext (Binary):\n{cipher_bin}\n\n")
    text_cipher.insert(tk.END, f"Ciphertext (Hex):\n{hex(int(cipher_bin, 2))[2:].upper()}")


# gui layout
root = tk.Tk()
root.title("DES Encryption - Tkinter GUI")

tk.Label(root, text="Plaintext:").grid(row=0, column=0, sticky="w")
entry_plain = tk.Entry(root, width=50)
entry_plain.grid(row=0, column=1)

tk.Label(root, text="Key (max 8 chars):").grid(row=1, column=0, sticky="w")
entry_key = tk.Entry(root, width=50)
entry_key.grid(row=1, column=1)

btn_encrypt = tk.Button(root, text="ENKRIPSI", command=encrypt_gui)
btn_encrypt.grid(row=2, column=1, pady=10)

tk.Label(root, text="16 Subkeys:").grid(row=3, column=0, sticky="nw")
text_subkeys = scrolledtext.ScrolledText(root, width=60, height=10)
text_subkeys.grid(row=3, column=1)

tk.Label(root, text="Output Ciphertext:").grid(row=4, column=0, sticky="nw")
text_cipher = scrolledtext.ScrolledText(root, width=60, height=10)
text_cipher.grid(row=4, column=1)

root.mainloop()
