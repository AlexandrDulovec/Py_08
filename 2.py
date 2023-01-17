import turtle
turtle.speed(50000)

def square(side):
    for x in range(4):
        turtle.pendown()
        turtle.fd(side)
        turtle.lt(90)
        turtle.penup()

def rotation(side, count):
    for x in range(count):
        square(side)
        turtle.goto(side / 4 * (-1), side / 2)
        turtle.rt(90 / count)
        square(side)

rotation(int(input("DÉLKA STRANY: ")), int(input("POČET ČTVRECŮ:")))
turtle.done()