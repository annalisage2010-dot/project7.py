
import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colour Loop Artwork")

artist = turtle.Turtle()
artist.speed("fastest")
artist.hideturtle()
artist.pensize(2)

def draw_petal(size, color):
    artist.color(color)
    artist.begin_fill()

    for _ in range(2):
        artist.circle(size, 60)
        artist.left(120)

    artist.end_fill()

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet","pink"]

for i in range(36):
    draw_petal(90, colors[i % len(colors)])
    artist.right(10)

artist.penup()
artist.goto(0, -25)
artist.pendown()

artist.penup()
artist.goto(0,0)
artist.pendown()
petal_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet","pink"]
for i in range(36):
    artist.color(petal_colors[i % len(petal_colors)],
                   petal_colors[(i +2) % len(petal_colors)])
    artist.begin_fill()
    for j in range(4):
     artist.forward(55)
     artist.right(90)
    artist.end_fill()
    artist.right(10)

artist.color("white")
artist.begin_fill()
artist.circle(30)
artist.end_fill()

turtle.done()