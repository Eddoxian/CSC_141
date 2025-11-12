import pygame
import random
from configs import HEIGHT, PIPE_GAP, PIPE_SPEED

class PipePair:
    def __init__(self, x):
        self.width = 52
        self.gap_y = random.randint(100, HEIGHT - 200)
        self.passed = False
        self.broken = False

        self.top = pygame.Rect(x, 0, self.width, self.gap_y)
        self.bottom = pygame.Rect(x, self.gap_y + PIPE_GAP, self.width, HEIGHT - (self.gap_y + PIPE_GAP))

    def update(self):
        self.top.x -= PIPE_SPEED
        self.bottom.x -= PIPE_SPEED

    def draw(self, screen):
        color = (0, 255, 0) if not self.broken else (150, 150, 150)
        pygame.draw.rect(screen, color, self.top)
        pygame.draw.rect(screen, color, self.bottom)

    def break_pipe(self):
        self.broken = True
