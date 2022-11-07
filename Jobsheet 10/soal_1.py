angka = list(map(int, input('Masukan 5 Angka = ') .split()))

for i in range(len(angka)):
    for j in range(i, len(angka)):
        if angka[i] > angka[j]:
            angka[i], angka[j] = angka[j], angka[i]
            
print('Angka dari kecil ke besar : ', angka)