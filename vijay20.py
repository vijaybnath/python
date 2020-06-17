weight = int(float(input('enter the weight you want to convert ')))
unit = input('(kg)kilograms or (ton)tonnes ')
if (unit == "tonnes"):
    converted = weight / 0.01
    print(f"the weight converted = {converted} kilograms")
else:
    converted = weight * 0.01
    print(f"the weight converted = {converted} tonnes")