# Program Pemeriksaan Peraturan Pelabuhan untuk Mas Imam

# Input berat kendaraan
A = float(input("Masukkan berat kendaraan A: "))
B = float(input("Masukkan berat kendaraan B: "))
C = float(input("Masukkan berat kendaraan C: "))

# Input batasan berat
total_limit = float(input("Masukkan batasan berat kendaraan keseluruhan: "))
private_limit = float(input("Masukkan batasan berat kendaraan yang dibawa ke ruang pribadi: "))

# Total berat ketiga kendaraan
total_weight = A + B + C

def check_compliance(A, B, C, total_limit, private_limit):
    combinations = [
        (A, B, C),  # A pribadi, B + C di kapal 
        (B, A, C),  # B pribadi, A + C di kapal
        (C, A, B)   # C pribadi, A + B di kapal
    ]
    
    for private, ship1, ship2 in combinations:
        if private <= private_limit and (ship1 + ship2) <= total_limit:
            return "Mas Imam memenuhi peraturan pelabuhan."
    
    # Jika tidak ada kombinasi yang memenuhi, periksa pelanggaran
    pelanggaran_peraturan1 = total_weight > total_limit
    pelanggaran_peraturan2 = not (A <= private_limit or B <= private_limit or C <= private_limit)
    
    if pelanggaran_peraturan1 and pelanggaran_peraturan2:
        return "Mas Imam melanggar peraturan pertama dan kedua pelabuhan."
    elif pelanggaran_peraturan1:
        return "Mas Imam melanggar peraturan pertama pelabuhan."
    elif pelanggaran_peraturan2:
        return "Mas Imam melanggar peraturan kedua pelabuhan."
    else:
        return "Mas Imam memenuhi peraturan pelabuhan."

# Output hasil pemeriksaan
hasil = check_compliance(A, B, C, total_limit, private_limit)
print(hasil)