import pygame

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

     
         

pygame.init()
renderer=pygame.display.set_mode((500,500))
pygame.display.set_caption("snek")
WHITE=(255,255,255)
RED=(255,0,0)
BLACK=(0,0,0)
renderer.fill(WHITE)
isRunning=True
currenttime=pygame.time.get_ticks()
snake = Snake(0,0)
while (isRunning):
    prevtime=currenttime
    currenttime=pygame.time.get_ticks()
    Delta=currenttime-prevtime
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
    snake.update()
    pygame.time.wait(100)
    pygame.draw.rect(renderer,BLACK,(20*snake.posx,20*snake.posy,20,20))
    pygame.display.update()
pygame.quit()


