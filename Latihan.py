nama = input("Masukan Nama:")
uts = input("Masukan Nilai UTS:")
uas = input("Masukan Nilai UAS:")
tugas = input ("Masukan Nilai Tugas:")

akhir = (int(tugas) * .2) + (int(uts) * .4)  + (int(uas) * .4)
Keterangan = ("TIDAK LULUS", "LULUS")[akhir > 60.0]

if akhir > 80:
    huruf = "A"
elif akhir > 70:
    huruf = "B"
elif akhir > 50:
    huruf = "C"
elif akhir > 40:
    huruf = "D"
else:
    huruf = "E"

print("\nNama:",nama)
print("Nilai Uts:",uts)
print("Nilai Uas:",uas)
print("Nilai Tugas:",tugas)
print("Nilai Akhir:",akhir)
print("\nNilai Huruf:",huruf)
print("keterangan:",keterangan)