import pygame
from pygame import gfxdraw
from pygame.locals import *


def main():
    # Variables
    windowName = 'Lime project'
    screenSize = 800, 600
    test_color = 255, 255, 255
    test_pos = 50, 50
    mouse_x = 0
    mouse_y = 0

    mousePixelX = 0;
    mousePixelY = 0;

    max_FPS = 144
    brush_color = (255,255,255)
    brush_size = 1

    #Colors
    color_one = (255, 255, 255)
    color_two = (0, 0, 0)
    color_three = (255, 0, 0)
    color_four = (255, 255, 0)
    color_five = (255, 0, 255)
    color_six = (0, 255, 255)
    color_zero = (255, 255, 255)

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

    def inverted_rgb():
        color = RGB_mouse_color(800, 600)
        return color

    # Blit everything to the screen
    # screen.blit(background, (0, 0))
    # pygame.display.flip()

    #Rectangle
    def draw_box(x, y, width, height, surface, box_color):
        rectangle = pygame.Rect(x, y, width, height)
        pygame.gfxdraw.box(surface, rectangle, box_color)

    def draw_line(x, y, startX, startY, size):
        pygame.draw.aaline(background, brush_color,(x,y),(startX,startY), size)


    # Display some text
    font = pygame.font.Font(None, 30)
    text = font.render(str(pygame.display.get_driver()), 1, (255, 255, 255))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx

    # Event loop
    while 1:
        pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if pressed[pygame.K_x]:
                background.fill(RGB_mouse_color(800, 600))

            if pygame.mouse.get_pressed() == (1, 0, 0):
                print(pygame.mouse.get_pressed())
                # draw_box(mouse_x - brush_size, mouse_y - brush_size, brush_size, brush_size, background, brush_color)
                draw_line(mouse_x, mouse_y, mousePixelX, mousePixelY, brush_size)


            if pygame.mouse.get_pressed() == (0, 0, 1):
                mousePixelX = mouse_x
                mousePixelY = mouse_y
                pygame.draw.circle(background, brush_color, (mousePixelX, mousePixelY), brush_size, brush_size)

            if pressed[pygame.K_0]:
                print("0")
                brush_color = color_zero
            if pressed[pygame.K_1]:
                brush_color = color_one
            if pressed[pygame.K_2]:
                brush_color = color_two
            if pressed[pygame.K_3]:
                brush_color = color_three
            if pressed[pygame.K_4]:
                brush_color = color_four
            if pressed[pygame.K_5]:
                brush_color = color_five

            if pressed[pygame.K_9]:
                brush_size +=1
                print(brush_size)
            if pressed[pygame.K_8]:
                if brush_size > 0:
                    brush_size -= 1
                    print(brush_size)

        mouse_x, mouse_y = pygame.mouse.get_pos()
        screen.blit(background, (0, 0))
        pygame.display.flip()


if __name__ == '__main__':
    main()
