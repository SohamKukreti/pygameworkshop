import pygame

pygame.init()
clock = pygame.time.Clock()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("OSDC workshop")

running = True

item_x = screen_width // 2
item_y = screen_height - screen_height // 4
item_dx = 0
item_dy = 0
item = pygame.image.load("assets/person.png")
item = pygame.transform.scale(item, (58, 148))

def display():
    screen.fill((255, 255, 255))
    screen.blit(item, (item_x, item_y))
    pygame.display.update()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                item_dx += 5
            if event.key == pygame.K_DOWN or event.key == pygame.K_s: 
                item_dy += 5
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                item_dx -= 5
            if event.key == pygame.K_UP or event.key == pygame.K_w: 
                item_dy -= 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                item_dx -= 5
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                item_dy -= 5
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                item_dx += 5
            if event.key == pygame.K_UP or event.key == pygame.K_w: 
                item_dy += 5

    item_x += item_dx
    item_y += item_dy
    print(item_dx)
    print(item_dy)
    display()
    clock.tick(60)