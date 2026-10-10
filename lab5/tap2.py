s=0
total=[2,3,4]
for x in total:
    s+=x
print('Jalpy: ', s)

mn=total[0]
for x in total:
    if x<mn:
        mn=x
print('Minimum: ', mn)

mx=total[0]
for x in total:
    if x>mx:
        mx=x
print('Maximum: ', mx)

print('Ortasha man: ', s/2)