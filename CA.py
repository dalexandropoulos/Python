import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the title
pygame.display.set_caption("Star Travel Screensaver")

# Star class
class Star:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.size = random.randint(1, 4)
        self.speed = random.uniform(0.5, 2)
        self.pulse_speed = random.uniform(0.01, 0.05)
        self.pulse_direction = 1

    def update(self):
        self.y += self.speed
        self.size += self.pulse_speed * self.pulse_direction

        if self.size >= 4 or self.size <= 1:
            self.pulse_direction *= -1

        if self.y > HEIGHT:
            self.y = 0
            self.x = random.randint(0, WIDTH)

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (int(self.x), int(self.y)), int(self.size))

# Create a list of stars
stars = [Star() for _ in range(200)]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    for star in stars:
        star.update()
        star.draw(screen)

    pygame.display.flip()
    pygame.time.delay(10)

pygame.quit()