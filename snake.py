# Larissa Motta Carrara
# Snake game
import pygame
import random


largura_tela = 795
altura_tela = 600

rodando = True
fps = 20

lado_quadrado = 15

velocidade = lado_quadrado
vel_x = velocidade
vel_y = 0

xq = (largura_tela // 2 // lado_quadrado) * lado_quadrado
yq = (altura_tela // 2 // lado_quadrado) * lado_quadrado

corpo = [(xq, yq)]

crescer = 0


def gerar_comida():
    while True:
        x = random.randrange(0, largura_tela, lado_quadrado)
        y = random.randrange(0, altura_tela, lado_quadrado)

        if (x, y) not in corpo:
            return (x, y)


xfood, yfood = gerar_comida()


def proc_eventos():
    global rodando, vel_x, vel_y

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP and vel_y == 0:
                vel_x = 0
                vel_y = -velocidade

            elif evento.key == pygame.K_DOWN and vel_y == 0:
                vel_x = 0
                vel_y = velocidade

            elif evento.key == pygame.K_LEFT and vel_x == 0:
                vel_x = -velocidade
                vel_y = 0

            elif evento.key == pygame.K_RIGHT and vel_x == 0:
                vel_x = velocidade
                vel_y = 0


def resetar_jogo():
    global xq, yq, corpo, crescer, vel_x, vel_y, xfood, yfood

    xq = (largura_tela // 2 // lado_quadrado) * lado_quadrado
    yq = (altura_tela // 2 // lado_quadrado) * lado_quadrado

    corpo = [(xq, yq)]
    crescer = 0
    vel_x = velocidade
    vel_y = 0
    xfood, yfood = gerar_comida()


def proc_colisoes():
    global crescer, xfood, yfood

    player_rect = pygame.Rect(xq, yq, lado_quadrado, lado_quadrado)
    food_rect = pygame.Rect(xfood, yfood, lado_quadrado, lado_quadrado)

    if player_rect.colliderect(food_rect):
        xfood, yfood = gerar_comida()
        crescer += 1


if __name__ == "__main__":
    pygame.init()
    tela = pygame.display.set_mode((largura_tela, altura_tela))
    relogio = pygame.time.Clock()

    while rodando:
        pygame.display.set_caption(f"Snake | Pontos: {len(corpo) - 1}")
        proc_eventos()

        
        next_x = xq + vel_x
        next_y = yq + vel_y

       # colisão com a borda
        if (
            next_x < 0 or
            next_x >= largura_tela or
            next_y < 0 or
            next_y >= altura_tela
        ):
            resetar_jogo()
            continue

        # colisão com o próprio corpo
        if (next_x, next_y) in corpo:
            resetar_jogo()
            continue

        
        xq = next_x
        yq = next_y

        proc_colisoes()

        corpo.insert(0, (xq, yq))

        if crescer > 0:
            crescer -= 1
        else:
            corpo.pop()

        tela.fill("#5593AE")

        
        for parte in corpo:
            x, y = parte
            pygame.draw.rect(tela, "#FF0000", (x, y, lado_quadrado, lado_quadrado))
            pygame.draw.rect(tela, "#000000", (x, y, lado_quadrado, lado_quadrado), 2)

        # comida
        pygame.draw.rect(tela, "#00FF00", (xfood, yfood, lado_quadrado, lado_quadrado))

        pygame.display.flip()
        relogio.tick(fps)

    pygame.quit()