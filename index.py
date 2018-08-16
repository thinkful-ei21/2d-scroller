import pygame

# initializes pygame
pygame.init()

display_width = 800
display_height =  600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Awesome 2D Side-Scroller!!')

# defines black and white with rGBA
black = (0,0,0)
white = (255,255,255)

# creates an object to help track time
clock = pygame.time.Clock()
crashed = False
charImg = pygame.image.load('8bit-mario.png')

# width of the sprite in pixels
charWidth = 80

def drawSprite(x,y): 
    # carImg is source, x,y tuple is the destiny of the image
    gameDisplay.blit(charImg, (x,y))

# location for sprite to appear
x = 0
y = 450

x_change = 0
char_speed = 0

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        
        # when a button is pressed
        if event.type == pygame.KEYDOWN:

            # if the button pressed is a left
            if event.key == pygame.K_LEFT:
                print('left button')
                x_change = -5

            elif event.key == pygame.K_RIGHT:
                print('right button')
                x_change = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0

    # once the character gets to the right border
    # it jumps back to the left
    if x + charWidth > display_width:
        x = 0
    # adds the x_change to x to mov
    x += x_change
    gameDisplay.fill(white)
    
    #draws the char
    drawSprite(x,y)

    # updates the display after filling the background with white
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()