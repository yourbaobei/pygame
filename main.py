import pygame as pg
import random
pg.init()
FPS = 30
clock = pg.time.Clock()

x = random.randint(1, 500)
y = random.randint(1, 500)

win = pg.display.set_mode((500, 500))
win.fill('white')
x = 200
speed = -5

"""
for i in range(100):

    x = random.randint(1, 500)
    y = random.randint(1, 500)
    a = random.randint(1, 250)
    b = random.randint(1, 250)
    c = random.randint(1, 250)
    pg.draw.circle(win, (a, b, c), (x, y), 30)
"""
while True:
    x = x + speed
    if x >= 600 or x <= 0:
        speed = -1 * speed
    win.fill('white')
    pg.draw.circle(win, (0, 0, 0), (x, 200), 30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    pg.display.update()
    clock.tick(FPS)
