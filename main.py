from pygame import *

BGCOLOR = (230, 200, 89)
TEXTCOLOR = (134, 74, 249)

SCREENSIZE = (700, 700)

window = display.set_mode(SCREENSIZE)
display.set_caption("ping-pong")

timer = time.Clock()

run = True

while run: 
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    window.fill(BGCOLOR)
    display.update()
    timer.tick(60)