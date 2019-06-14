import pygame
import random
import numpy as np
MAX=625

class Bot:
    def __init__(self):
        pass
    def move(self):
        global snake
        global food
        if snake.pos[0] < food.posx :
             snake.vel=[1,0]
             return
        if snake.pos[0] > food.posx  :
             snake.vel=[-1,0]
             return
        if snake.pos[1] > food.posy :
             snake.vel=[0,-1]
             return
        if snake.pos[1] < food.posy :
             snake.vel=[0,1]
             return
        snake.vel=random.choice([[1,0],[0,1],[-1,0],[0,-1]])

        
        
class Food:
    def __init__(self,x,y):
        self.posx=random.randint(0,24)
        self.posy=random.randint(0,24)
    def reset(self):
        self.posx=random.randint(0,24)
        self.posy=random.randint(0,24)
    def draw(self,renderer):
         pygame.draw.rect(renderer,RED,(20*self.posx,20*self.posy,20,20))
class Snake:
    
    global accum
    def __init__(self,x,y):
         self.pos=[x,y]
         self.vel=[0,0]
         self.gameover=False
         self.tail = np.empty(shape=(MAX,2))
         self.tailstart=0
         self.tailend=0
         self.taillen=0
    def update(self):
         self.tailstart += 1
         self.tail[self.tailend%MAX]=self.pos
         self.tailend += 1
         self.pos[0]+=self.vel[0]
         self.pos[1]+=self.vel[1]
         if((food.posx==self.pos[0]) and (food.posy == self.pos[1])):
             food.reset()
             self.taillen += 1
             #print(self.taillen)
             self.tailstart -= 1
         if (self.pos[0]>24):
             self.gameover=True
         if (self.pos[0]<0):
             self.gameover=True
         if (self.pos[1]>24):
             self.gameover=True
         if (self.pos[1]<0):
             self.gameover=True
        
         for i in range(self.taillen):
             tailpos=self.tail[(self.tailstart+i)%MAX]
             if(tailpos[0]==food.posx and tailpos[1]==food.posy):
                 food.reset()
             if(tailpos[0]==self.pos[0] and tailpos[1]==self.pos[1]):
                 self.gameover=True

         
    def draw(self,renderer):
         pygame.draw.rect(renderer,BLACK,(20*self.pos[0],20*self.pos[1],20,20))
         for i in range(self.taillen):
             tailpos=self.tail[(self.tailstart+i)%MAX]
             scale=float(1 - (i/self.taillen))
             colour=( int(255*scale), int(255*scale) , int(255*scale) )
             pygame.draw.rect(renderer,colour,(20*tailpos[0],20*tailpos[1],20,20))
             
    def reset(self):
        self.pos[0]=0
        self.pos[1]=0
        self.vel[0]=0
        self.vel[1]=0
        self.tailstart=self.tailend
        self.taillen=0
        self.gameover=False

pygame.init()
font=pygame.font.Font(pygame.font.get_default_font(), 15)
timeelapsed=0
clock=pygame.time.Clock()
renderer=pygame.display.set_mode((500,500))
pygame.display.set_caption("snek")
WHITE=(255,255,255)
RED=(45,175,126)
GREY=(168,172,186)
BLACK=(0,0,0)
renderer.fill(WHITE)
isRunning=True
snake = Snake(0,0)
food = Food(24,24)
bot =Bot()
botrequest=False
level = 0
while (isRunning):
 
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            isRunning=False
        key=pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            isRunning=False
        if key[pygame.K_RIGHT] and snake.vel != [-1,0]:
            snake.vel=[1,0]
        if key[pygame.K_LEFT] and snake.vel != [1,0]:
            snake.vel=[-1,0]
        if key[pygame.K_UP] and snake.vel != [0,1]:
           snake.vel=[0,-1]  
        if key[pygame.K_DOWN] and snake.vel != [0,-1]:
           snake.vel=[0,1]
        if key[pygame.K_b]:
            if not botrequest:
                botrequest=True
            else :
                botrequest=False
        if key[pygame.K_e]:
            level+=1
        if key[pygame.K_q]:
             level-=1
    renderer.fill(WHITE)
    snake.update()
    if(not snake.gameover):
        text=font.render("score: "+str(snake.taillen*(level+1)),True,(30,30,130))
        lev=font.render("level: "+str(level+1),True,(30,30,130))
        renderer.blit(text,(500-text.get_width(),0))
        renderer.blit(lev,(500-text.get_width(),15))
        snake.draw(renderer)   
        food.draw(renderer)
    else:
        snake.reset()
        food.reset()
    clock.tick(15 + level)
    if botrequest:
        bot.move()
    pygame.display.update()
pygame.quit()


