import turtle

window = turtle.Screen()
window.bgcolor('lightblue')

def round_rectangle(length,high,cor_angle,cor_rad):    
  for i in range(2):
    turtle.fd(high)
    turtle.circle(cor_rad,cor_angle)
    turtle.fd(length)
    turtle.circle(cor_rad,cor_angle)    

def round_square(length,high, cor_angle, cor_rad):
  for i in range(2):
    turtle.fd(high)
    turtle.circle(cor_rad, cor_angle)
    turtle.fd(length)
    turtle.circle(cor_rad, cor_angle)

def main():
  turtle.pensize(3)
  turtle.speed(10)
  turtle.seth(90)

  turtle.pencolor("#8E8e8e")
  turtle.penup()  
  turtle.goto(152,-152)
  turtle.pendown()
  round_rectangle(144,284,90,30)

  turtle.penup()  
  turtle.goto(150,-150)
  turtle.pendown()
  turtle.begin_fill()
  turtle.color("black")
  round_rectangle(140,280,90,30)
  turtle.end_fill()

  turtle.pencolor("white")
  turtle.penup()  
  turtle.goto(135,-150)
  turtle.pendown()
  turtle.begin_fill()
  turtle.color("white")
  round_rectangle(170,280,90,0)
  turtle.end_fill()

  for i in range(3):
    turtle.pencolor("#595959")
    turtle.penup()
    turtle.goto(60 + (i-1)*40, 60)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#cccccc")
    round_square(10,10,90,5)
    turtle.end_fill()

  for i in range(3):
    turtle.pencolor("#595959")
    turtle.penup()
    turtle.goto(60 + (i-1)*40, 20)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#cccccc")
    round_square(10,10,90,5)
    turtle.end_fill()

  for i in range(3):
    turtle.pencolor("#595959")
    turtle.penup()
    turtle.goto(60 + (i-1)*40, -20)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("#cccccc")
    round_square(10,10,90,5)
    turtle.end_fill() 

  turtle.pencolor("#595959")
  turtle.penup()
  turtle.goto(60, -60)
  turtle.pendown()
  turtle.begin_fill()
  turtle.color("#cccccc")
  round_square(10,10,90,5)
  turtle.end_fill()

  turtle.pencolor("#00cc00")
  turtle.penup()
  turtle.goto(60, -100)
  turtle.pendown()
  turtle.begin_fill()
  turtle.color("#00cc00")
  round_square(10,10,90,5)
  turtle.end_fill()
    
  turtle.exitonclick()

main()