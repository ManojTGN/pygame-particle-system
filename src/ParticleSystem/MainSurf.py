import pygame

from .Configs import COLOR_WHITE

class Particle:
    def __init__(self) -> None:
        pass
    
    def isDead(self) -> bool:
        return False

    def render(self):
        pass

class ParticleSys:
    def fillMissing(self):
        # Todo: Check For Missing / Invalid Values 
        # And Set It To Default If The Section Is Active
        return 

    def start(self) -> bool:
        self.canRender = True
        return self.canRender

    def stop(self) -> bool:
        self.canRender = False
        return self.canRender

    def isRenderDone(self) -> bool:
        for PARTICLE in self.PARTICLES:
            if(not PARTICLE.isDead()):
                return False 

        return True

    def render(self) -> bool:
        if(not self.canRender):return False

        if(not self.OPTIONS['Looping']):
            if(self.isRenderDone()):
                self.canRender = False
            return
        
        for PARTICLE in self.PARTICLES[:]:
            if(not PARTICLE.isDead()):self.PARTICLES.remove(PARTICLE)
        for PARTICLE in self.PARTICLES:PARTICLE.render()

        pygame.draw.rect(self.WINDOW,COLOR_WHITE,pygame.Rect(0,0,self.WINDOW.get_width(),self.WINDOW.get_height()),2)
        return True

    def __init__(self,MainWindow:pygame.Surface,options:dict) -> None:
        
        self.WINDOW = MainWindow
        self.OPTIONS = options
        self.PARTICLES = []

        self.canRender = True
        self.fillMissing()