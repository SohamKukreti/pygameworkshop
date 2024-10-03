import pygame
import random

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

score = 0
health = 100

rect_width = 50
rect_height = 50
rect_speed = 5
rectangles = []

GREEN = (0, 255, 0)
RED = (255, 0, 0)


def create_rectangle():
    x = random.randint(0, screen_width - rect_width)
    color = GREEN if random.random() < 0.5 else RED
    return [x, 0, rect_width, rect_height, color]

def display():
    screen.fill((255, 255, 255))

    screen.blit(item, (item_x, item_y))

    for rect in rectangles:
        pygame.draw.rect(screen, rect[4], (rect[0], rect[1], rect[2], rect[3]))

    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    health_text = font.render(f"Health: {health}%", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    screen.blit(health_text, (10, 50))

    pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
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

    if item_x < 0:
        item_x = 0
    elif item_x + item.get_width() > screen_width:
        item_x = screen_width - item.get_width()
    if item_y < 0:
        item_y = 0
    elif item_y + item.get_height() > screen_height:
        item_y = screen_height - item.get_height()

    if random.randint(1, 20) == 1: 
        rectangles.append(create_rectangle())

    for rect in rectangles:
        rect[1] += rect_speed

    player_rect = pygame.Rect(item_x, item_y, item.get_width(), item.get_height())
    new_rectangles = []
    for rect in rectangles:
        rect_rect = pygame.Rect(rect[0], rect[1], rect[2], rect[3])
        if player_rect.colliderect(rect_rect):
            if rect[4] == GREEN:
                score += 1
            elif rect[4] == RED:
                health -= 20
                if health <= 0:
                    running = False  
        else:
            if rect[1] < screen_height:
                new_rectangles.append(rect)

    rectangles = new_rectangles

    display()
    clock.tick(60)

pygame.quit()
