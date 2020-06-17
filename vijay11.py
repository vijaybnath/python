distance = int(float(input('enter the distance ')))
unit = input('(k)ilometre or (m)iles ')
if unit.upper() =="K":
    converted = distance * 1.609
    print(f"the distance = {converted} miles")
else:
    converted = distance * 1.609
    print(f"the distance is = {converted} kilometre")