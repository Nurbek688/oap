numbers=[1,2,3,4]
positive=0
negative=0
zeros=0
even=0
odd=0
for value in numbers:
    if value>0:
        positive+=1
    elif value<0:
        negative+=1
    else:
        zeros+=1
    if value%2==0:
        even+=1
    else:
        odd+=1
print('On sandar: ', positive)
print('Teris sandar: ', negative)
print('Nolder: ', zeros)
print('Zhyp sandar: ', even)
print('Taq sandar: ', odd)
