import turtle

my_turtle = turtle.Turtle()

sides = int(input("Input the number of sides you want your shape to have "))
length = int(input("Input the length you want the sides to have "))

turn = ((sides-2)*180)/sides
if turn > 90:
  turn = turn % 90
  turn = 90 - turn

i = 0

for i in range (0, sides):
  my_turtle.forward(length)
  my_turtle.right(turn)
  i + 1
