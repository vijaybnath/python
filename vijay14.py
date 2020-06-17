energy = int(input('enter the energy you want to convert '))
unit = input('(v)olt or (w)att ')
if unit.upper() =="w":
    converted = energy * 1
    print(f"the energy = {converted} volt")
else:
    converted = energy * 1
    print(f"the energy = {converted} watt")