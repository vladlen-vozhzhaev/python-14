import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SIZE = 40
PLAYER_SPEED = 5
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
WHITE = (255,255,255)
BLACK = (0,0,0)
RED   = (255,0,0)
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class Player(pygame.sprite.Sprite):
    def __init__(self, walls):
        super().__init__()
        self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (20,20)
        self.walls = walls
    def update(self, dx, dy):
        # Ограничение на диагональное перемещение
        if dx != 0 and dy != 0:
            dx = 0
            dy = 0
        new_x = self.rect.x + dx
        new_y = self.rect.y + dy
        # Проверка на выход за границы экрана
        if new_x < 0 or new_x > SCREEN_WIDTH - PLAYER_SIZE:
            new_x = self.rect.x
        elif new_y < 0 or new_y > SCREEN_HEIGHT - PLAYER_SIZE:
            new_y = self.rect.y
        self.rect.x = new_x
        self.rect.y = new_y
        collided_walls = pygame.sprite.spritecollide(self, self.walls, False)
        for wall in collided_walls:
            if dx > 0:
                self.rect.right = wall.rect.left
            if dx < 0:
                self.rect.left = wall.rect.right
            if dy > 0:
                self.rect.bottom = wall.rect.top
            if dy < 0:
                self.rect.top = wall.rect.bottom

wall1 = Wall(100, 100)
wall2 = Wall(400, 400)
walls = pygame.sprite.Group()
walls.add(wall1, wall2)
player = Player(walls)

all_sprites = pygame.sprite.Group()
all_sprites.add(player, walls)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    keys = pygame.key.get_pressed()
    dx, dy = 0,0
    if keys[pygame.K_LEFT]:
        dx = -PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        dx = PLAYER_SPEED
    if keys[pygame.K_UP]:
        dy = -PLAYER_SPEED
    if keys[pygame.K_DOWN]:
        dy = PLAYER_SPEED
    player.update(dx,dy)
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)