import pygame
import sys
import time 
from pygame.locals import *

XO = 'x'
winner = None
draw = None
width = 400
height = 400
white = (255, 255, 255)
line_color = (0, 0, 0)
board = [[None]*3, [None]*3, [None]*3]
pygame.init()
fps = 30
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode(
    (width, height + 100), 0, 32)
pygame.display.set_caption('My Tic Tac Toe')
initiating_window = pygame.image.load('modified_cover.png')
x_img = pygame.image.load('x_modified.png')
y_img = pygame.image.load('o_modified.png')

initiating_window = pygame.transform.scale(
    initiating_window, (width, height + 100))
x_img = pygame.transform.scale(x_img, (80, 80))
o_img = pygame.transform.scale(y_img, (80, 80))
def game_initiating_window():
    screen.blit(initiating_window, (0, 0))
    pygame.display.update()
    time.sleep(3)
    screen.fill(white)
    pygame.draw.line(screen, line_color, (width/3,0),
                (width / 3, height), 7)
    pygame.draw.line(screen, line_color, (width/3 * 2,0),
                (width / 3 * 2, height), 7)
    
    #linhas horizontais
    pygame.draw.line(screen, line_color, (0, height/ 3),
                (width, height / 3), 7)
    pygame.draw.line(screen, line_color, (0, height/3 * 2),
                (width, height / 3 * 2), 7)
    draw_status()

def draw_status():
    global draw

    if winner is None:
        message = XO.upper() + "s Turn"
    else: 
        message = winner.upper() + "won!"
    if draw:
        message = "Game Draw"
    
    font = pygame.font.Font(None, 30)
    text = font.render(message, 1, (255, 255, 255))
    screen.fill((0, 0, 0), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(width / 2, 500-50))
    screen.blit(text, text_rect)
    pygame.display.update()

def check_win():
    global board, winner, draw

    for row in range(0, 3):
        if ((board[row][0] == board[row][1] == board [row][2])
        and (board[row][0] is not None)):
            winner = board[row][0]
            pygame.draw.line(screen, (250, 0, 0),
                         (0, (row + 1)* height / 3 - height / 6),
                         (width, (row + 1)* height /3 - height/6),
                         4)
            break


    for col in range(0, 3):
        if ((board[0][col] == board[1][col] == board [2][col])
        and (board[0][col] is not None)):
            winner = board[0][col]
            pygame.draw.line(screen, (250, 0, 0), ((col+1)
                        * width / 3 - width / 6, 0),
                        ((col + 1)*width/3-width/6,height), 4)
            break
    if (board[0][0]==board[1][1]==board[2][2]) and (board[0][0] is not None):
        winner = board[0][0]
        pygame.draw.line(screen, (250, 70, 70), (50, 50), (350, 350), 4)

    if (board[0][2]==board[1][1]==board[2][0]) and (board[0][2] is not None):
        winner = board[0][2]
        pygame.draw.line(screen, (250, 70, 70), (350, 50), (50, 350), 4)

    if(all([all(row)for row in board]) and winner is None):
        draw = True
    draw_status()

def drawXO(row, col):
    global board, XO
    if row == 1:
        posx = 30
    if row == 2:
        posx = width / 3 + 30
    if row == 3:
        posx = width / 3 * 2 + 30
    if col == 1:
        posy = 30
    if col == 2:
        posy = height / 3 + 30
    if col == 3:
        posy = height / 3 * 2 + 30
    board[row-1][col-1] = XO
    if(XO == 'x'):
        screen.blit(x_img, (posy, posx)) 
        XO = 'o'
    else:
        screen.blit(o_img, (posy, posx))
        XO = 'x'
    pygame.display.update()

# Assuming you have defined width, height, board, drawXO, check_win, reset_game, winner, draw, XO, fps, and CLOCK before this point

def user_click():
    global XO
    x, y = pygame.mouse.get_pos()
    if x < width / 3:
        col = 1
    elif x < width / 3 * 2:
        col = 2
    elif x < width:
        col = 3
    else:
        col = None

    if y < height / 3:
        row = 1
    elif y < height / 3 * 2:
        row = 2
    elif y < height:
        row = 3
    else:
        row = None

    if row is not None and col is not None and board[row - 1][col - 1] is None:
        drawXO(row, col)
        check_win()

def reset_game():
    global board, winner, XO, draw
    time.sleep(3)
    XO = 'x'
    draw = False
    game_initiating_window()
    winner = None
    board = [[None]*3, [None]*3, [None]*3]

game_initiating_window()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            user_click()
            if winner or draw:
                reset_game()

    pygame.display.update()
    CLOCK.tick(fps)

