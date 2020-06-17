a=int(input("enter number a: "))
b=int(input("enter number b: "))
c=input("what operation should i do? only + for sum/ x for product/- for subtract/ / for division. ")
if(c == "-"):
    difference = a-b 
    print("difference = a-b =",difference)
elif(c == "+"):
    sum = a + b
    print("sum = a + b =",sum)
elif(c == "x"):
    product = a*b
    print("product = a*b =",product)
elif(c == "/"):
    if (b == 0 ):
        print("OPERATION canceled   cannot be divided by 0 ")
    else:
        division = a/b
        print("division = a/b =",division)
        print("/ means division")
else:
    print("WRONG OPERATION !! only + for sum/ - for subtract/x for product/ / for division")