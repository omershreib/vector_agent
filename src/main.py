import pygame
from sys import exit
from settings import *
from game import GameManager

pygame.init()
pygame.mixer.init()

def event_listener(game_manager):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print('need to fire!')
            if not game_manager.is_cannon_empty:
                game_manager.is_fire = True

        if event.type == pygame.MOUSEBUTTONUP:
            game_manager.is_fire = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_q:  # exit the game
                pygame.quit()
                exit()

            if event.key == pygame.K_r:  # reload cannon
                game_manager.reload_cannon()

            if event.key == pygame.K_n:  # call invader wave before time
                game_manager.is_ready = True


def main():
    surface = pygame.display.set_mode(screen_size)
    print(f"screen size details:\nwidth: {screen_width}, height: {screen_height}")
    clock = pygame.time.Clock()

    pygame.display.set_caption('Vector Agent')
    game_manager = GameManager(surface)

    # game loop
    while True:
        event_listener(game_manager)
        surface.fill(COLOR_WHITE)

        game_manager.start()
        pygame.display.update()
        clock.tick(CLOCK_RATE)


if __name__ == '__main__':
    main()



