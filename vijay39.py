import tkinter as tk
import turtle
import math

HEIGHT = 600
WIDTH = 600
root = tk.Tk()

# this function draws the grid the game will be played on
def drawBoard():
    # draw both of the horizontal lines
    for i in range (2):
        drawer.penup()
        drawer.goto(-300, 100 - 200 * i)
        drawer.pendown()
        drawer.forward(600)

    drawer.right(90)

    # draw the both of vertical lines
    for i in range(2):
        drawer.penup()
        drawer.goto(-100 + 200 * i, 300)
        drawer.pendown()
        drawer.forward(600)

    # add numbers to the top corner of each sqaure
    num = 1
    for i in range (3):
        for j in range(3):
            drawer.penup()
            drawer.goto(-290 + j * 200, 280 - i * 200)
            drawer.pendown()

            drawer.write(num, font= ("Arial", 12))
            num += 1


    #update the screen  with new changes
    screen.update()

# this function draws an "x" centered at the inputted coordinates
def drawX(x, y):
    # move the correct spot
    drawer.penup()
    drawer.goto(x, y)
    drawer.pendown()

    drawer.setheading(60)

    # draw the lines of the x
    for i in range (2):
        drawer.forward(75)
        drawer.backward(150)
        drawer.forward(75)
        drawer.left(60)

    # update the screen
    screen.update()

# this function draws an "o" centered at the inputed coordinate
def drawO(x, y):
    # move to the correct spot
    drawer.penup()
    drawer.goto(x, y + 75)
    drawer.pendown()

    drawer.setheading(0)

    # draw a big circle ith the currect size
    for i in range(180):
        drawer.forward((150 * math.pi)/180)
        drawer.right(2)

    # update the screen
    screen.update()

# this function will check if the inputted player hes won
def checkWon(letter):
    # check if there are three in a row horizontally
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] == letter:
            return True

        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] == letter:
            return True

        # check if there are three in a row diagonally down
        if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == letter:
            return True

        if  board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] == letter:
            return True

        # if at this point the given letter has not won
        return False 

# this function checks that there is a tie
def checkDraw():
    # count the number of x s in the board
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == "x":
                count += 1

    # check what the value of count was
    if count > 3:
        return True
    else:
        return False

# this function will add an o on the board to the best places
def addO():
    # check if any places would result in a win for O
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "o"
                if checkWon("o"):
                    drawO(-200 + 200 * j, 200 - 200 * i)
                    return
                board[i][j] = " "
    # check if there is any place that o should block x form winning
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "x"
                if checkWon("x"):
                    board[i][j] = "o"
                    drawO(-200 + 200 * j, 200 - 200 * i)
                    return
                board[i][j] = " "
    # try ot place an o one of the corners
    for i in range(0, 3, 2):
        for j in range(0, 3, 2):
            if board[i][j] == " ":
                board[i][j]  = "o"
                drawO(-200 + 200 * j, 200 - 200 * i)
                return

    # place an o in any open spot
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "o"
                drawO(-200 + 200 * j, 200 - 200 * i)
                return

# this activates all the function
def activate(functions):
    for i in range(9):
        screen.onkey(functions[i], str(i + 1))

# this function deactivate all functions
def deactivate():
    for i in range(9):
        screen.onkey(None, str(i + 1))

# this fnction will try to add an x to the  inputted location
def addX(row, column):
    # clear any announcment
    announcer.clear()
    # check if the space they want to add is fill
    if board[row][column] == "x" or board[row][column] == "o":
        # tell them  they cant take that spot
        announcer.write("That spot is taken !", font = ("Arial", 36))
        screen.update()
    else:

        # draw an x on the correct 
        drawX(-200 + 200 * column, 200 - 200 * row)

        # add a x to the computer's board
        board[row][column] = "x"

        # check if that new x made x win
        if checkWon("x"):
            # tll the user they won
            announcer.goto(-97, 0)
            announcer.write("You won !", font = ("Arial", 36))

            # update the screen and deactivate the event listeners
            screen.update()
            deactivate()
        else:
            # if they didnt win, then an o get add to the board
            addO()
            
            # check if that new o made o won
            if checkWon("o"):
                # tell the player that the lose
                announcer.goto(-90, 0)
                announcer.write("You lose !", font = ("Arial", 36))
            
                # update the screen and deactivate
                screen.update()
                deactivate()
            # check if there is a draw
            elif checkDraw():
                # tell them it was a draw
                announcer.goto(-97, 0)
                announcer.write("Its a tie !",font = ("Arial", 36))

                # update the screen
                screen.update()
                deactivate()

# define function for the event listeners
def squareOne():
    addX(0, 0)
def squareTwo():
    addX(0, 1)
def squareThree():
    addX(0, 2)
def squareFour():
    addX(1, 0)
def squareFive():
    addX(1, 1)
def squareSix():
    addX(1, 2)
def squareSeven():
    addX(2, 0)
def squareEight():
    addX(2, 1)
def sqaureNine():
    addX(2, 2)

# create a list of event listener function
functions = [squareOne, squareTwo, squareThree, squareFour, squareFive,
    squareSix, squareSeven, squareEight, sqaureNine]
    
# create turtle
drawer = turtle.Turtle()
announcer = turtle.Turtle()

drawer.pensize(10)
drawer.ht()

announcer.penup()
announcer.ht()
announcer.goto(-200, 0)
announcer.color("red")

#create screen
screen = turtle.Screen()
screen.tracer(0)

# draw the board
drawBoard()

# create the board
board = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(" ")
    board.append(row)

# activate the functions
activate(functions)
screen.listen()

root.mainloop()