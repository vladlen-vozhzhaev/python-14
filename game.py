import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((1600, 900))
plane = pygame.image.load('img/plane.png')
plane = pygame.transform.scale(plane, (200, 75))
plane_x = 0
plane_y = 20
plane = pygame.transform.rotate(plane, +20)
plane_transform = True
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if plane_y != 400-75:
        plane_y += 1
    elif plane_transform:
        plane = pygame.transform.rotate(plane, -20)
        plane_transform = False

    if plane_x != 800-200:
        plane_x += 1
    screen.fill((0,0,0))
    screen.blit(plane, (plane_x, plane_y))
    pygame.draw.line(screen, (0, 255, 0), [0, 400], [1600, 400], 3)
    pygame.draw.line(screen, (0, 255, 0), [800, 380], [800, 420], 3)
    pygame.display.flip()
    clock.tick(60)