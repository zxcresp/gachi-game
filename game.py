from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import time
from level1 import start_game
pygame.init()
screen = pygame.display.set_mode((1260, 680))
pygame.display.set_caption("GACHI")
font = pygame.font.SysFont('Arial', 30)
white = 255, 255, 255
black = 0, 0, 0
text1 = 'Привет, спасибо за установку моей игры) я так понимаю ты хочешь стать Dungeon Master?'
start_text = font.render(text1, 1, white, black)
background = pygame.image.load("back.jpg")
razrab_back = pygame.image.load("razrabl.jpg")
btnn_yes = pygame.image.load("btn_da.jpg")
btnn_no = pygame.image.load("btn_net.jpg")
btnn_ra = pygame.image.load("bnt_r.jpg")
btnn_o = pygame.image.load("btn_o.jpg")
pygame.mixer.music.load("backmusic2.mp3")
pygame.mixer.music.set_volume(0.040)
pygame.mixer.music.play(-1)
pygame.mixer.init()

close_button = pygame.Rect(150, 350, 200, 80)
start_button = pygame.Rect(900, 350, 200, 80)
razrab_button = pygame.Rect(490, 500, 200, 100)
ob_button = pygame.Rect(20, 500, 200, 100)


def wekd():
    screen.blit(razrab_back, (0, 0))
    pygame.draw.rect(screen, white, ob_button)
    screen.blit(btnn_o, (20, 500, 300, 100))

def render_screen():
    screen.blit(background, (0,0))
    screen.blit(start_text, (20, 150))
    pygame.draw.rect(screen, white, close_button)
    pygame.draw.rect(screen, white, start_button)
    pygame.draw.rect(screen, white, razrab_button)
    screen.blit(btnn_no, (150, 350))
    screen.blit(btnn_yes, (900, 350, 200, 80))
    screen.blit(btnn_ra, (490, 500, 300, 100))

running = True
menu = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
           if close_button.collidepoint(event.pos):
               pygame.mixer.music.load("slaves.wav")
               pygame.mixer.music.play()
               time.sleep(5.5)
               running = False
           elif start_button.collidepoint(event.pos):
               pygame.mixer.music.load("go.wav")
               pygame.mixer.music.play()
               start_game()
               #running = False
               screen = pygame.display.set_mode((1260, 680))
           if razrab_button.collidepoint(event.pos):
               menu = False
               #screen.blit(razrab_back, (0,0))
           if ob_button.collidepoint(event.pos):
               menu = True
               
    if menu:
        render_screen()
    else:
        wekd()
    pygame.display.update()

