print("welcome to bird game")
print("if you dont know the commands type help when a arrow like sign comes like this >")
name = input("enter your bird's name ")
command = ""
while command != "quit":
    command = input("<,> ").lower()
    if command == "up":
        print("^")
        print(f" {name} has move up")
    elif command == "down":
        print
        print(f" {name} has move down")
    elif command == "right":
        print(">>")
        print(f"{name} has move right")
    elif command == "left":
        print("<<")
        print(f"{name} has move left")
    elif command == "help":
        print("""
up - to move the bird up
down - to move the bird down
left - to turn the bird left
right - to turn the bird right
 """)
    elif command == "quit":
        break
    else:
        print("sorry i dont understand that")