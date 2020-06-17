energy = int(input('enter the energy you want to convert '))
unit = input('(kv)kilo volt ')
unit.upper() == "kv"
converted = energy * 1000
print(f"the energy = {converted} volt")