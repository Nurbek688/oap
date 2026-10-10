# Тапсырма 5. Екінші ең үлкен элемент
a = list(map(int, input("Массив: ").split()))

if len(a) < 2:
    print("Элемент саны 2-ден аз, екінші үлкен элемент жоқ")
else:
    first = float('-inf')
    second = float('-inf')
    for x in a:
        if x > first:
            second = first
            first = x
        elif x > second and x != first:
            second = x

    if second == float('-inf'):
        print("Барлық элемент бірдей, екінші үлкен элемент жоқ")
    else:
        print("Екінші ең үлкен элемент:", second)