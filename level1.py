import pygame
import random
import time
def start_game():
    pygame.init()
    WIDTH = 1500
    HEIGHT = 880
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("GACHI")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('Arial', 30)
    white = 255, 255, 255
    black = 0, 0, 0
    start_text = font.render('Ты выбрал правильный путь, начинай убивать этих slaves', 1, white, black)
    gameover_text = font.render('Как ты мог проиграть этим SLAVES, не быть тебе Dungeon Master...', 1, black, white)
    pygame.mixer.init()
    player_image = pygame.image.load("master.png")
    mob_image = pygame.image.load("fslave.png")
    bullet_image = pygame.image.load("bullet.png")
    background = pygame.transform.scale(pygame.image.load("back2.jpg"), (1500, 880))
    pygame.mixer.music.load("bgmusic.wav")
    pygame.mixer.music.set_volume(0.040)
    pygame.mixer.music.play(-1)
    #hit_sound = mixer.Sound('')
    FPS = 60
    gameover = False


    class Player(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = player_image
            self.rect = self.image.get_rect()
            self.rect.centerx = 0
            self.rect.bottom = HEIGHT - 10
            self.speedx = 0
            self.speedy = 0
        def shoot(self):
            bullet = Bullet(self.rect.right, self.rect.centery+55)
            bullets.add(bullet)

        def update(self):
            self.speedx = 0
            self.speedy = 0
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_a]:
                self.speedx = -10
            if keystate[pygame.K_d]:
                self.speedx = 10
            if keystate[pygame.K_w]:
                self.speedy = -10
            if keystate[pygame.K_s]:
                self.speedy = 10
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.top > HEIGHT:
                self.rect.top = HEIGHT
            if self.rect.bottom < 0:
                self.rect.bottom = 0

    class Mob(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = mob_image
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(700)
            self.speedx = random.randrange(-2, 2)

        def update(self):
            self.rect.x += self.speedx
            if self.rect.top > HEIGHT + 10 or self.rect.right > WIDTH + 20:
                self.rect.x = random.randrange(WIDTH - self.rect.width)
                self.rect.y = random.randrange(700)

    class Bullet(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = bullet_image
            self.rect = self.image.get_rect()
            self.rect.bottom = y
            self.rect.centerx = x
            self.speedx = 10

        def update(self):
            self.rect.x += self.speedx
            if self.rect.left > WIDTH:
                self.kill()

    all_sprites = pygame.sprite.Group()
    mobs = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)
    for i in range(7):
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

    running = True
    game = True
    while running and game:
        for event in pygame.event.get():
            clock.tick(FPS)
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()
        screen.blit(background, (0,0))
        screen.blit(start_text, (400, 100))
        all_sprites.update()
        hits = pygame.sprite.spritecollide(player, mobs, False)
        if hits:
            gameover = True
        hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
        for hit in hits:
            m = Mob()
            all_sprites.add(m)
            mobs.add(m)

        if gameover == True:
            screen.fill(black)
            screen.blit(gameover_text, (400, 100))
            running = False
            time.sleep(3)

        all_sprites.draw(screen)
        bullets.draw(screen)
        bullets.update()
        pygame.display.update()
    #pygame.quit()