ind = 0
ipa = 0
mtk = 0
stts = ""
alasan = ""
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
            alasan = "Sebab Nilai Matematika nya kurang dari 70"
    else:
        stts = "TIDAK LULUS"
        if ind < 60:
            alasan = "Sebab Nilai Bhs Indonesia nya kurang dari 60"
        elif ipa < 60:
            alasan = "Sebab Nilai IPA nya kurang dari 60"

    print('Status Kelulusan : '+ stts)
    if alasan != "":
        print('Sebab : ')
        print(alasan)


