row = int(input('n = '))
col = row

print()

for i in range(0, row + 1):
    for j in range(0, col + 1):
        if j and i > j:
            print("    ", end = "")
            continue
        multiply = max(1, i) * max(1, j)
        print(f"{multiply:3d} ", end = "")
    print("\n")
