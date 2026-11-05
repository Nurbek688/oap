def selection_sort(data):
    a = data.copy()
    comp = swap = 0
    for i in range(len(a) - 1):
        m = i
        for j in range(i + 1, len(a)):
            comp += 1
            if a[j] < a[m]: m = j
        if m != i:
            a[i], a[m] = a[m], a[i]
            swap += 1
    return comp, swap


def insertion_sort(data):
    a = data.copy()
    comp = shift = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0:
            comp += 1
            if a[j] <= key: break
            a[j + 1] = a[j]
            shift += 1
            j -= 1
        a[j + 1] = key
    return comp, shift


def bubble_sort(data):
    a = data.copy()
    comp = swap = 0
    for i in range(len(a) - 1):
        changed = False
        for j in range(len(a) - 1 - i):
            comp += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swap += 1
                changed = True
        if not changed: break
    return comp, swap

"""======Менің тізімім======"""
my_list = [12, 5, 9, 1, 7, 3]
print("Таңдау сұрыптау: ",selection_sort(my_list))
print('=' * 30)
print("Кірістіру сұрыптау: ",insertion_sort(my_list))
print('=' * 30)
print("Көпіршікті сұрыптау: ",bubble_sort(my_list))