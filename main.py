import pygame
import sys
#from grid import Grid 
#from blocks import *
from game import Game
from colors import Colors

pygame.init()       # Day1
# dark_blue = (44,44,127)    # Day1

title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)

score_rect = pygame.Rect(320,55,170,60)
next_rect = pygame.Rect(320,215,170,180)

screen = pygame.display.set_mode((500,620))
pygame.display.set_caption("Python Tetris")

clock = pygame.time.Clock()

#game_grid = Grid()
#block = IBlock()
game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)  # move down every 200 m/s

#Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()                  # Day1
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
                game.update_score(0,1)
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()           
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()
        
    #Drawing
    score_value_surface = title_font.render(str(game.score), True, Colors.white)
    
    screen.fill(Colors.dark_blue)      # Day1
    screen.blit(score_surface, (365,20,50,50))
    screen.blit(next_surface, (375,180,50,50))
    
    if game.game_over == True:
        screen.blit(game_over_surface, (320,450, 50,50))
    
    #game_grid.draw(screen)
    #block.draw(screen)
    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    screen.blit(score_value_surface,score_value_surface.get_rect(centerx = score_rect.centerx,
        centery = score_rect.centery))
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
    game.draw(screen)         # Day1
    #game.move_down()
    
    pygame.display.update()   # Day1
    clock.tick(60)            # Day1  game speed



