# menu toko polinos
print("=== TOKO POLINOS ===")
print("[1]. Bakso")
print("[2]. Soto")
print("[3]. Nasi Goreng")
# untuk input pilihan
c = int(input('Masukan pilihan anda : '))

# membuat switch case
match c:
    case 1:
        print('Anda Memilih Bakso (Rp 10.000)')
        jumlah    = int(input('Masukan Jumlah : '))
        
        harga     = 10000
        pembelian = harga * jumlah
        diskon    = (pembelian * 25) / 100
        bayar     = pembelian - diskon
        
        print('Total Pembelian  : %d' %pembelian)
        print('Total Diskon     : %d' %diskon)
        print('Total Bayar      : %d' %bayar)
    case 2:
        print('Anda Memilih Soto (Rp 7.000)')
        jumlah    = int(input('Masukan Jumlah : '))
        
        harga     = 7000
        pembelian = harga * jumlah
        diskon    = (pembelian * 25) / 100
        bayar     = pembelian - diskon
        
        print('Total Pembelian  : %d' %pembelian)
        print('Total Diskon     : %d' %diskon)
        print('Total Bayar      : %d' %bayar)
    case 3:
        print('Anda Memilih Nasi Goreng (Rp 12.000)')
        jumlah    = int(input('Masukan Jumlah : '))
        
        harga     = 12000
        pembelian = harga * jumlah
        diskon    = (pembelian * 25) / 100
        bayar     = pembelian - diskon
        
        print('Total Pembelian  : %d' %pembelian)
        print('Total Diskon     : %d' %diskon)
        print('Total Bayar      : %d' %bayar)