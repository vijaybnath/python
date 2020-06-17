weight = int(input('enter the weight you want to convert '))
unit = input('(kg)kilograms or (g)gram ')
if (unit == "kg"):
    converted = weight * 1000
    print(f"the weight converted = {converted} grams")
else:
    converted = weight / 1000
    print(f"the weight converted = {converted} kilogram")