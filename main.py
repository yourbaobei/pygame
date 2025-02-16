import pygame as pg
import random
pg.init()
FPS = 30
clock = pg.time.Clock()
x = random.randint(1, 500)
y = random.randint(1, 500)
win = pg.display.setmode((500, 500))
win.fill('white')
for i in range(100):
    pg.draw.circle(win, (112, 204, 209), (x, y), 50)
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    pg.display.update()
    clock.tick(FPS)
