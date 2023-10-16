import pygame
import random

# Initialize pygame
pygame.init()

# Set up the display
width, height = 800, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dinosaur Run")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Dinosaur parameters
dino_width = 32 #64
dino_height = 64
dino_x = 50
dino_y = height - dino_height - 30
dino_jump = False
dino_jump_count = 10

# Obstacle parameters
obstacle_width = 30
obstacle_height = random.randint(100, 300)
obstacle_x = width
obstacle_y = height - obstacle_height - 30
obstacle_speed = 4 #5

# Game variables
score = 0
clock = pygame.time.Clock()
game_over = False

def draw_dinosaur():
    pygame.draw.rect(screen, black, (dino_x, dino_y, dino_width, dino_height))

def draw_obstacle():
    pygame.draw.rect(screen, black, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

def display_score():
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, black)
    screen.blit(score_text, (10, 10))

def check_collision():
    if dino_x + dino_width >= obstacle_x and dino_x <= obstacle_x + obstacle_width:
        if dino_y + dino_height >= obstacle_y:
            return True
    return False

# Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not dino_jump:
                dino_jump = True

    if not game_over:
        screen.fill(white)

        # Dinosaur movement
        if dino_jump:
            if dino_jump_count >= -10:
                neg = 1
                if dino_jump_count < 0:
                    neg = -1
                dino_y -= (dino_jump_count ** 2) * 0.5 * neg
                dino_jump_count -= 1
            else:
                dino_jump = False
                dino_jump_count = 10

        # Obstacle movement
        obstacle_x -= obstacle_speed
        if obstacle_x < 0:
            obstacle_x = width
            obstacle_height = random.randint(100, 300)
            obstacle_y = height - obstacle_height - 30
            score += 1

        # Check collision
        if check_collision():
            game_over = True

        # Draw objects
        draw_dinosaur()
        draw_obstacle()
        display_score()

        # Update display
        pygame.display.flip()
        clock.tick(60)

# Game over message
font = pygame.font.Font(None, 72)
game_over_text = font.render("Game Over", True, black)
screen.blit(game_over_text, (width // 2 - 150, height // 2 - 50))
pygame.display.flip()

# Wait for a few seconds before closing the window
pygame.time.wait(2000)

# Quit the game
pygame.quit()
