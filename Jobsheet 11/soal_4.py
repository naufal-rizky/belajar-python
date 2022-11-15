import os

os.system("cls")

n = int(input('masukan n = '))

i = 1
while i <= 9:
    print(" " * (9 - i) + "%d " %n * i)
    i += 2