command = ""
while command != "quit":
    command = input("<> ").lower()
    if command == "up":
        print("the bird has moved up")
    elif command == "down":
        print("the bird has moved down")
    elif command == "left":
        print("the bird has moved left")
    elif command == "right":
        print("the bird has moved right")
    elif command == "stop":
        print("the bird has stopped moving")
    elif command == "help":
        print("""
        up - to move the bird up
        down - to move the bird down
        right - to move the bird right
        left - to move the bird left
        """)
    elif command == "quit":
        break
    else:
        print("sorry i don't know that") 