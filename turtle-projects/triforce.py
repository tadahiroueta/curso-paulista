import turtle
trl=turtle.Turtle()
#importation
d=700
n=1
x=1
y=0
z=0
#variable input
def t():
    for i in range(3):
        trl.pendown()
        trl.forward(d)
        trl.left(120)
        trl.penup()
#defining
trl.speed(100)
trl.penup()
trl.right(-90)
trl.forward(300)
trl.right(-150)
#placing1
trl.pensize(5)
t()
trl.pensize(1)
#triangle1
trl.forward(d)
trl.left(120)
d=d/2
trl.forward(d)
trl.left(60)
#placing2
t()
#triangle2
trl.forward(d)
trl.left(120)
d=d/2
trl.forward(d)
trl.right(120)
#placing3
while True:
#loops definetly
    y=(x+2**n*z)
    x=y
    z=1
    n=n+1
#formula
    def t():
        for i in range(3):
            t()
            trl.right(120)
            trl.forward(d*y)
#defines continiouly
    t()
#triangle 3<=
    
    trl.forward(d)
    trl.left(120)
    d=d/2
    trl.forward(d)
    trl.left(60)
#placing 4<=
