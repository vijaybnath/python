import tkinter as tk
import turtle
import math
import random

HEIGHT = 100000
WIDTH = 100000
root = tk.Tk()
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("space invaders") 

# draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# set the score to 0
score = 0

#draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("arial", 14, "normal"))
score_pen.hideturtle()


# create th player
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 23



# chosse a no of nnemies
number_of_enemies = 5
enemies = []

# add enemies to the list
for i in range(number_of_enemies):
    # create enemy
    enemies.append(turtle.Turtle())
   
for enemy in enemies:
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemyspeed = 2

# create the players 
bullet = turtle.Turtle()
bullet.color("gold")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 40

# define bullet states
# ready - ready to fire
# fire - bullet is firing
bulletstate = "ready"



# move player
def move_left():
    x = player.xcor()
    x -=playerspeed
    if x < -280:
        x = - 280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    # declear bullet state as a global if it needs to be changed
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
    # move the bullet to the just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

#create key bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "Up")

# main gameloop
while True:

    for enemy in enemies:
        # move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        #move the enemey bac and down
        if enemy.xcor() > 280:
            # move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
                # change enemy directio
            enemyspeed *= -1
           
        if  enemy.xcor() < -280:
            # move allenemies up
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
                #
            enemyspeed *= -1

    #check for collision between the bullet and the enemy
        if isCollision(bullet, enemy):
            # reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            # reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            # update the score
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("arial", 14, "normal"))

        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Gameover")
            break

        
    # move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #check to see if the bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

        
delay = input("Press enter to finish")


root.mainloop()