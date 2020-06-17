distance = int(input('enter the distance '))
unit = input('(k)ilometre or (m)etre ')
if unit.upper() =="K":
    converted = distance * 1000
    print(f"the distance = {converted} metre")
else:
    converted = distance / 1000
    print(f"the distance is = {converted} kilometre")