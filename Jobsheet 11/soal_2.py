import os

os.system("cls")

print('=== PROGRAM SOAL 2 ===\n')
print('menampilkan bilangan antara 2 dan 100 yang habis dibagi 8 :')

for i in range(2, 101):
    while i % 8 == 0:
        print(i, end=" ")
        i += 1
        
print("\n")