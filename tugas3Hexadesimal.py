def hexadesimal_ke_desimal (hexadesimal_str):
    return int(hexadesimal_str, 16)

def hexadesimal_ke_biner(hexadesimal_str):
    desimal = int(hexadesimal_str, 16)
    return bin(desimal)[2: ]

def hexadesimal_ke_oktal(hexadesimal_str):
    desimal = int(hexadesimal_str, 16)
    return oct(desimal)[2: ]
print("KONVERSI BILANGAN HEXADESIMAL")
hexadesimal_input = input("Masukkan bilangan hexadesimal : ")

try:
    if not all(ch in '0123456789ABCDEF' for ch in hexadesimal_input):
        raise ValueError("Input harus berupa bilangan hexadesimal yaitu 0123456789ABCDEF")
    
    desimal_output = hexadesimal_ke_desimal(hexadesimal_input)
    biner_output = hexadesimal_ke_biner(hexadesimal_input)
    oktal_output = hexadesimal_ke_oktal(hexadesimal_input)

    print(f"Hasil Konversi:")
    print(f"Hexadesimal : {hexadesimal_input}")
    print(f"Desimal : {desimal_output}")
    print(f"Biner : {biner_output}")
    print(f"Oktal : {oktal_output}")

except ValueError as e:
    print(f"Error: {e}")
