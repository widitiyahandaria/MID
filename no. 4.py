import sys
gj_pokok=int(0)
gj_bersih=int(0)
ptgn=float(0)
kd=str("")
nm=str("")
gl=str("")
print('=====================================================\n')
print('Program penentuan gaji pokok dan gaji bersih karyawan\n')
print('=====================================================\n')

kd = str(input("Masukkan kode karyawan : "))
nm = str(input("Masukkan nama karyawan : "))
gl = str(input("Masukkan golongan (A,B,C,D): "))
print('\n')


if gl not in ["A", "B", "C", "D"]:
    print("Golongan yang anda inputkan tidak sesuai")
    sys.exit()
else:
    if gl == "A":
        gj_pokok = 10000000
        ptgn = 2.5
    elif gl == "B":
        gj_pokok = 8500000
        ptgn = 2.0
    elif gl == "C":
        gj_pokok = 7000000
        ptgn = 1.5
    elif gl == "D":
        gj_pokok = 5500000
        ptgn = 1.0

hsl_ptg = gj_pokok*(ptgn/100)
gj_bersih = gj_pokok-hsl_ptg

print('=====================================================\n')
print('STRUK RINCIAN GAJI KARYAWAN\n')
print('-----------------------------------------------------\n')
print('Nama Karyawan : '+ nm +' (Kode: '+kd+')')
print('Golongan : '+ gl)
print('-----------------------------------------------------\n')
print('Gaji Pokok : Rp. {:,}'.format(int(gj_pokok)).replace(',','.'))
print('Potongan ('+str(ptgn)+' %): Rp. {:,}'.format(int(hsl_ptg)).replace(',','.'))
print('----------------------------------------------------- -\n')
print('Gaji Bersih : Rp. {:,}'.format(int(gj_bersih)).replace(',','.'))
