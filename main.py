import pygame as pyg
import os.path
import time

filepath = os.path.dirname(__file__)
resource_path = os.path.join(filepath, 'resource')


turn = 'x'
s = [' ' for i in range(9)]
non = [True for j in range(9)]
y = 0
winner = ''


pyg.init()

screen = pyg.display.set_mode((800, 700))
icon = pyg.image.load(os.path.join(resource_path, "ttt.png"))
menu_running = True
game_running = True
conclusion_screen_running = True
# Setting icon and caption
pyg.display.set_caption('Tic-Tac-Toe!!')
pyg.display.set_icon(icon)

# Images Being Loaded
background_menu = pyg.image.load(os.path.join(resource_path, "Menu ttt.png"))
background_game = pyg.image.load(os.path.join(resource_path, "Game ttt.png"))
X_img = pyg.image.load(os.path.join(resource_path, "X.png"))
O_img = pyg.image.load(os.path.join(resource_path, "O.png"))
X_won = pyg.image.load(os.path.join(resource_path, "X won.png"))
O_won = pyg.image.load(os.path.join(resource_path, "O won.png"))
no_winner = pyg.image.load(os.path.join(resource_path, "Draw.png"))

continue_to_game_screen = pyg.draw.rect(screen, (0, 0, 0), (0, 0, 800, 700))
screen.blit(background_menu, (0, 0))


def check(x):
    return (s[0] == s[1] == s[2] == x or  # Row 1
            s[3] == s[4] == s[5] == x or  # Row 2
            s[6] == s[7] == s[8] == x or  # Row 3
            s[0] == s[3] == s[6] == x or  # Column 1
            s[1] == s[4] == s[7] == x or  # Column 2
            s[2] == s[5] == s[8] == x or  # Column 3
            s[0] == s[4] == s[8] == x or  # Diagonal
            s[2] == s[4] == s[6] == x)    # Opposite Diagonal


def result():
    global winner
    global y
    if not check('x') and not check('o') and y == 8:
        winner = no_winner
        return True
    elif check('x'):
        winner = X_won
        return True
    elif check('o'):
        winner = O_won
        return True


# Menu Loop
while menu_running:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            menu_running = False
            game_running = False
            conclusion_screen_running = False
        if event.type == pyg.MOUSEBUTTONUP:
            pos_click = pyg.mouse.get_pos()
            if continue_to_game_screen.collidepoint(pos_click):
                menu_running = False
                screen.fill((255, 255, 255))
                break
    pyg.display.update()

# Hit Box for game screen
first = pyg.draw.rect(screen, (0, 0, 0), (91, 42, 202, 202))
sec = pyg.draw.rect(screen, (0, 0, 0), (299, 42, 202, 202))
third = pyg.draw.rect(screen, (0, 0, 0), (506, 42, 202, 202))
forth = pyg.draw.rect(screen, (0, 0, 0), (91, 249, 202, 202))
fifth = pyg.draw.rect(screen, (0, 0, 0), (299, 249, 202, 202))
sixth = pyg.draw.rect(screen, (0, 0, 0), (506, 249, 202, 202))
seventh = pyg.draw.rect(screen, (0, 0, 0), (91, 457, 202, 202))
eighth = pyg.draw.rect(screen, (0, 0, 0), (299, 457, 202, 202))
nineth = pyg.draw.rect(screen, (0, 0, 0), (506, 457, 202, 202))

# Game Loop
screen.blit(background_game, (0, 0))
while game_running:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            game_running = False
            conclusion_screen_running = False
        if event.type == pyg.MOUSEBUTTONUP:
            pos_click = pyg.mouse.get_pos()
            if first.collidepoint(pos_click) and non[0]:
                if turn == 'x':
                    screen.blit(X_img, (123, 74))
                    turn = 'o'
                    s[0] = 'x'
                else:
                    screen.blit(O_img, (116, 67))
                    turn = 'x'
                    s[0] = 'o'
                non[0] = False
                y += 1
            if sec.collidepoint(pos_click) and non[1]:
                if turn == 'x':
                    screen.blit(X_img, (330, 74))
                    turn = 'o'
                    s[1] = 'x'
                else:
                    screen.blit(O_img, (323, 67))
                    turn = 'x'
                    s[1] = 'o'
                y += 1
                non[1] = False
            if third.collidepoint(pos_click) and non[2]:
                if turn == 'x':
                    screen.blit(X_img, (537, 74))
                    turn = 'o'
                    s[2] = 'x'
                else:
                    screen.blit(O_img, (530, 67))
                    turn = 'x'
                    s[2] = 'o'
                y += 1
                non[2] = False
            if forth.collidepoint(pos_click) and non[3]:
                if turn == 'x':
                    screen.blit(X_img, (123, 280))
                    turn = 'o'
                    s[3] = 'x'
                else:
                    screen.blit(O_img, (116, 274))
                    turn = 'x'
                    s[3] = 'o'
                y += 1
                non[3] = False
            if fifth.collidepoint(pos_click) and non[4]:
                if turn == 'x':
                    screen.blit(X_img, (330, 280))
                    turn = 'o'
                    s[4] = 'x'
                else:
                    screen.blit(O_img, (323, 274))
                    turn = 'x'
                    s[4] = 'o'
                y += 1
                non[4] = False
            if sixth.collidepoint(pos_click) and non[5]:
                if turn == 'x':
                    screen.blit(X_img, (537, 280))
                    turn = 'o'
                    s[5] = 'x'
                else:
                    screen.blit(O_img, (530, 274))
                    turn = 'x'
                    s[5] = 'o'
                y += 1
                non[5] = False
            if seventh.collidepoint(pos_click) and non[6]:
                if turn == 'x':
                    screen.blit(X_img, (123, 480))
                    turn = 'o'
                    s[6] = 'x'
                else:
                    screen.blit(O_img, (116, 482))
                    turn = 'x'
                    s[6] = 'o'
                y += 1
                non[6] = False
            if eighth.collidepoint(pos_click) and non[7]:
                if turn == 'x':
                    screen.blit(X_img, (330, 480))
                    turn = 'o'
                    s[7] = 'x'
                else:
                    screen.blit(O_img, (323, 482))
                    turn = 'x'
                    s[7] = 'o'
                y += 1
                non[7] = False
            if nineth.collidepoint(pos_click) and non[8]:
                if turn == 'x':
                    screen.blit(X_img, (537, 480))
                    turn = 'o'
                    s[8] = 'x'
                else:
                    screen.blit(O_img, (530, 462))
                    turn = 'x'
                    s[8] = 'o'
                y += 1
                non[8] = False
            if result():
                game_running = False
    pyg.display.update()

time.sleep(.4)
screen.fill((0, 0, 0))
continue_to_game_screen = pyg.draw.rect(screen, (0, 0, 0), (0, 0, 800, 700))
screen.blit(winner, (0, 0))

# Conclusion Screen Loop
while conclusion_screen_running:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            conclusion_screen_running = False
        if event.type == pyg.MOUSEBUTTONUP:
            pos_click = pyg.mouse.get_pos()
            if continue_to_game_screen.collidepoint(pos_click):
                conclusion_screen_running = False
                break
    pyg.display.update()















