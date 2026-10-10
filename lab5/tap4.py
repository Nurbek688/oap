# Тапсырма 4. Сызықтық іздеу
a = list(map(int, input("Массив: ").split()))
k = int(input("Іздейтін сан: "))

pos = -1
for i in range(len(a)):
    if a[i] == k:
        pos = i
        break

if pos != -1:
    print("Табылды, индекс:", pos)
else:
    print("Массивте мұндай сан жоқ")