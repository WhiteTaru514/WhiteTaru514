import turtle as t
t.speed(10)
t.bgcolor("black")
t.pensize(1)
colors = ["red","yellow","green","purple","blue","orange"]
for i in range(300):
    t.pensize(i*6//300)
    t.pencolor(colors[i%6])
    t.fd(i)
    t.left(61)
t.done()
