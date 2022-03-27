ind = 0
ipa = 0
mtk = 0
stts = ""
print('==================================================\n')
print('Program penentuan status kelulusan ujian mahasiswa\n')
print('==================================================\n')
ind = int(input("Masukkan nilai Bhs Indonesia : "))
ipa = int(input("Masukkan nilai IPA : "))
mtk = int(input("Masukkan nilai Matematika : "))
print('\n')
if ind < 0 or ipa < 0 or mtk < 0:
     print('Maaf inputan ada yang tidak valid')
elif ind > 100 or ipa > 100 or mtk > 100:
     print('Maaf inputan ada yang tidak valid')
else:
    if ind >= 60 and ipa >= 60 and mtk >= 60:
       if mtk >= 70:
            stts = "LULUS"
       else :
            stts = "TIDAK LULUS"
    else:
      stts = "TIDAK LULUS"

    print('Status Kelulusan : '+ stts)
