print('Penentuan bilangan genap / ganjil')
print("---------------------------------")

bilangan = int(input('Bilangan = '))

kategori = 'bilangan ganjil'
if bilangan % 2 == 0:
  kategori = 'bilangan genap'
  
print('Bilangan', bilangan, 'merupakan', kategori)