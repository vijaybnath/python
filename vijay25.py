number1 = int(input("enter the number a: "))
number2 = int(input("enter the number b: "))
unit = input("(+)for sum , (-) for subtract ,(/)for division , (*)for multiplication or (%)for percentage ")
if unit == "+":
    sum = number1 + number2
    print("the sum of the two numbers are: ",sum)
elif unit == "-":
    subtract = number1 - number2
    print("the subtraction = ",subtract)
elif unit == "*":
    multiplication = number1 * number2
    print("the multiplication of two numbers are : ",multiplication)
elif unit == "%":
    percentage = number1 / number2 * 100
    print("the percentage = ",percentage)
elif unit == "/":
    if number2 == "0":
        print("operation canceled because you cannot divide any number by 0")
    else:
        division = number1 // number2
        print("the division of two numbers = ",division)
else:
    print("operation canceled because only sum/division/subtract/multiplication/percentage")