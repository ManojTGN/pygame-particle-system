import pygame
from ParticleSystem.Configs import *

class Screen:
    def __init__(self) -> None:
        self.WINDOW = pygame.display.get_surface()

        self.WINDOW_SIZE = self.WINDOW.get_size()
        self.RENDERER_WINDOW = pygame.Surface(((self.WINDOW_SIZE[0]/10)*7,self.WINDOW_SIZE[1]))
        self.SETTING_WINDOW = pygame.Surface(((self.WINDOW_SIZE[0]/10)*3,self.WINDOW_SIZE[1]))

    def render_rendererWindow(self) -> None:
        pygame.draw.rect(self.RENDERER_WINDOW,COLOR_WHITE,pygame.Rect(0,0,self.RENDERER_WINDOW.get_size()[0],self.RENDERER_WINDOW.get_size()[1]),4)

    def render_settingsWindow(self) -> None:
        pygame.draw.rect(self.SETTING_WINDOW,COLOR_WHITE,pygame.Rect(0,0,self.SETTING_WINDOW.get_size()[0],self.SETTING_WINDOW.get_size()[1]),4)
        

    def BlitToMainScreen(self) -> None:
        self.WINDOW.blit(self.RENDERER_WINDOW,(0,0))
        self.WINDOW.blit(self.SETTING_WINDOW,(self.RENDERER_WINDOW.get_size()[0],0))

    def render(self) -> None:
        self.render_rendererWindow()
        self.render_settingsWindow()
        self.BlitToMainScreen()