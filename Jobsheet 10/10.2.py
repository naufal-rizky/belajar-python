# Penentuan bilangan genap atau ganjil

print('Penentuan bilangan genap/ganjil')
print('-------------------------------')

bilangan = int(input('Bilangan = '))

# Penentuan bilangan genap atau ganjil
kategori = 'bilangan ganjil'
if bilangan % 2 == 0:
    kategori = 'bilangan genap'
    
# Tampilkan hasilnya
print('Bilangan', bilangan, 'merupakan', kategori)