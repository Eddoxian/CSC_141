import pygame
from birb import Bird
from pipe import Pipes
from menu import main_menu, game_over_menu
from configs import WIDTH, HEIGHT, FPS

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    running = main_menu(screen)
    if not running:
        return

    while True:
        bird = Bird(60, HEIGHT // 2)
        pipes = []
        spawn_timer = 0
        score = 0
        game_over = False

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    bird.flap()

            #Creates Pipes
            spawn_timer += 1
            if spawn_timer > 90:
                pipes.append(PipePair(WIDTH))
                spawn_timer = 0

            bird.update()
            for pipe in pipes:
                pipe.update()

                if bird.rect.colliderect(pipe.top) or bird.rect.colliderect(pipe.bottom):
                    if not pipe.broken:
                        pipe.break_pipe()
                        score += 1
                    else:
                        game_over = True

                if bird.rect.top <= 0 or bird.rect.bottom >= HEIGHT:
                    game_over = True

            pipes = [p for p in pipes if p.top.right > 0]

            screen.fill((0, 0, 100))
            bird.draw(screen)
            for pipe in pipes:
                pipe.draw(screen)

            font = pygame.font.Font(None, 36)
            text = font.render(f"Score: {score}", True, (255, 255, 255))
            screen.blit(text, (10, 10))

            pygame.display.flip()
            clock.tick(FPS)

        restart = game_over_menu(screen, score)
        if not restart:
            break

if __name__ == "__main__":
    main()
