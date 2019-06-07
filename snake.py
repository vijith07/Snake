import pygame
import random
class Food:
    
    def __init__(self,x,y):
        self.posx=random.randint(0,25)
        self.posy=random.randint(0,25)
    def reset(self):
        self.posx=random.randint(0,25)
        self.posy=random.randint(0,25)
    def draw(self,renderer):
         pygame.draw.rect(renderer,RED,(20*self.posx,20*self.posy,20,20))
class Snake:
    
    global accum
    def __init__(self,x,y):
         self.posx=x
         self.posy=y
         self.velx=0
         self.vely=0
    def update(self):   
         self.posx+=self.velx
         self.posy+=self.vely
         if((food.posx==self.posx) and (food.posy == self.posy)):
             food.reset()
    def draw(self,renderer):
         pygame.draw.rect(renderer,BLACK,(20*self.posx,20*self.posy,20,20))

     
         

pygame.init()
timeelapsed=0
clock=pygame.time.Clock()
renderer=pygame.display.set_mode((500,500))
pygame.display.set_caption("snek")
WHITE=(255,255,255)
RED=(255,0,0)
BLACK=(0,0,0)
renderer.fill(WHITE)
isRunning=True
snake = Snake(0,0)
food = Food(20,20)
while (isRunning):
    deltatime = clock.tick()
    timeelapsed+=deltatime
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            isRunning=False
        key=pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            isRunning=False
        if key[pygame.K_RIGHT]:
            snake.velx=1
            snake.vely=0
        if key[pygame.K_LEFT]:
            snake.velx=-1
            snake.vely=0
        if key[pygame.K_UP]:
            snake.velx=0
            snake.vely=-1    
        if key[pygame.K_DOWN]:
            snake.velx=0
            snake.vely=1 

    renderer.fill(WHITE)
    if timeelapsed>100:
        snake.update()
        timeelapsed=0
    snake.draw(renderer)   
    food.draw(renderer)
    pygame.display.update()
pygame.quit()


