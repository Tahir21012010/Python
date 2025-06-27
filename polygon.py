import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(1000,1000)
polygon = turtle.Turtle()

num_sides = int(input("Enter the number of sides for the polygon: "))
side_Leanth = int(input("Enter the length of each side: "))
angle = 360 / num_sides
for i in range(num_sides):
    polygon.forward(side_Leanth)
    polygon.right(angle)
turtle.done()