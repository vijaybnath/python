shape = input("what shape's peremeter do you want only square/rectangle ")
length = int(input('enter length '))
if (shape == "rectangle"):
    breadth = int(input('enter breadth '))
    peremeter = length + breadth +length + breadth
    print('peremeter of a rectangle = 2*(length + breadth) = ',peremeter)
if (shape == "square"):
    peremeter = length*4
    print('peremeter of a square = ',peremeter)
    