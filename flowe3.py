import turtle as bunga
s=bunga.Screen()

bunga.setup(800,800)
s.bgcolor('#282A3A')
bunga.pencolor('#000000')
bunga.speed(0)
bunga.tracer(100)
bunga.pensize(1)
col = ('#FF1493', '#CD1076', '#8B0A50', '#00BFFF')

for i in range(3):
    for n in range(400):
        bunga.color(col[n%4])
        bunga.circle(190-n/2,90)
        bunga.left(90)
        bunga.circle(190-n/2,90)
        bunga.color(col[n%4])
    bunga.left(30)
s.exitonclick()