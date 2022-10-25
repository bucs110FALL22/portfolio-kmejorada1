import pygame

class Character:
  def __init__(self):
    self.color = "red"
    self.height =  5
    self.pos = (0,0)

class background:
  def __init__(sky):
    sky.color = "blue"
    sky.window = pygame.display.set_mode(50,50)
    sky.color_change = False

class floor:
  def __init__(blocks):
    blocks.texture_change = False
    blocks.color = "red"
    blocks.size = 10