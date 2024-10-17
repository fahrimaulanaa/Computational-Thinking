n = int(input("Masukkan ukuran persegi: "))
diag_motif = input("Masukkan motif diagonal: ")
fill_motif = input("Masukkan motif isi: ")

# Pembuatan pola persegi
for i in range(n):
    baris = ""
    for j in range(n):
        if i == j or (i + j) == (n - 1):
            if diag_motif == "":
                baris += " "
            else:
                baris += diag_motif
        else:
            if fill_motif:
                baris += fill_motif
            else:
                baris += " "
    print(baris)