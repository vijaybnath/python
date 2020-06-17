a = int(input('enter the no of elements you want to enter '))
print('enter the list ')
b = []
for i in range(a):
    c = int(input(""))
    b.append (c)
max = b[0]
for number in b:
    if number > max:
        max = number
print('the biggest number in the list is',max)