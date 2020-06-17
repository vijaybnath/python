energy = int(input('enter the number you want to convert '))
units = input('which type of convertion you want to do only (kw)kilowatts to watts , (kv) kilovolt to volt or (v)olt to watt ')
if (units == "kw"):
    converted = energy * 1000
    print(f"the converted energy = {converted} watt")
elif(units == "kv"):
    converted = energy * 1000
    print(f"the energy = {converted} volt")
else:
    converted = energy * 1
    print(f"the energy = {converted} watt")