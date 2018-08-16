import pygame

# initializes pygame
pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('James\' Game')

clock = pygame.time.Clock()

crashed = False
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
