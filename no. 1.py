ind = 0
ipa = 0
mtk = 0
stts = ""
print('Program penentuan status kelulusan ujian mahasiswa\n')
ind = int(input("Masukkan nilai Bhs Indonesia : "))
ipa = int(input("Masukkan nilai IPA : "))
mtk = int(input("Masukkan nilai Matematika : "))

if ind >= 60 and ipa >= 60 and mtk >= 60:
    if mtk >= 70:
        stts = "LULUS"
    else :
        stts = "TIDAK LULUS"
else:
  stts = "TIDAK LULUS"

print('Status Kelulusan : '+ stts)
