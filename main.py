import pygame

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("OSDC workshop")

running = True

square = pygame.rect.Rect(0, 0 , 50, 50)


while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.exit()
    pygame.display.update()