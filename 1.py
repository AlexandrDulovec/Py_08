import turtle
turtle.speed(50000)

def square(side):
    for x in range(4):
        turtle.pendown()
        turtle.fd(side)
        turtle.lt(90)
        turtle.penup()

def ctverecvectverci(side):
    square(side)
    turtle.goto(side / 100 * 20, side / 100 * 20)
    square(side / 100 * 60)

ctverecvectverci(int(input("ZADEJ DÉLKU STRANY:")))
turtle.done()