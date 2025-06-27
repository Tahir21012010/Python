import turtle
turtle.Screen().bgcolor("blue")
loadwindow = turtle.Screen()
turtle.speed(2)
for i in range(100):
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)
loadwindow.exitonclick()