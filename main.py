# Snake the Game
# Created by Konrad Ceglarski 2019
__author__ = "Konrad Ceglarski"
__version__ = "1.0.0"

'''
Pisane po angielsku, ponieważ jest mi tak wygodniej i łatwiej,
przyzwyczaiłem się już do tego, że jak programuje to używam angielskiego dla spójności i ciągłości,
pomimo to czasami zdarza mi się wrzucić polski komentarz, czy zmienną, albo string'a.
Uważam, że każdy programista powinnien umieć pisać po angielsku.
Staram się pisać schludnie, a także komentować co nieco.

Ilość linijek: ~250 (150, 80, 20)
'''

# using pygame == 1.9.6 (higher should be fine too.)
import pygame, os, sys
import snake as snake_class
import food as food_class

os.system('title SNAKE')
os.system('cls')
print('SNAKE\n\nPowered by Python 3 and Pygame\nMade with heart by Konrad Ceglarski\n[Student of ZSET Leszno Class 2TI1 (2019)]')

# base values:
colors = [(50,50,50),(255,255,255),(128,128,128),(230,80,60),(255, 210, 50)]
map_size = 25
scale = 25
fps = 15
running = True
pause = False
game_over = False
borders = False

# cmd arguments
args = sys.argv[1:]
try:
    if len(args) > 0:
        if len(args) >= 1:
            map_size = int(args[0])
            if map_size >= 10 and map_size <= 30:
                print(f"\n{'argument initialized map size':<20} to {map_size}")
            else:
                map_size = 25
        if len(args) >= 2:
            scale = int(args[1])
            if scale >= 20 and scale <= 40:
                print(f"{'argument initialized scale':<20} to {scale}")
            else:
                scale = 25
        if len(args) >= 3:
            fps = int(args[2])
            print(f"{'argument initialized fps':<20} to {fps}")
        if len(args) == 4 and (args[3].lower() == 'true' or args[3].lower() == 'false'):
            if args[3].lower() == 'true':
                borders = True
            elif args[3].lower() == 'false':
                borders = False
            print(f"{'argument initialized borders':<20} to {'true' if borders else 'false'}")
except:
    pass

# app initialization
os.environ['SDL_VIDEO_CENTERED'] = '1' # center the window
pygame.init()
app = pygame.display.set_mode((map_size * scale, map_size * scale))
pygame.display.set_caption("snake")
clock = pygame.time.Clock()

# pause screen
pause_bg = pygame.Surface((map_size * scale, map_size * scale))
pause_bg.set_alpha(128)

snake = snake_class.snake([[2,12],[1,12],[0,12]])
food = food_class.food(map_size, snake.elements, 1)

font_sizes = [int(map_size * scale / 15), int(map_size * scale / 5)]

# functions
def display_len():
    global font_sizes
    font = pygame.font.SysFont("Arial", font_sizes[0])
    text = font.render(str(snake.lenght), True, colors[1])
    app.blit(text, (scale/2, scale/2))

def pause_screen():
    global done, font_sizes
    pause_bg.fill((0,0,0))
    font = pygame.font.SysFont("Arial", font_sizes[1])
    text = font.render("paused", True, colors[1])
    text_rect = text.get_rect()
    text_rect.center = (map_size * scale / 2, map_size * scale / 2)
    app.blit(pause_bg, (0, 0))
    app.blit(text, text_rect)

def game_over_screen():
    global done, font_sizes
    pause_bg.fill(colors[3])
    font = pygame.font.SysFont("Arial", font_sizes[1])
    text = font.render("game over", True, colors[1])
    text_rect = text.get_rect()
    text_rect.center = (map_size * scale / 2, map_size * scale / 2)
    app.blit(pause_bg, (0, 0))
    app.blit(text, text_rect)
    font = pygame.font.SysFont("Arial", font_sizes[0])
    text = font.render("press r to restart", True, colors[1])
    text_rect = text.get_rect()
    text_rect.center = (map_size * scale / 2, map_size * scale / 2 + font_sizes[0] * 2)
    app.blit(text, text_rect)

def restart():
    global pause, game_over
    snake.restart([[2,12],[1,12],[0,12]])
    pause = False
    game_over = False

while running:
    for e in pygame.event.get():
        # exit on esc or window's cross
        if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
            running = False
        # game over reset
        elif e.type == pygame.KEYDOWN and e.key == pygame.K_r and game_over:
            restart()
        # pause
        elif e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE and not game_over:
            pause = not pause
            pause_screen()
        # movement - setting snake's direction
        elif e.type == pygame.KEYDOWN and not snake.key_lock and not pause and not game_over:
            if (e.key == pygame.K_w or e.key == pygame.K_UP) and snake.dir != 'S':
                snake.dir = 'N'
                snake.key_lock = True
            elif (e.key == pygame.K_s or e.key == pygame.K_DOWN) and snake.dir != 'N':
                snake.dir = 'S'
                snake.key_lock = True
            elif (e.key == pygame.K_d or e.key == pygame.K_RIGHT) and snake.dir != 'W':
                snake.dir = 'E'
                snake.key_lock = True
            elif (e.key == pygame.K_a or e.key == pygame.K_LEFT) and snake.dir != 'E':
                snake.dir = 'W'
                snake.key_lock = True    

    if not pause and not game_over:
        app.fill(colors[0])
        if borders:
            pygame.draw.rect(app, colors[2], [0, 0, map_size * scale, map_size * scale], 1)
        food.display(app, colors, scale)
        snake.display(app, colors, scale, map_size, borders)
        display_len()
        snake.move()
        snake.check_collision(map_size, borders, food)
        if snake.dead:
            game_over = True
            game_over_screen()

    # refresh the screen
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()