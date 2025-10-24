def biner_ke_desimal (biner_str):
    return int(biner_str, 2)

def biner_ke_hexadesimal(biner_str):
    desimal = int(biner_str, 2)
    return hex(desimal)[2:].upper() 
print("KONVERSI BILANGAN BINER")
biner_input = input("Masukkan bilangan biner : ")

try:
    if not all(bit in '01' for bit in biner_input):
        raise ValueError("Input harus berupa bilangan biner yaitu hanya 0 dan 1")
    
    desimal_output = biner_ke_desimal(biner_input)
    heksa_output = biner_ke_hexadesimal(biner_input)

    print(f"Hasil Konversi:")
    print(f"Biner : {biner_input}")
    print(f"Desimal : {desimal_output}")
    print(f"Heksadesimal : {heksa_output}")

except ValueError as e:
    print(f"Error: {e}")
