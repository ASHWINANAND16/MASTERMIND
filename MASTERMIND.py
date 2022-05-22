import pygame as pg
import sys
import time
from pygame.locals import *
import random

# variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 69, 0)
BROWN = (92, 64, 51)
game = False
# setting the color code to be found
colors = ["red", "yellow", "green", "blue", "white", "purple", "orange", "brown"]
computer_color_code = random.sample(colors,4) #[[color_1, color_2, color_3, color_4]]
print(computer_color_code)
code = [None, None, None, None]
check = [None, None, None, None]
# display and board
pg.init()
screen = pg.display.set_mode((1000, 605))
pg.display.set_caption("MASTERMIND")


# opening of the game
def opening():
    global white, red, purple, blue, green, yellow, brown, orange, screen

    # to display the game name - "MASTERMIND"
    screen.fill(BLACK)
    font = pg.font.Font(None, 70)
    text = font.render("GAME - MASTERMIND", 1, RED)
    rect = text.get_rect(center=(500, 100))
    screen.blit(text, rect)
    # play_game=pg.draw.rect(screen,WHITE,(408,250,185,50),3)

    # to ask to play or quit
    font = pg.font.Font(None, 35)
    text = font.render("PLAY GAME", 10, BLACK)
    rect = text.get_rect(center=(500, 275))
    play_game = pg.draw.rect(screen, WHITE, (408, 250, 185, 50), 0)
    screen.blit(text, rect)

    font = pg.font.Font(None, 40)
    text = font.render("QUIT", 10, BLACK)
    rect = text.get_rect(center=(500, 375))
    quit_game = pg.draw.rect(screen, WHITE, (408, 350, 185, 50), 0)
    screen.blit(text, rect)
    pg.display.update()

    # while loop to move on only after choosing to either play or quit
    pick = False
    while pick is False:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

            elif event.type == MOUSEBUTTONDOWN:

                if play_game.collidepoint(pg.mouse.get_pos()):
                    gameplay()
                    pick = True
                    break
                elif quit_game.collidepoint(pg.mouse.get_pos()):
                    pg.quit()
                    sys.exit()


# drawing the starting board
def gameplay():
    global white, red, purple, blue, green, yellow, orange, brown
    screen.fill(BLACK)

    # drawing the board
    pg.draw.line(screen, WHITE, (700, 0), (700, 605))
    pg.draw.line(screen, WHITE, (750, 0), (750, 605))
    for x in range(1, 12): pg.draw.line(screen, WHITE, (700, 50 * x), (1000, 50 * x))

    # displaying the turn number for respective boxes
    font = pg.font.Font(None, 30)
    text = font.render("TURN 11", 1, WHITE)
    rect = text.get_rect(center=(650, 585))
    screen.blit(text, rect)

    font = pg.font.Font(None, 30)
    text = font.render("TURN 10", 1, WHITE)
    rect = text.get_rect(center=(650, 535))
    screen.blit(text, rect)

    font = pg.font.Font(None, 30)
    text = font.render("TURN 9", 1, WHITE)
    rect = text.get_rect(center=(650, 485))
    screen.blit(text, rect)

    font = pg.font.Font(None, 30)
    text = font.render("TURN 8", 1, WHITE)
    rect = text.get_rect(center=(650, 435))
    screen.blit(text, rect)

    font = pg.font.Font(None, 30)
    text = font.render("TURN 7", 1, WHITE)
    rect = text.get_rect(center=(650, 385))
    screen.blit(text, rect)

    font = pg.font.Font(None, 30)
    text = font.render("TURN 6", 1, WHITE)
    rect = text.get_rect(center=(650, 335))
    screen.blit(text, rect)

    font = pg.font.Font(None, 30)
    text = font.render("TURN 5", 1, WHITE)
    rect = text.get_rect(center=(650, 285))
    screen.blit(text, rect)

    font = pg.font.Font(None, 30)
    text = font.render("TURN 4", 1, WHITE)
    rect = text.get_rect(center=(650, 235))
    screen.blit(text, rect)

    font = pg.font.Font(None, 30)
    text = font.render("TURN 3", 1, WHITE)
    rect = text.get_rect(center=(650, 185))
    screen.blit(text, rect)

    font = pg.font.Font(None, 30)
    text = font.render("TURN 2", 1, WHITE)
    rect = text.get_rect(center=(650, 135))
    screen.blit(text, rect)

    font = pg.font.Font(None, 30)
    text = font.render("TURN 1", 1, WHITE)
    rect = text.get_rect(center=(650, 85))
    screen.blit(text, rect)

    # displaying instructions
    font = pg.font.Font(None, 21)
    text = font.render("THE CLUES ARE MIXED UP AND NOT ACCORDING TO THE PLACE OF THE COLORS", 1, WHITE)
    rect = text.get_rect(center=(300, 595))
    screen.blit(text, rect)

    font = pg.font.Font(None, 30)
    text = font.render("YOUR COLOR CODE", 1, WHITE)
    rect = text.get_rect(center=(875, 28))
    screen.blit(text, rect)

    font = pg.font.Font(None, 35)
    text = font.render("PICK YOUR COLOR", 1, WHITE)
    rect = text.get_rect(center=(300, 200))
    screen.blit(text, rect)
    pg.draw.rect(screen, WHITE, (175, 250, 255, 145), 3)

    # colors to pick from
    white = pg.draw.rect(screen, WHITE, (195, 270, 40, 40), 0)
    red = pg.draw.rect(screen, RED, (255, 270, 40, 40), 0)
    purple = pg.draw.rect(screen, PURPLE, (315, 270, 40, 40), 0)
    orange = pg.draw.rect(screen, ORANGE, (375, 270, 40, 40), 0)
    blue = pg.draw.rect(screen, BLUE, (195, 340, 40, 40), 0)
    green = pg.draw.rect(screen, GREEN, (255, 340, 40, 40), 0)
    yellow = pg.draw.rect(screen, YELLOW, (315, 340, 40, 40), 0)
    brown = pg.draw.rect(screen, BROWN, (375, 340, 40, 40), 0)
    pg.display.update()


# to reset the game
def reset():
    global colors, color_1, color_2, color_3, color_4, computer_color_code, code, game

    # resetting all the variables to their original values
    game = False
    colors = ["red", "yellow", "green", "blue", "white", "purple"]
    computer_color_code = random.sample(colors,4)
    code = [[None, None, None, None]]
    check = [None, None, None, None]
    opening()


# to choose your color code
def pick_color(x):
    # the while loops are for moving to the next operation only after choosing the color
    # the .collidepoint() is used to check if user has clicked inside the respective color box
    global white, red, purple, blue, green, yellow, orange, brown

    # to pick 1st color
    pick = False
    while pick is False:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

            elif event.type == MOUSEBUTTONDOWN:

                if white.collidepoint(pg.mouse.get_pos()):
                    code[0] = "white"
                    pg.draw.circle(screen, WHITE, (780, 75 + turn * 50), 15)
                    pg.display.update()
                    pick = True
                    break
                elif red.collidepoint(pg.mouse.get_pos()):
                    code[0] = "red"
                    pg.draw.circle(screen, RED, (780, 75 + turn * 50), 15)
                    pg.display.update()
                    pick = True
                    break
                elif purple.collidepoint(pg.mouse.get_pos()):
                    code[0] = "purple"
                    pg.draw.circle(screen, PURPLE, (780, 75 + turn * 50), 15)
                    pg.display.update()
                    pick = True
                    break
                elif blue.collidepoint(pg.mouse.get_pos()):
                    code[0] = "blue"
                    pg.draw.circle(screen, BLUE, (780, 75 + turn * 50), 15)
                    pg.display.update()
                    pick = True
                    break
                elif green.collidepoint(pg.mouse.get_pos()):
                    code[0] = "green"
                    pg.draw.circle(screen, GREEN, (780, 75 + turn * 50), 15)
                    pg.display.update()
                    pick = True
                    break
                elif yellow.collidepoint(pg.mouse.get_pos()):
                    code[0] = "yellow"
                    pg.draw.circle(screen, YELLOW, (780, 75 + turn * 50), 15)
                    pg.display.update()
                    pick = True
                    break
                elif orange.collidepoint(pg.mouse.get_pos()):
                    code[0] = "orange"
                    pg.draw.circle(screen, ORANGE, (780, 75 + turn * 50), 15)
                    pg.display.update()
                    pick = True
                    break
                elif brown.collidepoint(pg.mouse.get_pos()):
                    code[0] = "brown"
                    pg.draw.circle(screen, BROWN, (780, 75 + turn * 50), 15)
                    pg.display.update()
                    pick = True
                    break

    # to pick 2nd color
    pick = False
    while pick is False:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

            elif event.type == MOUSEBUTTONDOWN:

                if white.collidepoint(pg.mouse.get_pos()):
                    code[1] = "white"
                    pg.draw.circle(screen, WHITE, (840, 75 + turn * 50), 15)
                    pg.display.update()
                    pick = True
                    break
                elif red.collidepoint(pg.mouse.get_pos()):
                    code[1] = "red"
                    pg.draw.circle(screen, RED, (840, 75 + turn * 50), 15)
                    pg.display.update()
                    pick = True
                    break
                elif purple.collidepoint(pg.mouse.get_pos()):
                    code[1] = "purple"
                    pg.draw.circle(screen, PURPLE, (840, 75 + turn * 50), 15)
                    pg.display.update()
                    pick = True
                    break
                elif blue.collidepoint(pg.mouse.get_pos()):
                    code[1] = "blue"
                    pg.draw.circle(screen, BLUE, (840, 75 + turn * 50), 15)
                    pg.display.update()
                    pick = True
                    break
                elif green.collidepoint(pg.mouse.get_pos()):
                    code[1] = "green"
                    pg.draw.circle(screen, GREEN, (840, 75 + turn * 50), 15)
                    pg.display.update()
                    pick = True
                    break
                elif yellow.collidepoint(pg.mouse.get_pos()):
                    code[1] = "yellow"
                    pg.draw.circle(screen, YELLOW, (840, 75 + turn * 50), 15)
                    pg.display.update()
                    pick = True
                    break
                elif orange.collidepoint(pg.mouse.get_pos()):
                    code[1] = "orange"
                    pg.draw.circle(screen, ORANGE, (840, 75 + turn * 50), 15)
                    pg.display.update()
                    pick = True
                    break
                elif brown.collidepoint(pg.mouse.get_pos()):
                    code[1] = "brown"
                    pg.draw.circle(screen, BROWN, (840, 75 + turn * 50), 15)
                    pg.display.update()
                    pick = True
                    break

    # to pick 3rd color
    pick = False
    while pick is False:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

            elif event.type == MOUSEBUTTONDOWN:

                if white.collidepoint(pg.mouse.get_pos()):
                    code[2] = "white"
                    pg.draw.circle(screen, WHITE, (900, 75 + turn * 50), 15)
                    pg.display.update()
                    pick = True
                    break
                elif red.collidepoint(pg.mouse.get_pos()):
                    code[2] = "red"
                    pg.draw.circle(screen, RED, (900, 75 + turn * 50), 15)
                    pg.display.update()
                    pick = True
                    break
                elif purple.collidepoint(pg.mouse.get_pos()):
                    code[2] = "purple"
                    pg.draw.circle(screen, PURPLE, (900, 75 + turn * 50), 15)
                    pg.display.update()
                    pick = True
                    break
                elif blue.collidepoint(pg.mouse.get_pos()):
                    code[2] = "blue"
                    pg.draw.circle(screen, BLUE, (900, 75 + turn * 50), 15)
                    pg.display.update()
                    pick = True
                    break
                elif green.collidepoint(pg.mouse.get_pos()):
                    code[2] = "green"
                    pg.draw.circle(screen, GREEN, (900, 75 + turn * 50), 15)
                    pg.display.update()
                    pick = True
                    break
                elif yellow.collidepoint(pg.mouse.get_pos()):
                    code[2] = "yellow"
                    pg.draw.circle(screen, YELLOW, (900, 75 + turn * 50), 15)
                    pg.display.update()
                    pick = True
                    break
                elif orange.collidepoint(pg.mouse.get_pos()):
                    code[2] = "orange"
                    pg.draw.circle(screen, ORANGE, (900, 75 + turn * 50), 15)
                    pg.display.update()
                    pick = True
                    break
                elif brown.collidepoint(pg.mouse.get_pos()):
                    code[2] = "brown"
                    pg.draw.circle(screen, BROWN, (900, 75 + turn * 50), 15)
                    pg.display.update()
                    pick = True
                    break

    # to pick 4th color
    pick = False
    while pick is False:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

            elif event.type == MOUSEBUTTONDOWN:

                if white.collidepoint(pg.mouse.get_pos()):
                    code[3] = "white"
                    pg.draw.circle(screen, WHITE, (960, 75 + turn * 50), 15)
                    pg.display.update()
                    pick = True
                    break
                elif red.collidepoint(pg.mouse.get_pos()):
                    code[3] = "red"
                    pg.draw.circle(screen, RED, (960, 75 + turn * 50), 15)
                    pg.display.update()
                    pick = True
                    break
                elif purple.collidepoint(pg.mouse.get_pos()):
                    code[3] = "purple"
                    pg.draw.circle(screen, PURPLE, (960, 75 + turn * 50), 15)
                    pg.display.update()
                    pick = True
                    break
                elif blue.collidepoint(pg.mouse.get_pos()):
                    code[3] = "blue"
                    pg.draw.circle(screen, BLUE, (960, 75 + turn * 50), 15)
                    pg.display.update()
                    pick = True
                    break
                elif green.collidepoint(pg.mouse.get_pos()):
                    code[3] = "green"
                    pg.draw.circle(screen, GREEN, (960, 75 + turn * 50), 15)
                    pg.display.update()
                    pick = True
                    break
                elif yellow.collidepoint(pg.mouse.get_pos()):
                    code[3] = "yellow"
                    pg.draw.circle(screen, YELLOW, (960, 75 + turn * 50), 15)
                    pg.display.update()
                    pick = True
                    break
                elif orange.collidepoint(pg.mouse.get_pos()):
                    code[3] = "orange"
                    pg.draw.circle(screen, ORANGE, (960, 75 + turn * 50), 15)
                    pg.display.update()
                    pick = True
                    break
                elif brown.collidepoint(pg.mouse.get_pos()):
                    code[3] = "brown"
                    pg.draw.circle(screen, BROWN, (960, 75 + turn * 50), 15)
                    pg.display.update()
                    pick = True
                    break


# to draw a red or a white circle as a clue
# the clues will not be according to the position of the color
def draw_clue():
    # red means a color is in the right position
    # white means a color is present but not in the right position

    if check[1] == "red":
        pg.draw.circle(screen, RED, (715, 65 + turn * 50), 6)
    elif check[1] == "white":
        pg.draw.circle(screen, WHITE, (715, 65 + turn * 50), 6)
    else:
        pg.draw.line(screen, WHITE, (710, 65 + turn * 50), (720, 65 + turn * 50), 2)

    if check[3] == "red":
        pg.draw.circle(screen, RED, (735, 65 + turn * 50), 6)
    elif check[3] == "white":
        pg.draw.circle(screen, WHITE, (735, 65 + turn * 50), 6)
    else:
        pg.draw.line(screen, WHITE, (730, 65 + turn * 50), (740, 65 + turn * 50), 2)

    if check[0] == "red":
        pg.draw.circle(screen, RED, (715, 85 + turn * 50), 6)
    elif check[0] == "white":
        pg.draw.circle(screen, WHITE, (715, 85 + turn * 50), 6)
    else:
        pg.draw.line(screen, WHITE, (710, 85 + turn * 50), (720, 85 + turn * 50), 2)

    if check[2] == "red":
        pg.draw.circle(screen, RED, (735, 85 + turn * 50), 6)
    elif check[2] == "white":
        pg.draw.circle(screen, WHITE, (735, 85 + turn * 50), 6)
    else:
        pg.draw.line(screen, WHITE, (730, 85 + turn * 50), (740, 85 + turn * 50), 2)
    pg.display.update()


# to check the entered code
def check_code():
    global screen, check, computer_color_code, turn

    # to check color at position 1
    if code[0] == computer_color_code[0] or computer_color_code[1] or computer_color_code[2] or \
            computer_color_code[3]:
        if code[0] == computer_color_code[0]:
            check[0] = "red"
        else:
            if code[0] == computer_color_code[1] and code[1] != computer_color_code[1]:
                check[0] = "white"
            else:
                if code[0] == computer_color_code[2] and code[2] != computer_color_code[2]:
                    check[0] = "white"
                else:
                    if code[0] == computer_color_code[3] and code[3] != computer_color_code[3]:
                        check[0] = "white"

    # to check color at position 2
    if code[1] == computer_color_code[0] or computer_color_code[1] or computer_color_code[2] or \
            computer_color_code[3]:
        if code[1] == computer_color_code[1]:
            check[1] = "red"
        else:
            if code[1] == computer_color_code[2] and code[2] != computer_color_code[2]:
                check[1] = "white"
            else:
                if code[1] == computer_color_code[3] and code[3] != computer_color_code[3]:
                    check[1] = "white"
                else:
                    if code[1] == computer_color_code[0] and code[0] != computer_color_code[0]:
                        check[1] = "white"

    # to check color at position 3
    if code[2] == computer_color_code[0] or computer_color_code[1] or computer_color_code[2] or \
            computer_color_code[3]:
        if code[2] == computer_color_code[2]:
            check[2] = "red"
        else:
            if code[2] == computer_color_code[3] and code[3] != computer_color_code[3]:
                check[2] = "white"
            else:
                if code[2] == computer_color_code[0] and code[0] != computer_color_code[0]:
                    check[2] = "white"
                else:
                    if code[2] == computer_color_code[1] and code[1] != computer_color_code[1]:
                        check[2] = "white"

    # to check color at position 4
    if code[3] == computer_color_code[0] or computer_color_code[1] or computer_color_code[2] or \
            computer_color_code[3]:
        if code[3] == computer_color_code[3]:
            check[3] = "red"
        else:
            if code[3] == computer_color_code[0] and code[0] != computer_color_code[0]:
                check[3] = "white"
            else:
                if code[3] == computer_color_code[1] and code[1] != computer_color_code[1]:
                    check[3] = "white"
                else:
                    if code[3] == computer_color_code[2] and code[2] != computer_color_code[2]:
                        check[3] = "white"
    draw_clue()  # to draw the clue
    check = [None, None, None, None]  # resetting check to original


# calling opening to start the game
opening()

# infinite game loop
while True:
    for e in pg.event.get():
        if e.type == QUIT:
            pg.quit()
            sys.exit()
        # while loop for turns 1 to 11
        turn = 0
        while turn < 11:
            pick_color(turn)
            # to check if code has been found
            if code == computer_color_code:

                # to print message if code has been found
                font = pg.font.Font(None, 35)
                text = font.render("YOU HAVE FOUND THE CODE,YOU WIN", 1, RED)
                rect = text.get_rect(center=(360, 50))
                screen.blit(text, rect)
                pg.display.update()
                time.sleep(4)

                reset()  # to reset all the variables to their original values after the game is over
                break  # to end the while loop after the game is over
            # if code hasn't been found then continue to the next turn
            else:
                check_code()
            if turn == 10 and code != computer_color_code:
                # to print message if code hasn't been found after 11 turns
                font = pg.font.Font(None, 34)
                text = font.render("YOU HAVEN'T FOUND THE CODE,BETTER LUCK NEXT TIME!", 1, RED)
                rect = text.get_rect(center=(355, 50))
                screen.blit(text, rect)
                pg.display.update()
                time.sleep(4)

                reset()  # to reset all the variables to their original values after the game is o
                break  # to end the while loop after the game is over
            turn += 1
