num1 = []
num = int(input('how many numbers you want to enter in your list '))
for n in range(num):
    numbers = int(input("enter numbers "))
    num1.append(numbers)
print("The sum of all numbers in the list: ",sum(num1))