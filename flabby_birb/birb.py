import pygame
from configs import GRAVITY, FLAP_STRENGTH

class Bird:
    def __init__(self, x, y):
        self.image = pygame.Surface((34, 24), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 255), (17, 12), 12)
        self.rect = self.image.get_rect(center=(x, y))
        self.vel = 0

    def update(self):
        self.vel += GRAVITY
        self.rect.y += self.vel

    def flap(self):
        self.vel = FLAP_STRENGTH

    def draw(self, screen):
        screen.blit(self.image, self.rect)
