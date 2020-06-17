import tkinter as tk
import turtle

HEIGHT = 600    
WIDTH = 600
root = tk.Tk()
wn = turtle.Screen()
wn.title("Game")
wn.bgcolor("Turquoise")

player = turtle.Turtle()
player.shape("triangle")
player.color("blue")
player.penup()
player.setposition(0, -270)
player.setheading(90)

playerspeed = 15

enemy = turtle.Turtle()
enemy.shape("circle")
enemy.color("red")
enemy.penup()

enemyspeed = 15


def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < - 280:
        x = - 280
    player.setx(x)
    
def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)


turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")


wn.mainloop()

root.mainloop()