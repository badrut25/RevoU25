import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Chess Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Board constants
ROWS = 8
COLS = 8
SQUARE_SIZE = screen_width // COLS

# Create the chess board
board = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"],
]

# Selected piece variables
selected_piece = None
selected_piece_pos = None

# Function to draw the chess board
def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            piece = board[row][col]
            if piece:
                shape_color = GREEN if piece.islower() else BLACK
                radius = SQUARE_SIZE // 2 - 10
                shape_center = (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2)
                pygame.draw.circle(screen, shape_color, shape_center, radius)
    
    # Highlight selected piece
    if selected_piece_pos:
        row, col = selected_piece_pos
        pygame.draw.circle(screen, RED, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), radius, 5)

# Function to get the chessboard coordinates from mouse position
def get_coordinates(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                row, col = get_coordinates(pos)
                if selected_piece:
                    # Move the selected piece to the new position
                    board[row][col] = selected_piece
                    selected_piece = None
                    selected_piece_pos = None
                else:
                    # Select the piece at the clicked position
                    piece = board[row][col]
                    if piece:
                        selected_piece = piece
                        selected_piece_pos = (row, col)

    # Draw the board
    draw_board()

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
