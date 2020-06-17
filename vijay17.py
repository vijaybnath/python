length = int(input('enter the length '))
unit = input('(mm)millimetre or (cm)centimetre ')
if (unit == "cm"):
    converted = length / 0.1
    print(f"the converted length = {converted} millimetre")
else:
    converted = length * 0.1
    print(f"the converted length = {converted} centimetre")