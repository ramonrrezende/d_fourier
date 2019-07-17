import pygame

class controller:
    def __init__(self, tick, path, size):
        self.pause = False
        self.path = path
        self.size = size
        self.done = False
        self.hide = False

    def input(self):
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                self.done = True  # Flag that we are done so we exit this loop
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if(not self.pause):
                        self.pause = True
                    else:
                        self.pause = False
                if event.key == pygame.K_c:
                        self.path = [self.path[0]]
                if event.key == pygame.K_h:
                        if(not self.hide):
                            self.hide = True
                        else:
                            self.hide = False
        return self.pause, self.hide, self.path, self.done