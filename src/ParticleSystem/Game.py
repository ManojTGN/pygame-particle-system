import pygame
from ParticleSystem.Configs import *
from ParticleSystem.Screen import Screen

class Game:
    def __init__(self) -> None:
        self.isRunning = False
        self.Screen = Screen()
        self.WINDOW = pygame.display.set_mode()

    def eventHandler(self) -> None:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                self.isRunning = False
                break

    def run(self) -> None:
        if(self.isRunning): return

        self.isRunning = True
        while(self.isRunning):
            self.WINDOW.fill(COLOR_BLACK)
            self.Screen.render()
            pygame.display.update()
            self.eventHandler()