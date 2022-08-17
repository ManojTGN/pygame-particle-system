import pygame
from ParticleSystem.Configs import *
from ParticleSystem.MainSurf import ParticleSys
from ParticleSystem.SettingsSurf import SettingsSurfManager

class Screen:
    def __init__(self) -> None:
        self.WINDOW = pygame.display.get_surface()
        self.WINDOW_SIZE = self.WINDOW.get_size()

        self.RENDERER_WINDOW = pygame.Surface(((self.WINDOW_SIZE[0]/10)*7,self.WINDOW_SIZE[1]))
        self.SETTING_WINDOW = pygame.Surface(((self.WINDOW_SIZE[0]/10)*3,self.WINDOW_SIZE[1]))
        
        self.SettingsSurf = SettingsSurfManager(self.SETTING_WINDOW)
        self.MainSurf = ParticleSys(self.RENDERER_WINDOW,self.SettingsSurf.OPTIONS)

    def BlitToMainScreen(self) -> None:
        self.WINDOW.blit(self.RENDERER_WINDOW,(0,0))
        self.WINDOW.blit(self.SETTING_WINDOW,(self.RENDERER_WINDOW.get_size()[0],0))

    def render(self) -> None:
        self.MainSurf.render()
        self.SettingsSurf.render()

        self.BlitToMainScreen()