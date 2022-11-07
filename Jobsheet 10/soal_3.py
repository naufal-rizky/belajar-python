import os

# untuk membersihkan terminal
os.system("cls")

print('Program Hitung BMI')

# untuk memasukan berat dan tinggi badan
tinggi = float(input('Masukan Tinggi Badan (cm) : '))
berat  = float(input('Masukan Berat Badan (kg)  : '))

# untuk menghitung BMI
bmi    = berat / (tinggi / 100) ** 2

print('Tinggi badan anda : %.2f' %tinggi)
print('Berat  badan anda : %.2f' %berat)

# untuk menentukan golongan BMI
if bmi < 18.5:
    print('BMI = %.2f | Anda termasuk kategori "Kurus"' %bmi)
elif bmi >= 18.5 and bmi < 25:
    print('BMI = %.2f | Anda termasuk kategori "Normal"' %bmi)
elif bmi >= 25 and bmi < 30:
    print('BMI = %.2f | Anda termasuk kategori "Kelebihan Berat Badan"' %bmi)
else:
    print('BMI = %.2f | Anda termasuk kategori "Kegemukan"' %bmi)
