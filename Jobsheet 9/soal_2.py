# membuat variable untuk inputan panjang dan lebar
p = int(input('p = '))
lebar = int(input('l = '))

# membuat variable untuk menghitung luas dan keliling
l = p * lebar
k = 2 * (p + lebar)

# menampilkan luas dan keliling
print('Luas         = %.2f' %l)
print('Keliling     = %.2f' %k)