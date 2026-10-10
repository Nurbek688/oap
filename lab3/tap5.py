num1=int(input('Бірінші санды енгізіңіз: '))
num2=int(input('Екінші санды енгізіңіз: '))
if num1==num2:
    print('Екі сан бірдей')
else:
    if num1>num2:
        print(num1, '=', 'Үлкен сан')
    else:
        print(num2, '=', 'Кіші сан')