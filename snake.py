import pygame, random
from pygame import*
from pygame.time import Clock

#Deixar a maçã no mesmo pixel que a cobra
def on_grid_random():
    x = random.randint(0, 590)
    y = random.randint(0, 590) 
    return (x // 10 * 10, y // 10 *10)

#Colisão da cobra com a maçã
def collision(c1, c2):
    return (c1[0] == c2[0] and c1[1] == c2[1])


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

#Tela
pygame.init()                               
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Snake")

#Skin da cobra
snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((0,255,0))

#Skin da maçã
apple_pos = on_grid_random()
apple = pygame.Surface((10,10))
apple.fill((255,0,0)) 


my_direction = LEFT

#Velocidade de movimentação da cobra
clock = pygame.time.Clock()

while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        
        if event.type == KEYDOWN:  # <-movimentação
            if event.key == K_UP:
                 my_direction = UP

            if event.key == K_DOWN:
                 my_direction = DOWN

            if event.key == K_LEFT:
                 my_direction = LEFT

            if event.key == K_RIGHT:
                 my_direction = RIGHT
            

    if collision (snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))     #Nova posição vai tomar a posição anterior(que a calda tinha antes)

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake [i-1][0], snake[i-1][1])  


    if my_direction == UP:        #<-Direções
        snake[0] = (snake[0][0], snake [0][1] - 10)

    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake [0][1] + 10)

    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake [0][1])

    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake [0][1])

    
    screen.fill((0,0,0))  #Mostrando a cobra e a maçã na tela
    screen.blit(apple, apple_pos)
    for pos in snake:
        screen.blit(snake_skin,pos)

    i = 1
    while i < len(snake):
        if collision (snake[0], snake[i]):
            pygame.quit()
        i += 1


    pygame.display.update()
