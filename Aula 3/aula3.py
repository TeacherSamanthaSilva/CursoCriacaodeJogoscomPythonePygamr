import pygame #importar a biblioteca pygame

def main(): #as definições dos objetos
    pygame.init()
    tela = pygame.display.set_mode([300,300]) #cria a tela
    pygame.display.set_caption("Iniciando com Python")
    pygame.QUIT #comando para fechar a tela
    sair = False
    relogio = pygame.time.Clock()
    sup = pygame.Surface((200,200))

    while sair != True:
        for event in pygame.event.get(): #captura um evento
            if event.type == pygame.QUIT:
                sair = True
            relogio.tick(27) #numero de frames por segundo
            tela.fill((255,255,255))
            tela.blit(sup) #chamando superficie

    pygame.display.update()
    pygame.QUIT

main()