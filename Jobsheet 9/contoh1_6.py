a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

x1 = (-b + (b * a - 4 * a * c) ** 0.5) / (2 * a)
x2 = (-b - (b * a - 4 * a * c) ** 0.5) / (2 * a)

print()
print('x1 = ', x1)
print('x2 = ', x2)