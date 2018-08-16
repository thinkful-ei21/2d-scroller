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
charImg = pygame.image.load('8bit-mario.png')

# width of the sprite in pixels
charWidth = 80

def drawSprite(x,y): 
    # carImg is source, x,y tuple is the destiny of the image
    gameDisplay.blit(charImg, (x,y))

def game_loop():
    # location for sprite to appear
    x = 20
    y = 450

    x_change = 0
    crashed = False

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            
            # when a button is pressed
            if event.type == pygame.KEYDOWN:

                # if the button pressed is a left
                if event.key == pygame.K_LEFT:
                    x_change = -5

                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        # once the character gets to the right border
        # it jumps back to the left
        if x + charWidth > display_width:
            x = 0
        # adds the x_change to x to move
        x += x_change
        gameDisplay.fill(white)
        
        # calls the function, which draws the char
        drawSprite(x,y)

        # updates the display after filling the background with white
        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()