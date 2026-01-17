import pygame
pygame.init()
screen = pygame.display.set_mode((400,300))
done = True
while done:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            done = False
    pygame.draw.rect(screen,(242, 29, 29),pygame.Rect(50,30,100,60))
    pygame.display.flip()