import pygame
import numpy as num
import random as rand
# Initialize Pygame
pygame.init()

# Set up display
width, height = 1024, 768
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My First Pygame Program")
Running = True
# drawing shapes
screen.fill((120,145,123))

#to draw circle of circles
x = 450
y = 384-150
for i in range(100):
    pygame.draw.circle(screen,(rand.randint(1,255),rand.randint(1,255),rand.randint(1,255)),(x,y),80,1)
    x = x + 150 * num.cos(i)
    y = y + 150 * num.sin(i)

"""
#to draw the cool grid shaped thing
i=0
while i<1024:
    pygame.draw.line(screen,(255,0,0),(0,i),(i,768))
    i+=20
"""
"""
#to draw a grid
i=0
while (i<1024):
    pygame.draw.line(screen,(255,0,0),(i,0),(i,768),1)
    pygame.draw.line(screen,(255,0,0),(0,i),(1024,i),1)
    i+=20
"""

"""
#some tests
pygame.draw.arc(screen,(255,0,0),(10,10,600,350),0,20,1)
pygame.draw.aalines(screen,(255,0,0),True,[(0,0),(10,10),(100,100),(500,500)],100)
pygame.draw.line(screen,(255,0,0),(100,0),(600,500),10)
"""
#updating the screen so the shapes appears
pygame.display.update()

# Main game loop
while Running:
    for event in pygame.event.get():
        


        if event.type == pygame.QUIT:
            Running = False
            