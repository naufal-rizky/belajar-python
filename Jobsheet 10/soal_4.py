import os

os.system("cls")

print('=== PROGRAM UNTUK MENGHITUNG BESAR PAJAK ===')
hasil = int(input('Masukan Penghasilan (juta) = '))

if hasil <= 50:
    pajak = 0.05
    bayar = hasil * pajak
    print("Penghasilan anda sebesar {} juta, anda mendapatkan pajak sebesar {:.0%} serta harus membayar sebesar {} juta" .format(hasil, pajak, bayar))
elif hasil > 50 and hasil <= 150:
    pajak = 0.15
    bayar = hasil * pajak
    print("Penghasilan anda sebesar {} juta, anda mendapatkan pajak sebesar {:.0%} serta harus membayar sebesar {} juta" .format(hasil, pajak, bayar))
elif hasil > 150 and hasil <= 500:
    pajak = 0.25
    bayar = hasil * pajak
    print("Penghasilan anda sebesar {} juta, anda mendapatkan pajak sebesar {:.0%} serta harus membayar sebesar {} juta" .format(hasil, pajak, bayar))
else:
    pajak = 0.25
    bayar = hasil * pajak
    print("Penghasilan anda sebesar {} juta, anda mendapatkan pajak sebesar {:.0%} serta harus membayar sebesar {} juta" .format(hasil, pajak, bayar))