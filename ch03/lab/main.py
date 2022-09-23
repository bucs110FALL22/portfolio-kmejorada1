import turtle #1. import modules
import random
import pygame
import math

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')
turtle.delay(100)

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
mnum = random.randrange(1, 100)
lnum = random.randrange(1, 100)
michelangelo.forward(mnum)
leonardo.forward(lnum)
michelangelo.goto(-150, 20)
leonardo.goto(-150,-20)

for x in range (0, 10):
  mnum = random.randrange(1, 100)
  lnum = random.randrange(1, 100)
  michelangelo.forward(mnum)
  leonardo.forward(lnum)

michelangelo.goto(-150, 20)
leonardo.goto(-150,-20)

# PART B - complete part B here
pygame.init()
window = pygame.display.set_mode((800,800))
pygame.Color((255,255,255))

def points(num_sides):
  coords = []
  num_sides = num_sides
  side_length = 10
  offset = 20

  for i in range (num_sides):
    theta = (2.0 * math.pi * (i)) / num_sides
    x = side_length * math.cos(theta) + offset
    y = side_length * math.sin(theta) + offset
    coords.append([x, y])

  return coords

point = 3, 4, 6, 8, 360
for i in (point):
  pygame.draw.polygon(window, "blue", points(i))
  pygame.display.flip()
  pygame.time.delay(1000)
  window.fill("black")
  
#window.exitonclick()
  