while True:
    san =int(map(input('San engiziniz: '))).split()
    if san > 0:
        break

massiv = []
for i in range(san):
    # пайдаланушыдан әр элементті сұраймыз
    element = int(input('massiv', '[i]', '=', i))
    massiv.append(element)

print('massiv =', massiv)