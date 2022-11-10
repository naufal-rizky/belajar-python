print('Penentuan nama hari')
print('0 = minggu   1 = senin')
print('2 = selasa   3 = rabu')
print('4 = kamis    5 = jumat')
print('6 = sabtu')

print('----------------------')

kodeHari = int(input('Kode Hari = '))

if kodeHari == 0:
    print('Minggu')
elif kodeHari == 1:
    print('Senin')
elif kodeHari == 2:
    print('Selasa')
elif kodeHari == 3:
    print('Rabu')
elif kodeHari == 4:
    print('Kamis')
elif kodeHari == 5:
    print('Jumat')
elif kodeHari == 6:
    print('Sabtu')
else:
    print('Kode Salah')