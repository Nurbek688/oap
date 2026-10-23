numbers=[1,2,3,4]
if numbers:
    mn=numbers[0]
    mx=numbers[0]
    for value in numbers[1:]:
        if value<mn:
            mn=value
        if value>mx:
            mx=value
    print('Minimum: ', mn)
    print('Maximum: ', mx)
    