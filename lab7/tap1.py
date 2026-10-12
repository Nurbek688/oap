text=input('Сандарды бос орынмен енгізіңіз: ').split()
numbers=[int(x) for x in text]
print('Тізім: ', numbers)
print('Элементтар саны: ', len(numbers))
if numbers:
    print('Birinshi: ', numbers[0])
    print('Songy: ', numbers[-1])
    