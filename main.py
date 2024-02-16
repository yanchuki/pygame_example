import numpy as np
import pygame as pg


fps = pg.time.Clock()
screen = pg.display.set_mode((510, 510))
map_colors = np.arange(0, 510)
for i in map_colors:
    for j in map_colors:
        surf = pg.Surface((1, 1))
        surf.fill((i // 2, i // 2, i // 2))
        screen.blit(surf, (i, j))

r = 0
g = 0
b = 255
circle_start_size = 1
circle_end_size = 50
current_size = circle_end_size
size_dir = 1

while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    if pg.mouse.get_pressed()[0]:
        pg.draw.circle(screen, (r, g, b), pg.mouse.get_pos(), current_size, 2)

    if r < 255 and g == 0:
        r += 1
        b -= 1
    elif g < 255 and b == 0:
        g += 1
        r -= 1
    else:
        b += 1
        g -= 1

    if current_size in (circle_start_size, circle_end_size):
        size_dir *= -1

    current_size += size_dir

    fps.tick(60)
    pg.display.update()


