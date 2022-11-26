import turtle as t

colors = ['red','yellow','green','purple','orange','blue']

t.shape('turtle')
t.tracer(5)
t.bgcolor('black')

for x in range(300):
    t.pencolor(colors[x%6])
    t.width(x//20)
    t.forward(x)
    t.left(120)

    for y in range(2):
        t.fd(x)
        t.rt(120)
    
t.exitonclick()