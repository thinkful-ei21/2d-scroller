import pygame

# initializes pygame
pygame.init()

display_width = 800
display_height =  600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Awesome 2D Side-Scroller!!')


black = (0,0,0)
white = (255,255,255)

# creates an object to help track time
clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load('racecar.png')

def car(x,y): 
    # carImg is source, x,y tuple is the destiny of the image
    gameDisplay.blit(carImg, (x,y))



while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)
        print('hello')

    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()
