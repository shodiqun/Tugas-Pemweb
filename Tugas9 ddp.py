def profil(nama, alamat, gender, umur, hobi):
    print("Nama saya", nama)
    print("Alamat saya", alamat)
    print("Gender saya", gender)
    print("Umur saya", umur)
    print("Hobi saya", hobi)
profil("shodiqun Amin","Depok","laki laki","20","renang")

def Cek_kelulusan(nilai):
    if nilai < 60:
        return "Gagal"
    elif nilai <= 70:
        return "baik"
    elif nilai <= 80:
        return "sangat baik"
    elif nilai <= 100:
        return "Istimewa"
    input_nilai = 75
hasil = Cek_kelulusan(60)
print("nilai:", 60)
print("kelulusan:", hasil)

def ganjil(batas):
    for i in range(1, batas + 1, 2):
         print(i)

batas_gajil = 100
print(f"nilai ganjil hingga {batas_gajil }:")
ganjil(batas_gajil )


