import pygame
from modules import colors

class signal_handler:
    def __init__(self, screen):
        self.signal = []
        self.drawing = False
        self.begin = False
        self.screen = screen

    def clear(self):
        self.signal = []

    def load_example(self):
        f_y = open('y.txt', 'r')
        f_x = open('x.txt', 'r')
        signal_x = []
        signal_y = []
        for line in f_x:
            aux = f_x.readline()
            
            signal_x.append(float(aux) +100)
        for line in f_y:
            aux = f_y.readline()
            signal_y.append(float(aux) + 100)
        for i in range(len(signal_x)):
           self.signal.append([signal_x[i], signal_y[i]])

        f_x.close()
        f_y.close()
        return signal_x, signal_y


    def input(self):
        signal_x = []
        signal_y = []
        clock = pygame.time.Clock()
        while(self.drawing or not self.begin):
            clock.tick(60)
            self.screen.fill([0, 0, 0])
            print(pygame.mouse.get_pressed()[0])
            if(pygame.mouse.get_pressed()[0]):
                if(self.drawing == False and self.begin == False):
                    self.drawing = True
                    self.begin = True
                pos = pygame.mouse.get_pos()
                print(pos)
                if(len(self.signal) == 0 or pos != self.signal[0]):
                    self.signal.insert(0, pos)
                    signal_x.insert(0, pos[0])
                    signal_y.insert(0, pos[1])
            elif(self.drawing == True):
                    self.drawing = False
            for event in pygame.event.get():
               if event.type == pygame.QUIT:  # If user clicked close
                   self.drawing = False
                   self.begin = True
                
                
            for i in range(1, len(self.signal)):
                pygame.draw.line(self.screen, colors.WHITE, self.signal[i - 1], self.signal[i])
            pygame.display.flip()
        print(signal_x)
        return signal_x, signal_y