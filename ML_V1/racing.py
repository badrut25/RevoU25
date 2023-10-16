import pygame
import random

# Initialize pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("2D Racing Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Player car parameters
player_width = 50
player_height = 100
player_x = width // 2 - player_width // 2
player_y = height - player_height - 20
player_speed = 10 #5

# Enemy car parameters
enemy_width = 50
enemy_height = 100
enemy_x = random.randint(0, width - enemy_width)
enemy_y = -enemy_height
enemy_speed = 3

# Game variables
clock = pygame.time.Clock()
score = 0
font = pygame.font.Font(None, 36)

def draw_player():
    pygame.draw.rect(screen, black, (player_x, player_y, player_width, player_height))

def draw_enemy():
    pygame.draw.rect(screen, red, (enemy_x, enemy_y, enemy_width, enemy_height))

def display_score():
    score_text = font.render("Score: " + str(score), True, black)
    screen.blit(score_text, (10, 10))

def check_collision():
    if player_x + player_width >= enemy_x and player_x <= enemy_x + enemy_width:
        if player_y <= enemy_y + enemy_height and player_y + player_height >= enemy_y:
            return True
    return False

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x -= player_speed
            if event.key == pygame.K_RIGHT:
                player_x += player_speed

    screen.fill(white)

    enemy_y += enemy_speed
    if enemy_y > height:
        enemy_x = random.randint(0, width - enemy_width)
        enemy_y = -enemy_height
        score += 1
        enemy_speed += 0.1

    if check_collision():
        running = False

    draw_player()
    draw_enemy()
    display_score()

    pygame.display.flip()
    clock.tick(60)

# Game over message
game_over_text = font.render("Game Over", True, black)
screen.blit(game_over_text, (width // 2 - 100, height // 2 - 50))
pygame.display.flip()

# Wait for a few seconds before closing the window
pygame.time.wait(2000)

# Quit the game
pygame.quit()
