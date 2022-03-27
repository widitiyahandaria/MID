import sys
#WIDITIYA HANDARIA
gj_pokok=int(0)
gj_bersih=int(0)
gj_kotor=int(0)
ptgn=float(0)
kd=str("")
nm=str("")
gl=str("")
stts=int(0)
jml_anak=0
tunjangan_pasangan=0
tunjangan_anak=0
status_menikah=""

print('=====================================================\n')
print('Program penentuan gaji pokok dan gaji bersih karyawan\n')
print('=====================================================\n')

kd = str(input("Masukkan kode karyawan : "))
nm = str(input("Masukkan nama karyawan : "))
gl = str(input("Masukkan golongan (A,B,C,D): "))
stts = int(input("Masukkan status (1: menikah, 2: belum) : "))

if stts == 1:
    jml_anak = int(input("Masukkan jumlah anak : "))
    
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
        
if stts not in [1, 2]:
    print("Status yang anda inputkan tidak sesuai")
    sys.exit()

if stts == 1:
    tunjangan_pasangan = gj_pokok*10/100
    status_menikah = 'Menikah'
    if jml_anak != 0:
        tunjangan_anak = gj_pokok*5/100
    else:
        tunjangan_anak = 0
else:
    tunjangan_pasangan = 0
    status_menikah = 'Belum'

gj_kotor = gj_pokok+tunjangan_pasangan+(tunjangan_anak*jml_anak) 
hsl_ptg = gj_kotor*(ptgn/100)
gj_bersih = gj_kotor-hsl_ptg


print('=====================================================\n')
print('STRUK RINCIAN GAJI KARYAWAN\n')
print('-----------------------------------------------------\n')
print('Nama Karyawan : '+ nm +' (Kode: '+kd+')')
print('Golongan : '+ gl)
print('Status Menikah : '+ status_menikah)
print('Jumlah Anak : '+ str(jml_anak))
print('-----------------------------------------------------\n')
print('Gaji Pokok : Rp. {:,}'.format(int(gj_pokok)).replace(',','.'))
print('Tunjangan Istri/Suami : Rp. {:,}'.format(int(tunjangan_pasangan)).replace(',','.'))
print('Tunjangan anak : Rp. {:,}'.format(int((tunjangan_anak*jml_anak))).replace(',','.'))
print('-----------------------------------------------------\n')
print('Gaji Kotor : Rp. {:,}'.format(int(gj_kotor)).replace(',','.'))
print('Potongan ('+str(ptgn)+' %): Rp. {:,}'.format(int(hsl_ptg)).replace(',','.'))
print('----------------------------------------------------- -\n')
print('Gaji Bersih : Rp. {:,}'.format(int(gj_bersih)).replace(',','.'))
