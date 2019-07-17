import pygame
import math
import random
from modules.machine import double_machine_draw
from modules.signal import signal_handler

opt = int(input("Choose an option:\n1 - Draw example\n2 - Draw input\n"))

pygame.init()
SRD = [800, 600]
screen = pygame.display.set_mode(SRD)
done = False
pygame.display.set_caption("Fun with Discrete Fourier Transform")
clock = pygame.time.Clock()
signal_x = []
signal_y = []
if(opt == 1):
    signal_x, signal_y = signal_handler(screen).load_example()
if(opt == 2):
    signal_x, signal_y = signal_handler(screen).input()


time = 0
if(len(signal_x) == 0):
    done = True

machine = double_machine_draw(screen, signal_x, signal_y)
pause = False
while(not done):
    clock.tick(60)
    screen.fill([0, 0, 0])
    machine.draw(time, pause)
    if(not machine.pause):
        time -= machine.tick
    done = machine.done
    pygame.display.flip()
pygame.quit()

