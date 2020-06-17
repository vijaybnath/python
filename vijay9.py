c = input('what shape do you want to find the area only sqaure/rectangle ')
a = int(input('enter length '))
if (c == "rectangle"):
    b = int(input('enter breadth '))
if(c == "square"):
    area  = a * a
    print('area of a square = ', area)
if(c == "rectangle"):
    area = a * b
    print('area of a rectangle = ', area)