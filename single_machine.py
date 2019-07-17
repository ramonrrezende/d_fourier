import pygame
import math
import random
from modules.complex_number import complex_number
from modules.machine import simple_machine_draw
from modules.signal import signal_handler

opt = int(input("Choose an option:\n1 - Draw example\n2 - Draw input\n"))
pygame.init()
SRD = [800, 600]
screen = pygame.display.set_mode(SRD)
done = False
time = 0
pygame.display.set_caption("Fun with Discrete Fourier Transform")
clock = pygame.time.Clock()

signal = []
handler = signal_handler(screen)
if(opt == 1):
    handler.load_example()
    signal = handler.signal
if(opt == 2):
    handler.input()
    signal = handler.signal
for i in range(len(signal)):
    signal[i] = complex_number(signal[i][0], signal[i][1])

machine = simple_machine_draw(screen, signal)
pause = False
while(not done):
    clock.tick(60)
    screen.fill([0, 0, 0])
    machine.draw(time, pause)
    if(not pause):
        time -= machine.tick
    done = machine.done
    pause = machine.pause
    pygame.display.flip()
pygame.quit()

