import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 900, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Paint Application")
fps = 60
timer = pygame.time.Clock()

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Set up the drawing variables
draw_colour = black
draw_size = 3
drawing = False
last_pos = None

active_size = 0
active_colour = 'black'
painting = []


def draw_selection():
    global draw_colour, draw_size, drawing
    paint_menu = pygame.image.load('paint.png')
    screen.blit(paint_menu, (0, 0))
    blackrect = pygame.rect.Rect(511, 0, 130, 67)
    whiterect = pygame.rect.Rect(511, 66, 130, 66)
    greenrect = pygame.rect.Rect(641, 0, 130, 67)
    redrect = pygame.rect.Rect(641, 66, 130, 66)
    yellowrect = pygame.rect.Rect(770, 0, 130, 67)
    bluerect = pygame.rect.Rect(770, 66, 130, 66)
    colorlist = [blackrect, whiterect, greenrect, redrect, yellowrect, bluerect]

    brush_l = pygame.rect.Rect(281, 11, 50, 50)
    brush_m = pygame.rect.Rect(376, 11, 50, 50)
    brush_s = pygame.rect.Rect(281, 69, 50, 50)
    brush_xs = pygame.rect.Rect(376, 69, 50, 50)

    brushlist = [brush_l, brush_m, brush_s, brush_xs]
    rgb_list = [(0, 0, 0), (255, 255, 255), (0, 255, 0), (255, 0, 0), (255, 255, 0), (0, 0, 255)]

    return colorlist, brushlist, rgb_list

    # for event in pygame.event.get():
    #   if event.type == pygame.MOUSEBUTTONDOWN:
    #      if event.button == 1:  # Left mouse button
    #         drawing = True
    #    mouse_pos = pygame.mouse.get_pos()
    #   if blackrect.collidepoint(mouse_pos[0], mouse_pos[1]):
    #      pass
    #      #launch_duckhuntgame()
    # if whiterect.collidepoint(mouse_pos[0], mouse_pos[1]):
    #     draw_color = white
    # if greenrect.collidepoint(mouse_pos[0], mouse_pos[1]):
    #   draw_color = green


def draw_painting(paints):
    for i in range(len(paints)):
        pygame.draw.circle(screen, paints[i][0], paints[i][1], paints[i][2])


def paint_game():
    # Game loop
    global active_colour, active_size
    running = True
    while running:
        timer.tick(fps*10)
        screen.fill(black)
        color, brush, rgb = draw_selection()
        mouse = pygame.mouse.get_pos()
        left = pygame.mouse.get_pressed()[0]
        if mouse[1] > 132:
            pygame.draw.circle(screen, active_colour, mouse, active_size)
        if left and mouse[1] > 132:
            painting.append((active_colour, mouse, active_size))
        draw_painting(painting)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:

                for i in range(len(brush)):
                    if brush[i].collidepoint(event.pos):
                        active_size = 20 - (i * 5)

                for i in range(len(color)):
                    if color[i].collidepoint(event.pos):
                        active_colour = rgb[i]

        # Update the display
        pygame.display.flip()


if __name__ == '__main__':
    paint_game()

# Quit the program
# pygame.quit()
