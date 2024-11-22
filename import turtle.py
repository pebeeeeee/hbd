import turtle

t =  turtle.Turtle()
t.pensize(15)

def go (x, y):
    t.penup()
    t.goto(x,  y)
    t.pendown()

t.pencolor("black")
t.fillcolor("black")

go(273.97, -258.28)
t.seth(96.07)
t.circle(1348.69,  11.44)
t.seth(107.51)
t.circle(186.17, 93.86)
t.seth(203.9)
t.circle(118.68, 30.81)
t.seth(247.8)
t.circle(26.09, 89.43)
t.seth(337.22)
t.circle(366.94, 26.42)
t.seth(3.64)
t.circle(80.93, 30.88)

go(205.86, -65.70)
t.seth(270.09)
t.circle(-710.74, 13.9)
t.seth(0)
t.forward(21.84)
t.begin_fill()
t.seth(90)
t.circle(21.84)
t.end_fill()

go(-40.44, 40.23)
t.seth(262.87)
t.circle(1202.76, 14.26)

go(-49.72, -102.85)
t.seth(235.33)
t.forward(68.74)
t.seth(225)
t.circle(-26.72,  70)
t.seth(130.7)
t.forward(78.51)

go(-159.50, -84.99)
t.begin_fill()
t.seth(180)
t.forward(75.88)
t.seth(302.66)
t.circle(45.07, 114.68)
t.end_fill()

go(-108.16, -84.99)
t.seth(180)
t.forward(173.34)

go(90.79, 75.70)
t.begin_fill()
t.seth(90)
t.circle(8.52)
t.end_fill()

go(-19.49, 77.88)
t.begin_fill()
t.seth(90)
t.circle(8.52)
t.end_fill()

t.pensize(8)
t.pencolor("black")
t.fillcolor("red")

go(32.75, 126.62)
t.begin_fill()
t.seth(320.51)
t.circle(107.03, 52.7)
t.seth(103.34)
t.forward(113.89)
t.seth(230.64)
t.forward(110)
t.end_fill()

t.pensize(6)
t.pencolor("black")
t.fillcolor("#FFF59D")

go(-108.62, -78.18)
t.begin_fill()
t.seth(90)
t.forward(64.60)
t.seth(180)
t.forward(163.41)
t.seth(270)
t.forward(64.60)
t.seth(0)
t.forward(163.41)
t.end_fill()

t.fillcolor("#FFC0CB")

go(-108.62, -35.40)
t.begin_fill()
t.seth(90)
t.forward(21.82)
t.seth(180)
t.forward(163.41)
t.seth(270)
t.forward(21.82)
t.seth(0)
t.forward(163.41)
t.end_fill()

t.fillcolor("#FFF59D")

go (-171.94, -13.58)
t.begin_fill()
t.seth(90)
t.forward(29.94)
t.seth(180)
t.forward(26.09)
t.seth(270)
t.forward(29.94)
t.seth(0)
t.forward(26.09)
t.end_fill()

go(-184.98,  16.36)
t.seth(90)
t.forward(10.69)

t.fillcolor("orange")
go(-177.07, 27.06)
t.begin_fill()
t.seth(111.7)
t.forward(22.56)
t.seth(248.3)
t.forward(22.56)
t.seth(0)
t.forward(16.68)
t.end_fill()

t.color("#4169E1")
t.penup()
t.goto(100,120)
t.pendown()
t.write("Happy Birthday", False,
        "right", ("Times New Roman", 50, "bold"))

t.color("#4169E1")
t.penup()
t.goto(270,-200)
t.pendown()
t.write("Lutfiiiiiiiii", False,
        "right", ("Times New Roman", 60, "bold"))

t.hideturtle()
turtle.done()