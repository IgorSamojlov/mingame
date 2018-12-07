import pygame
import game_m
import sys

def main():

    #game.hero_name = input("Whats your name? ")
    game = game_m.Game_m()


    while True:

            game.screen.fill(game.c_bal)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    game.m_keyd = 1
                    p = pygame.mouse.get_pos()

                    game.myhero.hero_shoot(game.bullets_group, p)

                if event.type == pygame.MOUSEBUTTONUP:
                    m_keyd = 0

            kd = pygame.key.get_pressed()
            if kd:
                game.myhero.move_hero(kd)

            game.draw_game()

main()
