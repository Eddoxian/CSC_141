import pygame
from configs import WIDTH, HEIGHT

def draw_text(screen, text, size, color, y):
    font = pygame.font.Font(None, size)
    surf = font.render(text, True, color)
    rect = surf.get_rect(center=(WIDTH // 2, y))
    screen.blit(surf, rect)

def main_menu(screen):
    clock = pygame.time.Clock()
    while True:
        screen.fill((0, 0, 50))
        draw_text(screen, "Flappy Breaker", 48, (255, 255, 255), HEIGHT // 2 - 50)
        draw_text(screen, "Press SPACE to start", 32, (200, 200, 200), HEIGHT // 2 + 20)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return True

        clock.tick(30)

def game_over_menu(screen, score):
    clock = pygame.time.Clock()
    while True:
        screen.fill((50, 0, 0))
        draw_text(screen, "Game Over!", 48, (255, 255, 255), HEIGHT // 2 - 50)
        draw_text(screen, f"Score: {score}", 36, (200, 200, 200), HEIGHT // 2)
        draw_text(screen, "Press R to restart or ESC to quit", 24, (255, 255, 255), HEIGHT // 2 + 60)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                elif event.key == pygame.K_ESCAPE:
                    return False

        clock.tick(30)
