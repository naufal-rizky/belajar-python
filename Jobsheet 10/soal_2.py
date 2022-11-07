print('=== PROGRAM TAHUN KABISAT ===')
print('')
tahun = int(input('Masukan Tahun = '))
if tahun % 4 == 0 and tahun % 400 == 0:
    print('%d adalah tahun kabisat' %tahun)
else:
    print('%d bukan tahun kabisat' %tahun)