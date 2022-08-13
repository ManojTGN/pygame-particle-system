import pygame
from ParticleSystem.Configs import *
from ParticleSystem.Screen import Screen

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
                break
            if(event.type == pygame.MOUSEBUTTONDOWN):
                pos = pygame.mouse.get_pos()
                pos = (pos[0] - self.Screen.RENDERER_WINDOW.get_size()[0],pos[1])

                self.Screen.GlobalCheck.isClicked(pos)
                self.Screen.GlobalInput.isClicked(pos)
            elif(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN):
                    if(self.Screen.GlobalInput.isTyping):
                        self.Screen.GlobalInput.DoneTyping()
                else:
                    if(self.Screen.GlobalInput.isTyping):
                        self.Screen.GlobalInput.Type(event)

    def run(self) -> None:
        if(self.isRunning): return
        self.isRunning = True

        while(self.isRunning):
            self.WINDOW.fill(COLOR_BLACK)
            self.Screen.render()
            pygame.display.update()
            self.eventHandler()