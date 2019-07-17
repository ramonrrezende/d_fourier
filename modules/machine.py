import math
from modules.fourier import *
import pygame
import modules.colors as colors
from modules.controller import *

class double_machine_draw:
    def __init__(self, screen, signal_x, signal_y):
        self.screen = screen
        self.fourier_x = fourier(signal_x).get_transform()
        self.fourier_y = fourier(signal_y).get_transform()
        self.tick = 2 * math.pi / len(self.fourier_x)
        self.path = []
        self.controller = controller(self.tick, self.path, len(self.fourier_x))
        self.center_x = [100, 300]
        self.center_y = [500, 100]
        self.done = False
        self.pause = False
        self.k = len(self.fourier_x)
        self.hide = False

    def draw(self, time, pause):
        self.pause, self.hide, self.path, self.done = self.controller.input()
        x, y = self.center_x
        x2, y2 = self.center_y
        for i in range(1, self.k):
            freq_x = self.fourier_x[i].get('freq')
            radiusx = self.fourier_x[i].get('amp')
            phasex = self.fourier_x[i].get('phase')
            freq_y = self.fourier_y[i].get('freq')
            radiusy = self.fourier_y[i].get('amp')
            phasey = self.fourier_y[i].get('phase')
            if(not self.hide):
                if(radiusy >= 1):
                    pygame.draw.circle(self.screen, colors.WHITE, [int(x2), int(y2)], int(radiusy), 1)
                else:
                    pygame.draw.circle(self.screen, colors.WHITE, [int(x2), int(y2)], 1, 1)
                if(radiusx >= 1):
                    pygame.draw.circle(self.screen, colors.WHITE, [int(x), int(y)], int(radiusx), 1)
                else:
                    pygame.draw.circle(self.screen, colors.WHITE, [int(x), int(y)], 1, 1)
            temp_x = x
            temp_y = y
            temp_x2 = x2
            temp_y2 = y2
            x = x + radiusx * math.cos(freq_x * time + phasex)
            y = y + radiusx * math.sin(freq_x * time + phasex)
            x2 = x2 + radiusy * math.cos(freq_y * time + phasey)
            y2 = y2 + radiusy * math.sin(freq_y * time + phasey)
            pygame.draw.line(self.screen, colors.WHITE, [temp_x, temp_y], [x, y])
            pygame.draw.line(self.screen, colors.WHITE, [temp_x2, temp_y2], [x2, y2])
            pygame.draw.circle(self.screen, colors.WHITE, [int(x), int(y)], 0, 0)
                    
        if(not self.pause):
            self.path.insert(0, [x2, y])
                
            if(len(self.path) > len(self.fourier_x)):
                self.path.pop()
        for i in range(1, len(self.path)):
            pygame.draw.line(self.screen, colors.PURPLE, self.path[i - 1], self.path[i])
        pygame.draw.line(self.screen, colors.WHITE, [int(x), int(y)], self.path[0])
        pygame.draw.line(self.screen, colors.WHITE, [int(x2), int(y2)], self.path[0])

class simple_machine_draw:
    def __init__(self, screen, signal):
        self.screen = screen
        self.fourier = fourier2d(signal).get_transform()
        self.tick = 2 * math.pi / len(self.fourier)
        self.path = []
        self.controller = controller(self.tick, self.path, len(self.fourier))
        self.center = [400, 300]
        self.done = False
        self.pause = False
        self.k = len(self.fourier)
        self.hide = False
    
    def draw(self, time, pause):
        self.pause, self.hide, self.path, self.done = self.controller.input()
        x, y = self.center
        for i in range(1, self.k):
            n = self.fourier[i].get('freq')
            radius = self.fourier[i].get('amp')
            phase = self.fourier[i].get('phase')
            if(not self.hide):
                if(radius >= 1):
                    pygame.draw.circle(self.screen, colors.WHITE, [int(x), int(y)], int(radius), 1)
                else:
                    pygame.draw.circle(self.screen, colors.WHITE, [int(x), int(y)], 1, 1)
            temp_x = x
            temp_y = y
            x = x + radius * math.cos(n * time + phase + math.pi/2)
            y = y + radius * math.sin(n * time + phase + math.pi/2)
            pygame.draw.line(self.screen, colors.WHITE, [temp_x, temp_y], [x, y])
            pygame.draw.circle(self.screen, colors.WHITE, [int(x), int(y)], 0, 0)
                        
        if(not self.pause):
            self.path.insert(0, [x, y])
            
            if(len(self.path) > len(self.fourier)):
                self.path.pop()
        for i in range(1, len(self.path)):
            pygame.draw.line(self.screen, colors.PURPLE, self.path[i - 1], self.path[i])
        pygame.draw.line(self.screen, colors.WHITE, [int(x), int(y)], self.path[0])