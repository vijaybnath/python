import turtle
import  time

wn = turtle.Screen()
wn.title("TETERIS")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

delay = 0.02

class Shape():
    def __init__(self):
        self.x =5
        self.y =0
        self.color = 4

    def move_left(self, grid):
        if self.x >0:
            if grid[self.y][self.x - 1] == 0:
                grid[self.y][self.x] = 0
                self.x -= 1

    def move_right(self, grid):
        if self.x < 11:
            if grid[self.y][self.x + 1] == 0:
                grid[self.y][self.x] = 0
                self.x += 1

grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 2, 3, 4, 0, 0, 0, 7, 1, 2, 3],

]

print(len(grid))

pen = turtle.Turtle()
pen.penup()
pen.speed(0)
pen.shape('square')
pen.setundobuffer(None)

def draw_grid(pen, grid):
    pen.clear()
    top = 230
    left = -110

    colors = ["black", "lightblue", "blue", "orange", "yellow", "green", "purple", "red"]

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            screen_x = left + (x * 20)
            screen_y = top - (y * 20)
            color_number = grid[y][x]
            color = colors[color_number]
            pen.color(color)
            pen.goto(screen_x, screen_y)
            pen.stamp()

shape = Shape()

grid[shape.y][shape.x] = shape.color

draw_grid(pen, grid)

wn.listen()
wn.onkey(lambda: shape.move_left(grid), "a")
wn.onkey(lambda: shape.move_right(grid), "d")

while True:
    wn.update()

    # move the shape
    if shape.y == 23:
        shape = Shape()
    elif grid [shape.y + 1][shape.x] == 0:
        grid[shape.y][shape.x] = 0
        shape.y += 1
        grid[shape.y][shape.x] = shape.color
    else:
        shape = Shape()

    y = 23
    while y > -1:
        is_full = True
        for x in range(0, 12):
            if grid[y][x] == 0:
                is_full = False
                y -= 1
                break
    if is_full:
        for y in range(22, -1, -1):
            for copy_x in range(0, 12):
                grid[copy_y+1][copy_x] = grid[copy_y][copy_x]

    draw_grid(pen, grid)
    time.sleep(delay)

wn.mainloop()