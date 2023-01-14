import turtle
trl=turtle.Turtle()
#importation
dst1=0
dst2=0.001
dstd=1
#input varation
while True:
#loops definetly
    for i in range(90):
        trl.forward((dst1+dst2)*3.1415/2)
        trl.right(1)
#movement
    if dstd==1:
        dstd=2
        dst1=dst1+dst2
    else:
        dstd=1
        dst2=dst1+dst2
#inputs new variations
