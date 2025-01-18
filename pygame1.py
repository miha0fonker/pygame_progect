import pygame
import random
import sqlite3

global run

db_name = 'carandgold.db'
connection = sqlite3.connect(db_name)
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS carandgold(
nickname,
score
)
''')


def creatle_log_in():
    cursor = connection.cursor()
    name = input()
    try:
        prohel_proverky_login = cursor.execute("""SELECT nickname FROM carandgold WHERE (nickname = ?)""", (name,)).fetchall()[0]
        if len(prohel_proverky_login) == 1:
            print("Такой никнейм существует!")
            return creatle_log_in()
    except IndexError:
        cursor.execute("""INSERT INTO carandgold (nickname, score) VALUES(? , 0 )""", (name,))
        connection.commit()
    main()



def log_in():
    cursor = connection.cursor()
    global run
    global name2
    global name1
    global goldper
    global goldvtor
    flag1 = False
    flag2 = False
    name1 = input()
    name2 = input()
    flag_login = True
    try:
        prohel_proverky_login1 = \
        cursor.execute("""SELECT nickname FROM carandgold WHERE (nickname = ?)""", (name1,)).fetchall()[0]
        flag1 = True
    except IndexError:
        print("Неверный никнейм первого аккаунта!")
        return log_in()
    try:
        prohel_proverky_login2 = \
        cursor.execute("""SELECT nickname FROM carandgold WHERE (nickname = ?)""", (name2,)).fetchall()[0]
        flag2 = True
    except IndexError:
        print("Неверный никнейм второго аккаунта!")
        return log_in()
    if flag1 == flag2:
        if flag_login:
            a = cursor.execute("""SELECT score FROM carandgold WHERE (nickname = ?)""", (name1,)).fetchall()
            b = cursor.execute("""SELECT score FROM carandgold WHERE (nickname = ?)""", (name2,)).fetchall()
            for i in a:
                goldper = (i)
            goldper = str(goldper)[1]
            for j in b:
                goldvtor = (j)
            goldvtor = str(goldvtor)[1]
            print(goldvtor, goldper)
            run = True
            connection.commit()
        else:
            return log_in()
        connection.commit()

def main():
    l = []
    print("Ввести никнейм или выбрать существующий")
    menu = cursor.execute('''SELECT * FROM carandgold'''). fetchall()
    for k in menu:
        print(k)
    vibor = input()
    if vibor == "1":
        creatle_log_in()
    else:
        log_in()

main()

pygame.init()

screen_width = 1200
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("CAR AND GOLD")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (40, 40, 40)
YELLOW = (255, 255, 0)

# Переменные
x_gold = 1200
y_gold = 400
x_gold2 = 1500
y_gold2 = random.randint(120, 480)
step = 5
y_car = 120
gold = 0
gold2 = 0
my_font = pygame.font.Font(None, 36)
x_car2 = 1200
y_car2 = random.randint(100, 447)
car1 = pygame.image.load("Машина 1.png")
car2 = pygame.image.load("Машина 2.png")
car3 = pygame.image.load("Машина 3.png")
car = car1
t = 0
finish = 1
speed = 1
y_car3 = 320
red_car = pygame.image.load("red_car.png")


while run:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            run = False
    # Логика (соблюдайте отступ!)
    game_time = pygame.time.get_ticks()
    x_gold = x_gold - step
    if x_gold <= -20:
        x_gold = 1300
        y_gold = random.randint(120, 480)
    x_gold2 = x_gold2 - step
    if x_gold2 <= -20:
        x_gold2 = 1300
        y_gold2 = random.randint(120, 480)
    x_car2 = x_car2 - step + 2
    if x_car2 <= -159:
        x_car2 = 1200
        y_car2 = random.randint(100, 447)
    if x_gold <= -20:
        x_gold = 1300
        y_gold = random.randint(120, 480)

    x_gold2 = x_gold2 - step
    if x_gold2 <= -20:
        x_gold2 = 1300
        y_gold2 = random.randint(120, 480)
    keys = pygame.key.get_pressed()

    if keys[pygame.K_1]:
        step = 5
        speed = 1
    if keys[pygame.K_2]:
        step = 6
        speed = 2
    if keys[pygame.K_3]:
        step = 7
        speed = 3
    if keys[pygame.K_4]:
        step = 8
        speed = 4
    if keys[pygame.K_5]:
        step = 9
        speed = 5
    if keys[pygame.K_6]:
        step = 10
        speed = 6
    if keys[pygame.K_7]:
        step = 14
        speed = 10

    if y_car > 100:
        if keys[pygame.K_UP]:
            y_car = y_car - 5
    if y_car < 440:
        if keys[pygame.K_DOWN]:
            y_car = y_car + 5
    if 100 < x_gold < 100 + 100:
        if y_car + 60 > y_gold > y_car:
            x_gold = 1300
            y_gold = random.randint(120, 480)
            gold = gold + 1
    if 100 < x_gold2 < 200:
        if y_car + 60 > y_gold2 > y_car:
            x_gold2 = 1300
            y_gold2 = random.randint(120, 480)
            gold = gold + 1

    if y_car3 > 100:
        if keys[pygame.K_w]:
            y_car3 = y_car3 - 5
    if y_car3 < 440:
        if keys[pygame.K_s]:
            y_car3 = y_car3 + 5
    if 100 < x_gold < 100 + 100:
        if y_car3 + 60 > y_gold > y_car3:
            x_gold = 1300
            y_gold = random.randint(120, 480)
            gold2 = gold2 + 1
    if 100 < x_gold2 < 200:
        if y_car3 + 60 > y_gold2 > y_car3:
            x_gold2 = 1300
            y_gold2 = random.randint(120, 480)
            gold2 = gold2 + 1

    t = t + 1

    if t < 10:
        car = car1
    if 10 < t < 20:
        car = car2
    if 20 < t < 30:
        car = car3
    if t == 30:
        car = car1
        t = 0

    if y_car < y_car2 < y_car + 60:
        if 100 < x_car2 < 200:
            finish = 0
        if 100 < x_car2 + 159 < 200:
            finish = 0
    if y_car < y_car2 + 53 < y_car + 60:
        if 100 < x_car2 < 200:
            finish = 0
        if 100 < x_car2 + 159 < 200:
            finish = 0

    if y_car3 < y_car2 < y_car3 + 60:
        if 100 < x_car2 < 200:
            finish = 0
        if 100 < x_car2 + 159 < 200:
            finish = 0
    if y_car3 < y_car2 + 53 < y_car3 + 60:
        if 100 < x_car2 < 200:
            finish = 0
        if 100 < x_car2 + 159 < 200:
            finish = 0

    if game_time > 60000:
        finish = 2

    if gold == 25:
        finish = 3

    # Рисование
    if finish == 1:
        screen.fill(BLACK)
        pygame.draw.line(screen, WHITE, (0, 100), (1200, 100), 10)
        pygame.draw.line(screen, WHITE, (0, 500), (1200, 500), 10)
        pygame.draw.line(screen, WHITE, (0, 300), (1200, 300), 4)
        # pygame.draw.rect(screen, RED, (100, y_car, 100, 60))
        # pygame.draw.rect(screen, RED, (100, y_car3, 100, 60))
        screen.blit(red_car, (100, y_car))
        screen.blit(red_car, (100, y_car3))
        pygame.draw.circle(screen, YELLOW, (x_gold, y_gold), 20)
        pygame.draw.circle(screen, YELLOW, (x_gold2, y_gold2), 20)
        screen.blit(car, (x_car2, y_car2))

        text_gold = str(gold)
        t_gold = f"{name1}:" + text_gold
        if int(gold) > int(goldper):
            cursor.execute('''UPDATE carandgold SET score = ? WHERE nickname = ?''', (gold, name1))
            connection.commit()
        text = my_font.render(t_gold, True, WHITE)
        screen.blit(text, (10, 10))

        text_gold = str(gold2)
        t_gold = f"{name2}:" + text_gold
        if int(gold2) > int(goldvtor):
            cursor.execute('''UPDATE carandgold SET score = ? WHERE nickname = ?''', (gold2, name2))
            connection.commit()
        text = my_font.render(t_gold, True, WHITE)
        screen.blit(text, (10, 50))

        text_time = str(round(game_time / 1000))
        t_time = "Time: " + text_time
        text = my_font.render(t_time, True, WHITE)
        screen.blit(text, (150, 10))

    else:
        if finish == 0:
            my_font = pygame.font.Font(None, 120)
            text = my_font.render("АВАРИЯ!!!", True, WHITE)
            screen.blit(text, (350, 200))
        if finish == 2:
            my_font = pygame.font.Font(None, 120)
            text = my_font.render("КОНЕЦ ИГРЫ!!!", True, WHITE)
            screen.blit(text, (350, 200))
        if finish == 3:
            my_font = pygame.font.Font(None, 120)
            text = my_font.render("ты победил!!", True, WHITE)
            screen.blit(text, (350, 200))


    pygame.time.delay(17)
    pygame.display.update()
quit()
