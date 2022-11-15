import os

os.system("cls")

total = 0

print("===  PROGRAM SOAL 3 ===\n")
print("Menampilkan hasil penjumlahan kuadrat angka genap dari 2 - 30 :")

for i in range(2, 31):
    if i % 2 == 0:
        i = i ** 2
        total += i
        print(i, end=" ")

print()
print("Total = %d\n" %total)