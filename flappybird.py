""" A unique flappy bird game that I built in Python that includes
a scoring system, unique graphics, and sound effects. """

import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 600
FPS = 30
GRAVITY = 0.5
BIRD_JUMP = 10
PIPE_WIDTH = 50
PIPE_HEIGHT = 300
PIPE_GAP = 150

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game variables
bird_x = 50
bird_y = HEIGHT // 2
bird_velocity = 0
pipes = []
score = 0

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Unique Flappy Bird")

# Load images and sounds
bird_image = pygame.image.load("unique_bird.png")
pipe_image = pygame.image.load("unique_pipe.png")
background_image = pygame.image.load("unique_background.jpg")
ground_image = pygame.image.load("unique_ground.jpg")
flap_sound = pygame.mixer.Sound("flap_sound.wav")
hit_sound = pygame.mixer.Sound("hit_sound.wav")

# Resize images
bird_image = pygame.transform.scale(bird_image, (50, 50))
pipe_image = pygame.transform.scale(pipe_image, (PIPE_WIDTH, PIPE_HEIGHT))
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
ground_image = pygame.transform.scale(ground_image, (WIDTH, 100))

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Function to draw text on the screen
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird_velocity = -BIRD_JUMP
            flap_sound.play()

    # Update bird position and velocity
    bird_y += bird_velocity
    bird_velocity += GRAVITY

    # Generate pipes
    if random.randint(0, 10) == 0:
        pipe_height = random.randint(50, HEIGHT - 50 - PIPE_GAP)
        pipes.append([WIDTH, pipe_height])

    # Update pipe positions
    for pipe in pipes:
        pipe[0] -= 5

    # Remove off-screen pipes
    pipes = [pipe for pipe in pipes if pipe[0] > -PIPE_WIDTH]

    # Check for collisions
    for pipe in pipes:
        if (
            bird_x < pipe[0] + PIPE_WIDTH
            and bird_x + 50 > pipe[0]
            and (bird_y < pipe[1] or bird_y + 50 > pipe[1] + PIPE_GAP)
        ):
            hit_sound.play()
            pygame.quit()
            sys.exit()

    # Check for scoring
    for pipe in pipes:
        if pipe[0] == bird_x - PIPE_WIDTH:
            score += 1

    # Draw background
    screen.blit(background_image, (0, 0))

    # Draw pipes
    for pipe in pipes:
        screen.blit(pipe_image, (pipe[0], 0))
        screen.blit(pipe_image, (pipe[0], pipe[1] + PIPE_GAP))

    # Draw bird
    screen.blit(bird_image, (bird_x, bird_y))

    # Draw ground
    screen.blit(ground_image, (0, HEIGHT - 100))

    # Draw score
    font = pygame.font.Font(None, 36)
    draw_text(f"Score: {score}", font, WHITE, WIDTH // 2, 50)

    # Draw designer line
    font = pygame.font.Font(None, 24)
    draw_text("Designed by Prahlad", font, WHITE, WIDTH // 2, HEIGHT - 50)

    # Update display
    pygame.display.flip()

    # Control frame rate
    clock.tick(FPS)
