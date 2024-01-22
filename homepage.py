import pygame

pygame.init()

window_size = (900, 800)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("home page")

menu_img = pygame.image.load('HOMEPAGE.png')
screen.blit(menu_img, (0, 0))

clock = pygame.time.Clock()
number = 0
timer = 0
blit_interval = 30000
font = pygame.font.Font('lato-italic.ttf', 30)
font2 = pygame.font.Font('lato-italic.ttf', 40)
font3 = pygame.font.Font('lato-italic.ttf', 25)

run_game = False
run_game2 = False
run_game3 = False
run_game4 = False


def streak_counter():
    global number
    number += 1


def launch_duckhuntgame():
    global run_game
    run_game = True


def launch_memorypalace():
    global run_game2
    run_game2 = True

def launch_paint():
    global run_game3
    run_game3 = True

def launch_Fight_game():
    global run_game4
    run_game4 = True


def rank(text, numscore, size):
    file = open('user_details', 'r')
    read_file = file.readlines()
    file.close()
    username = read_file[0]
    username = username[:len(username) - 1]

    file = open('high_scores.txt', 'r')
    read_file = file.readlines()
    file.close()
    scores = [int(score.strip()) for score in read_file[:3]] + [int(read_file[-1].strip())]
    total_score = sum(scores)

    num1 = font3.render((text + f'{numscore}'), True, pygame.Color('white'))
    screen.blit(num1, (size))

    if total_score > 2400:
        numscore = total_score
        text = username
        pygame.draw.rect(screen, (9, 89, 160), (717,378,180,55))
        num1 = font3.render((text + ':' + f'{numscore}'), True, pygame.Color('white'))
        screen.blit(num1, (727, 396))
    elif total_score > 1872:
        numscore = total_score
        text = username
        pygame.draw.rect(screen, (9, 89, 160), (717,437,180,55))
        num1 = font3.render((text + ':' + f'{numscore}'), True, pygame.Color('white'))
        screen.blit(num1, (727, 443))
    elif total_score > 1136:
        numscore = total_score
        text = username
        pygame.draw.rect(screen, (9, 89, 160), (717, 494, 180, 55))
        num1 = font3.render((text + ':' + f'{numscore}'), True, pygame.Color('white'))
        screen.blit(num1, (727, 509))
    elif total_score > 750:
        numscore = total_score
        text = username
        pygame.draw.rect(screen, (9, 89, 160), (717, 555, 180, 55))
        num1 = font3.render((text + ':' + f'{numscore}'), True, pygame.Color('white'))
        screen.blit(num1, (727, 568))
    elif total_score > 444:
        numscore = total_score
        text = username
        pygame.draw.rect(screen, (9, 89, 160), (717, 619, 180, 55))
        num1 = font3.render((text + ':' + f'{numscore}'), True, pygame.Color('white'))
        screen.blit(num1, (727, 629))

def user_rank_title():
    file = open('high_scores.txt', 'r')
    read_file = file.readlines()
    file.close()
    scores = [int(score.strip()) for score in read_file[:3]] + [int(read_file[-1].strip())]
    total_score = sum(scores)
    if total_score < 500:
        rank_title = font3.render('newbie beginner', True, pygame.Color('white'))
        screen.blit(rank_title, (720, 714))
    elif 500 <= total_score < 1000:
        rank_title = font3.render('average gamer', True, pygame.Color('white'))
        screen.blit(rank_title, (720, 714))
    elif 1000 <= total_score < 1500:
        rank_title = font3.render('pro level boss', True, pygame.Color('white'))
        screen.blit(rank_title, (720, 714))
    elif 1500 <= total_score < 2000:
        rank_title = font3.render('gigachad', True, pygame.Color('white'))
        screen.blit(rank_title, (720, 714))
    elif 2000 <= total_score < 2500:
        rank_title = font3.render('limits surpassed', True, pygame.Color('white'))
        screen.blit(rank_title, (720, 714))
    elif 2500 <= total_score < 3000:
        rank_title = font3.render('lvl 100 mafia boss', True, pygame.Color('white'))
        screen.blit(rank_title, (720, 714))
    elif total_score >= 3000:
        rank_title = font3.render('...GOAT...', True, pygame.Color('white'))
        screen.blit(rank_title, (748, 714))

def Homepagehub():
    # Run the game loop
    global timer, run_game, run_game2, run_game3,run_game4
    running = True
    run = pygame.Rect(261, 385, 42, 42)  # creating invisible rectangles
    run2 = pygame.Rect(587, 385, 42, 42)
    run3 = pygame.Rect(261,687,42,42)
    run4 = pygame.Rect(587, 687, 42, 42)


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if run.collidepoint(mouse_pos[0], mouse_pos[1]):
                    launch_duckhuntgame()
                if run2.collidepoint(mouse_pos[0], mouse_pos[1]):
                    launch_memorypalace()
                if run3.collidepoint(mouse_pos[0], mouse_pos[1]):
                    launch_paint()
                if run4.collidepoint(mouse_pos[0], mouse_pos[1]):
                    launch_Fight_game()


        current_time = pygame.time.get_ticks()

        # Check if it's time to blit the number
        if current_time - timer >= blit_interval:
            streak_counter()
            timer = current_time

        pygame.draw.rect(screen, (0, 0, 0), run, 1)  # Draw the invisible rectangles
        pygame.draw.rect(screen, (0, 0, 0), run2, 1)

        screen.blit(menu_img, (0, 0))  # Clear the screen
        text_surface = font.render(str(number), True, pygame.Color('white'))
        text_rect = text_surface.get_rect(topleft=(767.03, 79.32))
        screen.blit(text_surface, text_rect)

        file = open('user_details', 'r')
        read_file = file.readlines()
        file.close()
        username = read_file[0]
        username = username[:len(username) - 1]

        usernametext = font2.render(username, True, pygame.Color('white'))
        screen.blit(usernametext, (245, 44))

        file = open('high_scores.txt', 'r')
        read_file = file.readlines()
        file.close()
        scores = [int(score.strip()) for score in read_file[:3]] + [int(read_file[-1].strip())]
        total_score = sum(scores)
        score = font.render(str(total_score), True, pygame.Color('white'))
        screen.blit(score, (763, 744))

        user_rank_title()

        rank('laserdude:', 2400, (727, 396))
        rank('rayyan:', 1872, (727, 450))
        rank('shazil:', 1136, (727, 509))
        rank('Goku:', 750, (727, 578))
        rank('rmoz:', 444, (727, 632))

        pygame.display.flip()
        clock.tick(60)

        if run_game:
            import duckhuntgame  # Import the duckhuntgame module here
            duckhuntgame.duck_hunt_game()  # Call the duck_hunt_game function from the module
            run_game = False
        if run_game2:
            import config  # Import the config module here
            config.memory_palace()  # Call the memory_palace function from the module
            run_game2 = False
        if run_game3:
            import paint # Import the config module here
            paint.paint_game()  # Call the paint function from the module
            run_game3 = False
        if run_game4:
            import Fight_game
            Fight_game.fight_game()  # Call the paint function from the module
            run_game4 = False

        if username == '':
            file = open('high_scores.txt', 'r')
            read_file = file.readlines()
            best_freeplay = read_file[0]
            best_ammo = read_file[1]
            best_timed = read_file[2]
            file.close()
            best_freeplay = 0
            best_ammo = 0
            best_timed = 0
            file = open('high_scores.txt', 'w')
            file.write(f'{best_freeplay}\n{best_ammo}\n{best_timed}')
            file.close()




    pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    Homepagehub()
