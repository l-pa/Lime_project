import pygame
from pygame import gfxdraw
from pygame.locals import *
import sys


def main():
    # Variables
    windowName = 'Lime project'
    screenSize = 800, 600
    test_color = 255, 255, 255
    test_pos = 50, 50
    mouse_x = 0
    mouse_y = 0
    max_FPS = 60

    # Initialise
    pygame.init()
    screen = pygame.display.set_mode(screenSize)
    pygame.display.set_caption(windowName)
    clock = pygame.time.Clock()
    clock.tick(max_FPS)

    # Fill background
    background = pygame.Surface(screen.get_size())

    def RGB_mouse_color(height, width):
        colorR, colorG = mouse_x, mouse_y
        colorR /= height / 255
        colorG /= width / 255
        colorB = (colorR + colorG) / 2
        background_color = colorB, colorG, colorR
        return background_color

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    #Rectangle
    def draw_box(x, y, width, height, surface, box_color):
        rectangle = pygame.Rect(x, y, width, height)
        pygame.gfxdraw.box(surface, rectangle, box_color)


    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                print('Click')

        mouse_x, mouse_y = pygame.mouse.get_pos()

        background.fill(RGB_mouse_color(800, 600))

        draw_box(mouse_x - 20, mouse_y - 20, 20, 20, background, test_color)

        screen.blit(background, (0, 0))
        pygame.display.flip()


if __name__ == '__main__':
    main()