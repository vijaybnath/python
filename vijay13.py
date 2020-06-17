length = int(input('enter the length '))
unit = input('(c)entimetre or (m)etre (mm)millimetre ')
if unit.upper() =="c":
    converted = length / 100
    print(f"the length = {converted} metre")
else:
    converted = length / 0.1
    print(f"the converted length = {converted} millimetre")