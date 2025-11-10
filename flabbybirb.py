import pygame
import sys
import random




pygame.init()




WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flabby Birb")




clock = pygame.time.Clock()
FPS = 60




WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BLUE = (0, 150, 255)
RED = (255, 80, 80)
GRAY = (120, 120, 120)
YELLOW = (255, 255, 0)




bird_x = 50
bird_y = HEIGHT // 2
bird_radius = 15
bird_velocity = 0
gravity = 0.5
flap_strength = -8




pipe_width = 60
pipe_gap = 150
pipe_speed = 3
pipes = []




def create_pipe():
    y = random.randint(100, HEIGHT - 200)
    top = pygame.Rect(WIDTH, 0, pipe_width, y)
    bottom = pygame.Rect(WIDTH, y + pipe_gap, pipe_width, HEIGHT - (y + pipe_gap))
    return {"top": top, "bottom": bottom, "broken": False, "fragments": []}




pipes.append(create_pipe())




#Enemy and Laser setup
enemies = []
lasers = []
enemy_timer = 0
enemy_spawn_interval = 180
laser_speed = 4
enemy_speed = 2




score = 0
font = pygame.font.SysFont(None, 48)




running = True
while running:
    clock.tick(FPS)
    screen.fill(BLUE)




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = flap_strength




    # Bird physics
    bird_velocity += gravity
    bird_y += bird_velocity




    # Make bird
    pygame.draw.circle(screen, WHITE, (bird_x, int(bird_y)), bird_radius)




    # Move pipes
    new_pipes = []
    for pipe in pipes:
        top = pipe["top"]
        bottom = pipe["bottom"]




        #Pipe speed
        top.x -= pipe_speed
        bottom.x -= pipe_speed




        #Pipe broken vs Not
        if pipe["broken"]:
            for frag in pipe["fragments"]:
                frag["rect"].x -= pipe_speed
                frag["rect"].y += frag["vel_y"]
                frag["vel_y"] += 0.3
                pygame.draw.rect(screen, GRAY, frag["rect"])
        else:
            pygame.draw.rect(screen, GREEN, top)
            pygame.draw.rect(screen, GREEN, bottom)




        #Break pipe code
        if not pipe["broken"]:
            if top.collidepoint(bird_x, bird_y) or bottom.collidepoint(bird_x, bird_y):
                pipe["broken"] = True
                score += 1




                impact_y = bird_y
                fragments = []
                if top.collidepoint(bird_x, bird_y):
                    y_split = impact_y
                    upper = pygame.Rect(top.x, top.y, top.width, y_split)
                    lower = pygame.Rect(top.x, y_split, top.width, top.bottom - y_split)
                    fragments.append({"rect": upper, "vel_y": -3})
                    fragments.append({"rect": lower, "vel_y": 3})
                else:
                    y_split = impact_y
                    upper = pygame.Rect(bottom.x, bottom.y, bottom.width, y_split - bottom.y)
                    lower = pygame.Rect(bottom.x, y_split, bottom.width, bottom.bottom - y_split)
                    fragments.append({"rect": upper, "vel_y": -3})
                    fragments.append({"rect": lower, "vel_y": 3})
                pipe["fragments"] = fragments


        #Pipe kill code
        if (not pipe["broken"]
            and top.right > bird_x - bird_radius
            and top.left < bird_x + bird_radius
            and top.bottom < bird_y < bottom.top):
            running = False




 
        if top.right > 0 or (pipe["broken"] and any(f["rect"].right > 0 for f in pipe["fragments"])):
            new_pipes.append(pipe)




    pipes = new_pipes




    if not pipes or pipes[-1]["top"].x < WIDTH - 200:
        pipes.append(create_pipe())


#Basic enemy code
    enemy_timer += 1
    if enemy_timer >= enemy_spawn_interval:
        enemy_timer = 0
        enemy_y = random.randint(50, HEIGHT - 100)
        enemies.append({
            "x": WIDTH + 40,
            "y": enemy_y,
            "cooldown": random.randint(60, 120)
        })




    new_enemies = []
    for enemy in enemies:
        enemy["x"] -= enemy_speed
        pygame.draw.rect(screen, RED, (enemy["x"], enemy["y"], 30, 20))  # enemy body




        # Enemy Laser shooting
        enemy["cooldown"] -= 1
        if enemy["cooldown"] <= 0:
            enemy["cooldown"] = random.randint(90, 150)
            lasers.append(pygame.Rect(enemy["x"], enemy["y"] + 10, 10, 4))  # shoot laser




        if enemy["x"] > -40:
            new_enemies.append(enemy)
    enemies = new_enemies




    #Laser Code
    new_lasers = []
    for laser in lasers:
        laser.x -= laser_speed
        pygame.draw.rect(screen, RED, laser)
        if laser.collidepoint(bird_x, bird_y):
            running = False
        if laser.right > 0:
            new_lasers.append(laser)
    lasers = new_lasers


    if bird_y - bird_radius < 0 or bird_y + bird_radius > HEIGHT:
        running = False




    #Score
    score_surface = font.render(str(score), True, WHITE)
    screen.blit(score_surface, (WIDTH // 2 - 10, 20))




    pygame.display.flip()

pygame.quit()
print(f"Game Over! Final Score: {score}")








