import pygame
import back
import front


file = 'graphics/background.png'
background = pygame.image.load(file)
rect = background.get_rect()
print(background)

pygame.init()
rect.size = (rect.size[0]*0.7, rect.size[1]*0.7)
screen = pygame.display.set_mode(rect.size)
pygame.display.set_caption('SR TowerDefense')

# creating a bool value which checks 
# if game is running
running = True
 
# setting variable to storecolor
color = "red"
 
# keep game running till running is true
while running:
   
    # Check for event if user has pushed 
    # any event in queue
    for event in pygame.event.get():
         
        # if event is of type quit then set 
        # running bool to false
        if event.type == pygame.QUIT:
            running = False
     
    # set background color to our window
    screen.fill(color)
    

    front.updateFront()
    # Update our window
    pygame.display.flip()