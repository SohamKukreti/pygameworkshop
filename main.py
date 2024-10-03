import pygame  # Importing the Pygame library to create games
import random  # Importing the random library to generate random numbers

# Initialize Pygame so we can use its functions
pygame.init()
clock = pygame.time.Clock()  # Create a clock to manage frame rate

# Set the screen size for the game
screen_width = 800
screen_height = 600

# Create the game window with the specified width and height
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("OSDC workshop")  # Set the title of the game window

# Uncomment to load a background image (optional)
#background = pygame.image.load("assets/background.png")

# Game is running until set to False
running = True

# Set the initial position of the player
player_x = screen_width // 2  # Center horizontally
player_y = screen_height - screen_height // 4  # Place near the bottom
player_dx = 0  # Change in x-direction (initially zero, i.e., no movement)
player_dy = 0  # Change in y-direction (initially zero, i.e., no movement)

# Load the player character image and resize it
player = pygame.image.load("assets/character.png")
player = pygame.transform.scale(player, (64, 64))

# Load and resize the coin image (for green rectangles)
coin_image = pygame.image.load("assets/coin.png")
coin_image = pygame.transform.scale(coin_image, (50, 50))

# Load and resize the skull image (for red rectangles)
skull_image = pygame.image.load("assets/skull.png")
skull_image = pygame.transform.scale(skull_image, (50, 50))

# Initialize game score and player health
score = 0
health = 100

# Define properties of the falling rectangles (coins and skulls)
rect_width = 50
rect_height = 50
rect_speed = 5  # Speed at which the rectangles fall
rectangles = []  # List to hold all the falling rectangles

# Function to create a new rectangle (either a coin or a skull)
def create_rectangle():
    x = random.randint(0, screen_width - rect_width)  # Random horizontal position
    color = 'green' if random.random() < 0.5 else 'red'  # Randomly choose color: green or red
    return [x, 0, rect_width, rect_height, color]  # Return the rectangle as a list

# Function to display everything on the screen
def display():
    screen.fill((255, 255, 255))  # Fill the screen with white (clear previous frame)
    # Uncomment to draw a background image
    #screen.blit(background, (0, 0))

    # Draw the player character at its current position
    screen.blit(player, (player_x, player_y))

    # Draw all the falling rectangles
    for rect in rectangles:
        if rect[4] == 'green':  # If rectangle is green, draw a coin
            screen.blit(coin_image, (rect[0], rect[1]))  
        elif rect[4] == 'red':  # If rectangle is red, draw a skull
            screen.blit(skull_image, (rect[0], rect[1]))  

    # Display the score and health in the top left corner
    font = pygame.font.Font(None, 36)  # Set font and size
    score_text = font.render(f"monies: {score}", True, (0, 0, 0))  # Create text for score
    health_text = font.render(f"Health: {health}%", True, (0, 0, 0))  # Create text for health
    screen.blit(score_text, (10, 10))  # Draw score on screen
    screen.blit(health_text, (10, 50))  # Draw health on screen

    # Update the display to show all the drawn elements
    pygame.display.update()

# Main game loop: this runs as long as `running` is True
while running:
    # Handle events like key presses or closing the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If the user closes the window, stop running
            running = False
        # Handle key down events to move the player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player_dx += 5  # Move right
            if event.key == pygame.K_DOWN or event.key == pygame.K_s: 
                player_dy += 5  # Move down
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player_dx -= 5  # Move left
            if event.key == pygame.K_UP or event.key == pygame.K_w: 
                player_dy -= 5  # Move up
        # Handle key up events to stop moving the player
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player_dx -= 5  # Stop moving right
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player_dy -= 5  # Stop moving down
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player_dx += 5  # Stop moving left
            if event.key == pygame.K_UP or event.key == pygame.K_w: 
                player_dy += 5  # Stop moving up

    # Update the player's position based on the direction changes
    player_x += player_dx
    player_y += player_dy

    # Ensure the player does not move out of the screen bounds
    if player_x < 0:
        player_x = 0
    elif player_x + player.get_width() > screen_width:
        player_x = screen_width - player.get_width()
    if player_y < 0:
        player_y = 0
    elif player_y + player.get_height() > screen_height:
        player_y = screen_height - player.get_height()

    # Randomly add new rectangles to fall (1 in every 20 frames)
    if random.randint(1, 20) == 1: 
        rectangles.append(create_rectangle())

    # Move each rectangle down by the specified speed
    for rect in rectangles:
        rect[1] += rect_speed

    # Create rectangles representing the player and items to check collisions
    player_rect = pygame.Rect(player_x, player_y, player.get_width(), player.get_height())
    new_rectangles = []  # Create a new list for rectangles that remain on screen
    for rect in rectangles:
        rect_rect = pygame.Rect(rect[0], rect[1], rect[2], rect[3])
        if player_rect.colliderect(rect_rect):  # Check if the player collides with a rectangle
            if rect[4] == 'green':  # If it is a green rectangle (coin), increase score
                score += 1
            elif rect[4] == 'red':  # If it is a red rectangle (skull), reduce health
                health -= 20
                if health <= 0:  # If health drops to 0 or below, stop the game
                    running = False 
        else:
            if rect[1] < screen_height:  # Only keep rectangles still on the screen
                new_rectangles.append(rect)

    rectangles = new_rectangles  # Update the list of rectangles with the ones still active

    # Draw everything on the screen
    display()

    # Cap the frame rate at 60 frames per second
    clock.tick(60)

# Quit Pygame after the game loop ends
pygame.quit()
