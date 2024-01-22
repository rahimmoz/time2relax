import pygame
from pygame import mixer
from fighter import Fighter

def fight_game():
    mixer.init()
    pygame.init()

    # Create game window
    width = 1000
    height = 600

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Fighting Game")

    # Set framerate
    clock = pygame.time.Clock()
    fps = 60

    # Define colors
    red = (255, 0, 0)
    yellow = (255, 255, 0)
    white = (255, 255, 255)


    intro_count = 3
    last_count_update = pygame.time.get_ticks()
    score = [0, 0]
    round_over = False
    round_over_cooldown = 2000

    warrior_size = 162
    warrior_scale = 4
    warrior_offset = [72, 56]
    warrior_char = [warrior_size, warrior_scale, warrior_offset]
    wizard_size = 250
    wizard_scale = 3
    wizard_offset = [112, 107]
    wizard_char = [wizard_size, wizard_scale, wizard_offset]

    # Load music and sounds
    pygame.mixer.music.load('assets/audio/music.mp3')
    pygame.mixer.music.set_volume(0.25)
    pygame.mixer.music.play(-1, 0.0, 5000)
    sword_fx = pygame.mixer.Sound('assets/audio/sword.wav')
    sword_fx.set_volume(0.3)
    magic_fx = pygame.mixer.Sound('assets/audio/magic.wav')
    magic_fx.set_volume(0.5)


    bg_image = pygame.image.load('assets/images/background/background.jpg').convert_alpha()

    warrior_sheet = pygame.image.load('assets/images/warrior/Sprites/warrior.png').convert_alpha()
    wizard_sheet = pygame.image.load('assets/images/wizard/Sprites/wizard.png').convert_alpha()


    victory_img = pygame.image.load('assets/images/icons/victory.png').convert_alpha()


    warrior_animation_steps = [10, 8, 1, 7, 7, 3, 7]
    wizard_animation_steps = [8, 8, 1, 8, 8, 3, 7]

    # Define font
    count_font = pygame.font.Font('assets/fonts/turok.ttf', 80)
    score_font = pygame.font.Font('assets/fonts/turok.ttf', 30)

    # Function for drawing text
    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    # Function for drawing background
    def draw_bg():
        scaled_bg = pygame.transform.scale(bg_image, (width, height))
        screen.blit(scaled_bg, (0, 0))

    # Function for drawing fighter health bars
    def draw_health_bar(health, x, y):
        ratio = health / 100
        pygame.draw.rect(screen, white, (x - 2, y - 2, 404, 34))
        pygame.draw.rect(screen, red, (x, y, 400, 30))
        pygame.draw.rect(screen, yellow, (x, y, 400 * ratio, 30))

    # Create two instances of fighters
    fighter_1 = Fighter(1, 200, 310, False, warrior_char, warrior_sheet, warrior_animation_steps, sword_fx)
    fighter_2 = Fighter(2, 700, 310, True, wizard_char, wizard_sheet, wizard_animation_steps, magic_fx)

    # Game loop
    run = True
    while run:
        clock.tick(fps)

        # Draw background
        draw_bg()

        # Show player stats
        draw_health_bar(fighter_1.health, 20, 20)
        draw_health_bar(fighter_2.health, 580, 20)
        draw_text("P1: " + str(score[0]), score_font, red, 20, 60)
        draw_text("P2: " + str(score[1]), score_font, red, 580, 60)

        # Update countdown
        if intro_count <= 0:
            # Move fighters
            fighter_1.move(width, height, screen, fighter_2, round_over)
            fighter_2.move(width, height, screen, fighter_1, round_over)
        else:
            # Display count timer
            draw_text(str(intro_count), count_font, red, width / 2, height / 3)
            # Update count timer
            if (pygame.time.get_ticks() - last_count_update) >= 1000:
                intro_count -= 1
                last_count_update = pygame.time.get_ticks()

        # Update fighters
        fighter_1.update()
        fighter_2.update()

        # Draw fighters
        fighter_1.draw(screen)
        fighter_2.draw(screen)

        # Check for player defeat
        if not round_over:
            if not fighter_1.alive:
                score[1] += 1
                round_over = True
                round_over_time = pygame.time.get_ticks()
            elif not fighter_2.alive:
                score[0] += 1
                round_over = True
                round_over_time = pygame.time.get_ticks()
        else:
            # Display victory image
            screen.blit(victory_img, (360, 150))
            if pygame.time.get_ticks() - round_over_time > round_over_cooldown:
                round_over = False
                intro_count = 3
                fighter_1 = Fighter(1, 200, 310, False, warrior_char, warrior_sheet, warrior_animation_steps, sword_fx)
                fighter_2 = Fighter(2, 700, 310, True, wizard_char, wizard_sheet, wizard_animation_steps, magic_fx)

        # Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Update display
        pygame.display.update()

    # Exit pygame
    pygame.quit()

if __name__ == '__main__':
    fight_game()
