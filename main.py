import pygame, time
from homepage import Homepagehub

logo = pygame.image.load(f'time2relax.jpg')
logo = pygame.transform.scale(logo, (210, 100))


class InputBox():

    def __init__(self, x, y):
        self.font = pygame.font.Font(None, 45)
        self.inputBox = pygame.Rect(x, y, 200, 50)
        self.colourInactive = pygame.Color('lightskyblue3')
        self.colourActive = pygame.Color('black')
        self.colour = self.colourInactive
        self.text = ''
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.inputBox.collidepoint(event.pos)
            self.colour = self.colourActive if self.active else self.colourInactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    return self.text
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def draw(self, screen):
        txtSurface = self.font.render(self.text, True, self.colour)
        width = max(200, txtSurface.get_width() + 10)
        self.inputBox.w = width
        screen.blit(txtSurface, (self.inputBox.x + 5, self.inputBox.y + 5))
        pygame.draw.rect(screen, self.colour, self.inputBox, 2)


def mainloop():
    global login_button
    pygame.init()
    window_size = (900, 800)
    screen = pygame.display.set_mode(window_size)
    clock = pygame.time.Clock()

    # Create objects
    input1 = InputBox(410, 430)
    input2 = InputBox(410, 340)

    title_font = pygame.font.SysFont('lato-italic.ttf', 70)
    font = pygame.font.Font('lato-italic.ttf', 30)
    title_text = title_font.render("time to relax", True, (255, 255, 255))

    title_x = 0
    title_y = 175
    title_velocity = 2

    username_text = []
    password_text = []  # List to store user input

    username_text1 = False
    password_text1 = False

    login_error_message = ""
    login_error_start_time = 0
    login_error_duration = 5

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if username_text1 == True and password_text1 == True:
                    if login_button.collidepoint(mouse_pos):
                        running = True
                        while running:
                            Homepagehub()
                            if event.type == pygame.QUIT:
                                Homepagehub()
                                pygame.quit()
                if username_text1 == False and password_text1 == False:
                    if login_button.collidepoint(mouse_pos):
                        login_error_message = "please enter a username and password"
                        login_error_start_time = time.time()

            # Handle every event

            text1 = input1.handle_event(event)
            text2 = input2.handle_event(event)
            if text1 is not None:
                username_text.append(text1)
                username_text1 = True
            if text2 is not None:
                password_text.append(text2)
                password_text1 = True

            file = open("user_details", "w")
            username_str = ",".join(username_text)
            password_str = ",".join(password_text)

            file.write(f'{password_str}\n{username_str}')
            file.close()

        screen.fill((13, 103, 181))

        # Update the position of the title text
        title_x += title_velocity
        if title_x > window_size[0] - title_text.get_width() or title_x < 0:
            title_velocity = -title_velocity

        # Draw the title text
        screen.blit(title_text, (title_x, title_y))

        text_user = font.render("Username:", True, (0, 0, 0))
        screen.blit(text_user, (246, 346))

        text_password = font.render("Password:", True, (0, 0, 0))
        screen.blit(text_password, (246, 430))

        login_button = pygame.draw.rect(screen, (13, 103, 181), (410, 518, 100, 50))
        text = font.render("Login", True, (0, 0, 0))
        screen.blit(text, (410, 518))

        border = pygame.draw.rect(screen, (102, 163, 187), (1, 723, 900, 100))
        border2 = pygame.draw.rect(screen, (102, 163, 187), (0, 0, 900, 100))

        screen.blit(logo, (363, 0))

        # Draw input boxes
        input1.draw(screen)
        input2.draw(screen)

        if login_error_message:
            elapsed_time = time.time() - login_error_start_time
            if elapsed_time < login_error_duration:
                login_error = font.render(login_error_message, True, (0, 0, 0))
                screen.blit(login_error, (246, 619))

        pygame.display.flip()
        clock.tick(60)


# Run the main loop
if __name__ == "__main__":
    mainloop()
