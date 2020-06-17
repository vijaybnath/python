weight = int(input('enter the weight you want to convert '))
unit = input('(kg)kilograms or (mg)milligrams ')
if (unit == "kg"):
    converted = weight * 1000000
    print(f"the weight converted = {converted} milligrams")
else:
    converted = weight / 1000000
    print(f"the weight converted = {converted} kilograms")