import pygame
from ParticleSystem.Configs import *
from ParticleSystem.Screen import Screen
from ParticleSystem.UI.Input import Input
from ParticleSystem.UI.Checkbox import Checkbox

class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.font.init()

        self.isRunning = False
        self.WINDOW = pygame.display.set_mode()
        self.Screen = Screen()

    def eventHandler(self) -> None:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                self.isRunning = False
                return
            if(event.type == pygame.MOUSEBUTTONDOWN):
                pos = pygame.mouse.get_pos()
                pos = (pos[0] - self.Screen.RENDERER_WINDOW.get_size()[0],pos[1])

                for Surface in self.Screen.Surf.Surfaces:
                    for Component in Surface.Components:
                        if(type(Component) == Input): Component.isClicked(pos)
                        if(type(Component) == Checkbox): Component.isClicked(pos)

            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN):
                    for INPUT in self.Screen.Surf.Surfaces:
                        for Component in INPUT.Components:
                            if(type(Component) == Input):Component.DoneTyping()
                
                for INPUT in self.Screen.Surf.Surfaces:
                    for Component in INPUT.Components:
                        if(type(Component) == Input and Component.isTyping):Component.Type(event)

    def run(self) -> None:
        if(self.isRunning): return
        self.isRunning = True

        while(self.isRunning):
            self.WINDOW.fill(COLOR_BLACK)
            self.Screen.render()
            pygame.display.update()
            self.eventHandler()