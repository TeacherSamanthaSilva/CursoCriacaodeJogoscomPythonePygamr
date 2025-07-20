import pygame #importa biblioteca pygame

display = pygame.display.set_mode((1280,720)) #retorna uma tela com uma determinada dimensão largura e altura

player1 = pygame.Rect(0,0,30,150) #desenha um retângulo na tela
player2 = pygame.Rect(1250,0,30,150) #desenha um retângulo na tela
player1_speed = 1
player2_speed = 1
ball_dir_x = 1
ball_dir_y = 1

ball = pygame.Rect(600,350,15,15) 

loop = True #todo jogo fica dentro de um loop

while loop:

    for event in pygame.event.get(): #verifica os tipos de eventos
        if event.type == pygame.QUIT:  #verifica se é um evento de saída
            loop = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1_speed = 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                player1_speed = -1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
               player2_speed = 1


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
             player2_speed = -1

        if player1.y <= 0:
            player1.y = 0
        
        if player1.y >= 720 - 150:
            player1.y = 720 - 150

        if player2.y <= 0:
            player2.y = 0
        
        if player2.y >= 720 - 150:
            player2.y = 720 - 150

    player1.y += player1_speed
    player2.y += player2_speed

    if ball.x <= 0:
        ball.x = 600
      
    
    if ball.x >= 1280:
        ball.x = 600
    
    if ball.y <= 0:
        ball_dir_y *= -1
    
    if ball.y >= 720 - 15:
        ball_dir_y *= 1
      
    ball.x = ball_dir_x
    ball.y = ball_dir_y


    display.fill((0,0,0)) #define a cor da tela usando padrão RGB
    pygame.draw.rect(display, "white", player1)
    pygame.draw.rect(display, "white", player2)
    pygame.draw.rect(display,"white" , ball)
    pygame.display.flip() #define que a tela vai ficar sempre atualizando