import pygame
from ParticleSystem.Configs import *
from ParticleSystem.Surf import SurfManager
from ParticleSystem.UI.Font import Font

class Screen:
    def __init__(self) -> None:
        self.WINDOW = pygame.display.get_surface()
        self.WINDOW_SIZE = self.WINDOW.get_size()

        self.RENDERER_WINDOW = pygame.Surface(((self.WINDOW_SIZE[0]/10)*7,self.WINDOW_SIZE[1]))
        self.SETTING_WINDOW = pygame.Surface(((self.WINDOW_SIZE[0]/10)*3,self.WINDOW_SIZE[1]))
        
        self.FONT = Font()
        self.Surf = SurfManager(self.SETTING_WINDOW)
        
        #RENDERER SCREEN
        self.RendererText = self.FONT.render("Particle Renderer",COLOR_WHITE,64)
        self.RendererTextPos = self.RendererText.get_rect()
        self.RendererTextPos.center = ( self.RENDERER_WINDOW.get_size()[0]//2, self.RENDERER_WINDOW.get_size()[1]//2 )

    def render_rendererWindow(self) -> None:
        self.RENDERER_WINDOW.fill(COLOR_BLACK)
        pygame.draw.rect(self.RENDERER_WINDOW,COLOR_WHITE,pygame.Rect(0,0,self.RENDERER_WINDOW.get_size()[0],self.RENDERER_WINDOW.get_size()[1]),4)
        self.RENDERER_WINDOW.blit(self.RendererText,self.RendererTextPos)


    def BlitToMainScreen(self) -> None:
        self.WINDOW.blit(self.RENDERER_WINDOW,(0,0))
        self.WINDOW.blit(self.SETTING_WINDOW,(self.RENDERER_WINDOW.get_size()[0],0))

    def render(self) -> None:
        self.render_rendererWindow()
        self.Surf.render()
        self.BlitToMainScreen()