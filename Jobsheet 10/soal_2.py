import os

os.system("cls")

def tahunKabisat(tahun):
    if tahun % 400 == 0 and tahun % 100 == 0:
        return True
    elif tahun % 4 == 0 and tahun % 100 != 0:
        return True
    else:
        return False

print("=== PROGRAM TAHUN KABISAT ===")

tahun = int(input('Masukan Tahun = '))

if(tahunKabisat(tahun)):
    print("{} adalah tahun kabisat" .format(tahun))
else:
    print("{} bukan tahun kabisat" .format(tahun))