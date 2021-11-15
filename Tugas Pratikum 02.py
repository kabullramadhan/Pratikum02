print("Kabul Ramadhan | 311810315 | TI.18.B2 | Tugas Pratikum 02")
print("PROGRAM SEDERHANA MENAMPILKAN BILANGAN TERBESAR DARI 3 BUAH BILANGAN MENGGUNAKAN STATEMENT IF")

A= int(input("MASUKAN BILANGAN PERTAMA : "))
B= int(input("MASUKAN BILANGAN KEDUA   : "))
C= int(input("MASUKAN BILANGAN KETIGA  : "))
if A > B and A > C:
 print(A, "Terbesar dari 3 bilangan yang diinputkan")
elif B > A and B > C:
    print(B, "Terbesar dari 3 bilangan yang diinputkan")
else:
   print(C, "Terbesar dari 3 bilangan yang diinputkan")
