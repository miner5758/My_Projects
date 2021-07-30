import pygame as py
import time
import random


py.init()

dis_Width = 800
dis_Height = 600
dis=py.display.set_mode((dis_Width,dis_Height))

py.display.set_caption('Zenake')

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0,0,255)
red = (255,0,0)
green = (0, 255, 0)
yellow = (255, 255, 102)
dark_red = (165, 42, 42)
purple = (197, 139, 231)
snake_block = 10
font_style = py.font.SysFont('bahnschrift',30)
score_style = py.font.SysFont('bahnschrift',35)
clock = py.time.Clock()

def your_score(score):
    value = score_style.render('Your score: ' + str(score),True,green)
    dis.blit(value, [0,0])

def our_sneke(snake_block, snake_list):
    for x in snake_list:
        py.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
        

def message(msg,color):
    mesg = font_style.render(msg,True,color)
    dis.blit(mesg,[dis_Width/6, dis_Height/3])
    
    
def game_loop():
    game_over = False
    game_close = False
    snake_speed = 15

    x1 = dis_Width / 2
    y1 = dis_Height / 2
    
    x1_change = 0
    y1_change = 0
    
    snake_list = []
    length_of_snake = 1
    
    foodx = round(random.randrange(0, dis_Width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_Height - snake_block) / 10.0) * 10.0
    
    while not game_over:
        
        while game_close == True:
            dis.fill(black)
            message('Game over, Press Q-Quit or C-Play Again',dark_red)
            py.display.update()
            for event in py.event.get():
                if event.type == py.KEYDOWN:
                    if event.key == py.K_q:
                        game_over = True
                        game_close = False
                    if event.key == py.K_c:
                        game_loop()
                        
        for event in py.event.get():
            if event.type == py.QUIT:
                game_over = True
            if event.type == py.KEYDOWN:
                if event.key == py.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == py.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == py.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == py.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_Width or x1 < 0 or y1 >= dis_Height or y1 < 0:
            game_close = True
    
        x1 += x1_change
        y1 += y1_change
        dis.fill(purple)
        py.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_sneke(snake_block,snake_list)
        your_score(length_of_snake - 1)
        py.display.update()
    
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0,dis_Width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0,dis_Height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
            snake_speed = snake_speed + 3
        clock.tick(snake_speed)

    py.quit()
    
game_loop()