import random, sys, time, pygame
from homepage import Homepagehub
from pygame.locals import *

pygame.init()
fps = 60
window_width = 900
window_height = 800
flash_speed = 500  # in milliseconds
flash_delay = 200
button_size = 300
buttongap_size = 30
timeout = 10  # seconds before game over if no button is pushed.

white = (255, 255, 255)
black = (0, 0, 0)
bright_red = (255, 0, 0)
red = (155, 0, 0)
bright_green = (0, 255, 0)
green = (0, 155, 0)
bright_blue = (0, 0, 255)
blue = (0, 0, 155)
bright_yellow = (255, 255, 0)
yellow = (155, 155, 0)
gray = (40, 40, 40)
bg_color = black

x_margin = int((window_width - (2 * button_size) - buttongap_size) / 2)
y_margin = int((window_height - (2 * button_size) - buttongap_size) / 2)

# Rect objects for each of the four buttons

yellowrect = pygame.Rect(x_margin, y_margin, button_size, button_size)
bluerect = pygame.Rect(x_margin + button_size + buttongap_size, y_margin, button_size, button_size)
redrect = pygame.Rect(x_margin, y_margin + button_size + buttongap_size, button_size, button_size)
greenrect = pygame.Rect(x_margin + button_size + buttongap_size, y_margin + button_size + buttongap_size, button_size,
                        button_size)

run_game = False


def launch_homepagehub():
    global run_game
    run_game = True


def memory_palace():
    global fpsclock, displaysurf, basicfont, beep1, beep2, beep3, beep4, run_game

    pygame.init()
    fpsclock = pygame.time.Clock()
    displaysurf = pygame.display.set_mode((window_width, window_height))

    pygame.display.set_caption('memory palace')
    basicfont = pygame.font.Font('lato-italic.ttf', 22)
    basicfont2 = pygame.font.Font('lato-italic.ttf', 30)
    infoSurf = basicfont.render('Match the pattern by clicking on the button or using the Q, W, A, S keys.', True,
                                white)
    infoRect = infoSurf.get_rect()
    infoRect.topleft = (0, 0)

    # load the sound files

    beep1 = pygame.mixer.Sound('beep1.ogg')
    beep2 = pygame.mixer.Sound('beep2.ogg')
    beep3 = pygame.mixer.Sound('beep3.ogg')
    beep4 = pygame.mixer.Sound('beep4.ogg')

    # Initialize some variables for a new game

    pattern = []  # stores the pattern of colors
    currentStep = 0  # the color the player must push next
    lastClickTime = 0  # timestamp of the player's last button push

    score = 0

    # when False, the pattern is playing. when True, waiting for the player to click a colored button:

    waitingForInput = False

    '''

    def return_button():
        exit_button = pygame.rect.Rect((0, 734), (900, 66))
        exit_button2 = pygame.draw.rect(displaysurf, (255, 255, 255), (exit_button))
        clicked = pygame.mouse.get_focused()
        font = pygame.font.Font('lato-italic.ttf', 30)
        return_text = font.render("return", True, (0, 0, 0))
        displaysurf.blit(return_text, (415, 734))
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if exit_button.collidepoint(mouse_pos[0], mouse_pos[1]):
                while True:
                    Homepagehub()
    '''

    while True:  # main game loop

        clickedButton = None  # button that was clicked (set to YELLOW, RED, GREEN, or BLUE)
        displaysurf.fill(bg_color)
        drawButtons()

        scoreSurf = basicfont2.render('Score: ' + str(score), True, white)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topleft = (window_width - 150, 10)
        displaysurf.blit(scoreSurf, scoreRect)
        displaysurf.blit(infoSurf, infoRect)

        # exit_button = pygame.rect.Rect((0, 734), (900, 66))
        # pygame.draw.rect(displaysurf, (255, 255, 255), (exit_button))
        # font = pygame.font.Font('lato-italic.ttf', 30)
        # return_text = font.render("return", True, (0, 0, 0))
        # displaysurf.blit(return_text, (415, 734))

        checkForQuit()

        for event in pygame.event.get():  # event handling loop

            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                clickedButton = getButtonClicked(mousex, mousey)

 
            # if event.type == pygame.MOUSEBUTTONDOWN:
            # mouse_pos = pygame.mouse.get_pos()
            # if exit_button.collidepoint(mouse_pos[0], mouse_pos[1]):
            #   launch_homepagehub()

            elif event.type == KEYDOWN:
                if event.key == K_q:
                    clickedButton = yellow
                elif event.key == K_w:
                    clickedButton = blue
                elif event.key == K_a:
                    clickedButton = red
                elif event.key == K_s:
                    clickedButton = green

        if not waitingForInput:

            # play the pattern
            pygame.display.flip()
            pygame.time.wait(1000)
            pattern.append(random.choice((yellow, blue, red, green)))

            for button in pattern:
                flashButtonAnimation(button)
                pygame.time.wait(flash_delay)

            waitingForInput = True

        else:

            # wait for the player to enter buttons

            if clickedButton and clickedButton == pattern[currentStep]:
                # pushed the correct button
                flashButtonAnimation(clickedButton)
                currentStep += 1
                lastClickTime = time.time()

                if currentStep == len(pattern):
                    # pushed the last button in the pattern
                    changeBackgroundAnimation()
                    score += 1
                    waitingForInput = False
                    currentStep = 0  # reset back to first step

                    score2 = score * 100
                    file = open('high_scores.txt', 'a')
                    file.write(f'\n{score2}')
                    file.close()

                    memory_score()





            elif (clickedButton and clickedButton != pattern[currentStep]) or (
                    currentStep != 0 and time.time() - timeout > lastClickTime):
                # pushed the incorrect button, or has timed out
                gameOverAnimation()
                # reset the variables for a new game:
                pattern = []
                currentStep = 0
                waitingForInput = False
                score = 0
                pygame.time.wait(1000)
                changeBackgroundAnimation()

        if run_game:
            import homepage  # Import the duckhuntgame module here
            homepage.Homepagehub()  # Call the duck_hunt_game function from the module
            run_game = False

        pygame.display.update()

        fpsclock.tick(fps)


def terminate():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Homepagehub()
            pygame.quit()
            sys.exit()


def memory_score():
    file = open('high_scores.txt', 'r')
    read_file = file.readlines()
    file.close()
    memory_score = int(read_file[-1])


def checkForQuit():
    global event
    for event in pygame.event.get(QUIT):  # get all the QUIT events
        # Homepagehub()
        pygame.quit()
        sys.exit()
    # terminate if any QUIT events are present

    for event in pygame.event.get(KEYUP):  # get all the KEYUP events
        if event.key == K_ESCAPE:
            pygame.quit()  # terminate if the KEYUP event was for the Esc key

        pygame.event.post(event)  # put the other KEYUP event objects back


def flashButtonAnimation(color, animationSpeed=50):
    global sound, flashColor, rectangle
    if color == yellow:
        sound = beep1
        flashColor = bright_yellow
        rectangle = yellowrect

    elif color == blue:
        sound = beep2
        flashColor = bright_blue
        rectangle = bluerect

    elif color == red:
        sound = beep3
        flashColor = bright_red
        rectangle = redrect

    elif color == green:
        sound = beep4
        flashColor = bright_green
        rectangle = greenrect

    origSurf = displaysurf.copy()
    flashSurf = pygame.Surface((button_size, button_size))
    flashSurf = flashSurf.convert_alpha()
    r, g, b = flashColor
    sound.play()

    for start, end, step in ((0, 255, 1), (255, 0, -1)):  # animation loop
        for alpha in range(start, end, animationSpeed * step):
            checkForQuit()
            displaysurf.blit(origSurf, (0, 0))
            flashSurf.fill((r, g, b, alpha))
            displaysurf.blit(flashSurf, rectangle.topleft)
            pygame.display.update()
            fpsclock.tick(fps)

    displaysurf.blit(origSurf, (0, 0))


def drawButtons():
    pygame.draw.rect(displaysurf, yellow, yellowrect)
    pygame.draw.rect(displaysurf, blue, bluerect)
    pygame.draw.rect(displaysurf, red, redrect)
    pygame.draw.rect(displaysurf, green, greenrect)


def changeBackgroundAnimation(animationSpeed=40):
    global bg_color
    newBgColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    newBgSurf = pygame.Surface((window_width, window_height))
    newBgSurf = newBgSurf.convert_alpha()
    r, g, b = newBgColor

    for alpha in range(0, 255, animationSpeed):  # animation loop

        checkForQuit()
        displaysurf.fill(bg_color)
        newBgSurf.fill((r, g, b, alpha))
        displaysurf.blit(newBgSurf, (0, 0))
        drawButtons()  # redraw the buttons on top of the tint
        pygame.display.flip()
        fpsclock.tick(fps)

    bg_color = newBgColor


def gameOverAnimation(color=white, animationSpeed=50):
    origSurf = displaysurf.copy()
    flashSurf = pygame.Surface(displaysurf.get_size())
    flashSurf = flashSurf.convert_alpha()
    beep1.play()
    beep2.play()
    beep3.play()
    beep4.play()
    r, g, b = color
    for i in range(3):  # do the flash 3 times
        for start, end, step in ((0, 255, 1), (255, 0, -1)):
            # The first iteration in this loop sets the following for loop
            # to go from 0 to 255, the second from 255 to 0.
            for alpha in range(start, end, animationSpeed * step):  # animation loop
                # alpha means transparency. 255 is opaque, 0 is invisible
                checkForQuit()
                flashSurf.fill((r, g, b, alpha))
                displaysurf.blit(origSurf, (0, 0))
                displaysurf.blit(flashSurf, (0, 0))
                drawButtons()
                pygame.display.flip()
                fpsclock.tick(fps)


def getButtonClicked(x, y):
    if yellowrect.collidepoint((x, y)):
        return yellow

    elif bluerect.collidepoint((x, y)):
        return blue

    elif redrect.collidepoint((x, y)):
        return red

    elif greenrect.collidepoint((x, y)):
        return green

    return None


if __name__ == '__main__':
    memory_palace()
