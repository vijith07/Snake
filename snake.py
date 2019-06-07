import pygame
import random
MAX=625
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
         self.pos=[x,y]
         self.vel=[0,0]
         self.gameover=False
    def update(self):   
         self.pos[0]+=self.vel[0]
         self.pos[1]+=self.vel[1]
         if((food.posx==self.pos[0]) and (food.posy == self.pos[1])):
             food.reset()
         if (self.pos[0]>24):
             self.gameover=True
         if (self.pos[0]<0):
             self.gameover=True
         if (self.pos[1]>24):
             self.gameover=True
         if (self.pos[1]<0):
             self.gameover=True
    def draw(self,renderer):
         pygame.draw.rect(renderer,BLACK,(20*self.pos[0],20*self.pos[1],20,20))

    def reset(self):
        self.pos[0]=0
        self.pos[1]=0
        self.vel[0]=0
        self.vel[1]=0
        self.gameover=False

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
            snake.vel=[1,0]
        if key[pygame.K_LEFT]:
            snake.vel=[-1,0]
        if key[pygame.K_UP]:
           snake.vel=[0,-1]  
        if key[pygame.K_DOWN]:
           snake.vel=[0,1]

    renderer.fill(WHITE)
    if timeelapsed>100:
        snake.update()
        timeelapsed=0
    if(not snake.gameover):
        snake.draw(renderer)   
        food.draw(renderer)
    else:
        snake.reset()
        food.reset()
    pygame.display.update()
pygame.quit()


