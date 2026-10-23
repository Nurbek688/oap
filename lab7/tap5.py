numbers=[1,2,3,4]
squares=[]
positive=[]
for value in numbers:
    squares.append(value**2)
    if value>0 and value%2==0:
        positive.append(value)
print('Quadrattar: ', squares)
print('On zhyp sandar: ', positive)
