import pygame
import math
import random
from fourier import *


pygame.init()
SRD = [800, 600]
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
PURPLE = [148,0,211]
screen = pygame.display.set_mode(SRD)
done = False
pygame.display.set_caption("Fun with Discrete Fourier Transform")
clock = pygame.time.Clock()
signal = []
f_y = open('x.txt', 'r')
f_x = open('y', 'r')
value = 50
value2 = 50
for i in range(300):
    value += random.randint(-10, 10) 
    value2 += random.randint(-10, 10)
    signal.append([value, value2])

signal_x = []
signal_y = []
for line in f_x:
    aux = f_x.readline()
    
    signal_x.append(float(aux) +100)
for line in f_y:
    aux = f_y.readline()
    signal_y.append(float(aux) + 100)
signal = []
for i in range(len(signal_x)):
    signal.append([signal_x[i], signal_y[i]])
print(signal)
f_x.close()
f_y.close()

fouri_y = fourier(signal_y)
fouri_x  = fourier(signal_x)
dftx = fouri_x.get_transform()
dfty = fouri_y.get_transform()
time = 0
radius = 200
center_x = 100
center_y  = 300
center = [center_x, center_y]
center_x2 = 500
center_y2 = 100
begin = 2 * radius + 10
wave = [[begin, center_y]]
tick = 2 * math.pi / len(dftx)
k = len(dftx)
pause = False
while(not done):
    clock.tick(60)
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if(not pause):
                    pause = True
                else:
                    pause = False
            if event.key == pygame.K_DOWN:
                if(k > 0 ):
                    k -=1
            if event.key == pygame.K_UP:
                if(k < len(dft)):
                    k += 1
            if event.key == pygame.K_LEFT:
                if(tick > 0.005):
                    tick -= 0.005
            if event.key == pygame.K_RIGHT:
                if(tick < 0.1):
                    tick += 0.005
            if event.key == pygame.K_c:
                    wave = [wave[0]]

    screen.fill([0, 0, 0])

        
    x = center_x
    y = center_y
    x2 = center_x2
    y2 = center_y2
    for i in range(1, len(dftx)):
        nx = dftx[i].get('freq')
        radiusx = dftx[i].get('amp')
        phasex = dftx[i].get('phase')
        ny = dfty[i].get('freq')
        radiusy = dfty[i].get('amp')
        phasey = dfty[i].get('phase')
        if(radiusy >= 1):
            pygame.draw.circle(screen, WHITE, [int(x2), int(y2)], int(radiusy), 1)
        else:
            pygame.draw.circle(screen, WHITE, [int(x2), int(y2)], 1, 1)
        if(radiusx >= 1):
            pygame.draw.circle(screen, WHITE, [int(x), int(y)], int(radiusx), 1)
        else:
            pygame.draw.circle(screen, WHITE, [int(x), int(y)], 1, 1)
        temp_x = x
        temp_y = y
        temp_x2 = x2
        temp_y2 = y2
        x = x + radiusx * math.cos(nx * time + phasex)
        y = y + radiusx * math.sin(nx * time + phasex)
        x2 = x2 + radiusy * math.cos(ny * time + phasey + math.pi/2)
        y2 = y2 + radiusy * math.sin(ny * time + phasey + math.pi/2)
        pygame.draw.line(screen, WHITE, [temp_x, temp_y], [x, y])
        pygame.draw.line(screen, WHITE, [temp_x2, temp_y2], [x2, y2])
        pygame.draw.circle(screen, WHITE, [int(x), int(y)], 0, 0)
                    
    if(not pause):
        wave.insert(0, [x2, y])
        
        if(len(wave) > len(dftx)):
            wave.pop()
    for i in range(1, len(wave)):
        pygame.draw.line(screen, PURPLE, wave[i - 1], wave[i])
    pygame.draw.line(screen, WHITE, [int(x), int(y)], wave[0])
    pygame.draw.line(screen, WHITE, [int(x2), int(y2)], wave[0])
    if(not pause):
        time -= tick
    pygame.display.flip()
pygame.quit()

