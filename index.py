import pygame
import time

# initializes pygame
pygame.init()

display_width = 800
display_height =  600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Awesome 2D Side-Scroller!!')

# defines colors with rGBA
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# creates an object to help track time
clock = pygame.time.Clock()
charImg = pygame.image.load('8bit-mario.png')

# width of the sprite in pixels
charWidth = 80

def drawSprite(x,y): 
    # carImg is source, x,y tuple is the destiny of the image
    gameDisplay.blit(charImg, (x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 30)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    # updates the game display, it doesn't auto-update
    pygame.display.update()
    time.sleep(2)

    game_loop()

def charDeath():
    message_display('You died!')

def game_loop():
    # location for sprite to appear
    x_position = 20
    y = 450

    x_change = 0
    y_change = 0
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            
            # when a button is pressed
            if event.type == pygame.KEYDOWN:

                # if the button pressed is a left
                if event.key == pygame.K_LEFT:
                    x_change = -5

                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                
                elif event.key == pygame.K_UP:
                    
                    y_change = -5
                    # y += y_change
                    # pygame.display.update()
                    # while y < 450:
                    #     pygame.display.update()


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                
                if event.key == pygame.K_UP:
                    y_change = 5

        # once the character gets to the right border
        # it jumps back to the left
        # adds the x_change to x to move
        x_position += x_change
        y += y_change

        gameDisplay.fill(white)
        
        # calls the function, which draws the char
        drawSprite(x_position,y)

        # if the char gets to the ride boundary,
        # set the x_change to 0
        # and subtract 5 from x to reverse the K_RIGHT event
        if x_position + charWidth > display_width:
            x_change = 0
            x_position = x_position - 5
            # charDeath()
        
        # once the char position is less than 20
        # reset the position 
        # prevents movement beyond that left border
        if x_position < 20:
            x_change = 0
            x_position = x_position + 5

        if y > 450:
            y_change = 0
            
        # updates the display after filling the background with white
        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()