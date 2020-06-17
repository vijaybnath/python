number = int(input('enter the number: '))
number2 = int(input('enter the second number: '))
unit = input('only (+)for sum (-)for subract (/)for division (*)for multiplication (%)for percentage ')
if (unit == "+"):
    sum = number + number2 
    print('the sum of two numbers are ',sum)
elif (unit == "-"):
    difference = number - number2 
    print('the difference of two numbers = ',difference)
elif (unit == "*"):
    multiplication = number * number2
    print('the multiplication of two numbers = ',multiplication)
elif (unit == "%"):
    percentage = number / number2 * 100
    print('the percentage of two numbers = ',percentage)
elif (unit == "/"):
    if (number2 == "0"):
        print('operation canceled because you cannot divide any number by 0')
    else:
        division = number / number2
        print('the division of two numbers = ',division)
else:
    print('operation canceled only sum/multipication/division/percentage/subtract')