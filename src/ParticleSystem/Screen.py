import pygame
from ParticleSystem.Configs import *
from ParticleSystem.UI.Font import Font
from ParticleSystem.UI.Checkbox import Checkbox
from ParticleSystem.UI.Input import Input

class Screen:
    def __init__(self) -> None:
        self.WINDOW = pygame.display.get_surface()
        self.WINDOW_SIZE = self.WINDOW.get_size()

        self.RENDERER_WINDOW = pygame.Surface(((self.WINDOW_SIZE[0]/10)*7,self.WINDOW_SIZE[1]))
        self.SETTING_WINDOW = pygame.Surface(((self.WINDOW_SIZE[0]/10)*3,self.WINDOW_SIZE[1]))
        self.FONT = Font()

        #RENDERER SCREEN
        self.RendererText = self.FONT.render("Particle Renderer",COLOR_WHITE,64)
        self.RendererTextPos = self.RendererText.get_rect()
        self.RendererTextPos.center = ( self.RENDERER_WINDOW.get_size()[0]//2, self.RENDERER_WINDOW.get_size()[1]//2 )
        #SETTINGS SCREEN
        self.GlobalText = self.FONT.render("Global Settings",COLOR_WHITE,32)
        self.GlobalCheck = Checkbox(self.SETTING_WINDOW,10,50,20,True)
        self.GlobalInput = Input(self.SETTING_WINDOW,10,100,0,60)

    def render_rendererWindow(self) -> None:
        self.RENDERER_WINDOW.fill(COLOR_BLACK)
        pygame.draw.rect(self.RENDERER_WINDOW,COLOR_WHITE,pygame.Rect(0,0,self.RENDERER_WINDOW.get_size()[0],self.RENDERER_WINDOW.get_size()[1]),4)
        self.RENDERER_WINDOW.blit(self.RendererText,self.RendererTextPos)

    def render_settingsWindow(self) -> None:
        self.SETTING_WINDOW.fill(COLOR_BLACK)
        pygame.draw.rect(self.SETTING_WINDOW,COLOR_WHITE,pygame.Rect(0,0,self.SETTING_WINDOW.get_size()[0],self.SETTING_WINDOW.get_size()[1]),4)
        self.SETTING_WINDOW.blit(self.GlobalText,(10,0))
        
        self.GlobalCheck.render()
        self.GlobalInput.render()

    def BlitToMainScreen(self) -> None:
        self.WINDOW.blit(self.RENDERER_WINDOW,(0,0))
        self.WINDOW.blit(self.SETTING_WINDOW,(self.RENDERER_WINDOW.get_size()[0],0))

    def render(self) -> None:
        self.render_rendererWindow()
        self.render_settingsWindow()
        self.BlitToMainScreen()