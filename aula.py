import pygame
from pygame.locals import*
from sys import exit

pygame.init

largura = 680 
altura = 480 
x = largura / 2
y = 0
relogio = pygame.time.Clock()

tela = pygame.display.set_mode((largura,altura))

while True:
    relogio.tick(30)
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.draw.rect(tela ,(255,0,0),(x,y,40,50))
    if y >= altura:
        y = 0
    y = y + 1
    pygame.display.update()

