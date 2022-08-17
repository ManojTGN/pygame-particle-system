import pygame
from ParticleSystem.Configs import *
from ParticleSystem.UI.Font import Font
from ParticleSystem.UI.Input import Input
from ParticleSystem.UI.Checkbox import Checkbox

class SettingsSurf:
    def __init__(self,SETTINGS:tuple,surf:pygame.Surface,Startpos:tuple = (0,0)) -> None:
        self.SETTINGS = SETTINGS

        self.surf = surf
        self.StartPos = Startpos
        self.width,self.height = surf.get_size()
        self.heightGap = 30

        self.Texts = []
        self.Components = []

        self.FONT = Font()
        self.__build()

    def __build(self) -> None:
        tmpSize,tmpX,tmpY = 0,self.StartPos[0],self.StartPos[1]
        for SETTING in self.SETTINGS:
            #Text
            tmpSize = int(32*self.height/BEST_SUIT_HEIGHT) if(SETTING[1] == "TITLE") else int(16*self.height/BEST_SUIT_HEIGHT)
            self.Texts.append( [self.FONT.render(SETTING[0],COLOR_WHITE,tmpSize),(10,tmpY)] )
            
            #Component
            tmpX = self.Texts[-1][0].get_rect().width +20 if(self.Texts[-1][0].get_rect().width > self.width) else self.width//2
            if(SETTING[1] == "INPUT"):self.Components.append(Input(self.surf,tmpX,tmpY,tmpX-20,self.Texts[-1][0].get_rect().height,SETTING[2],SETTING[2]))
            elif(SETTING[1] == "CHECKBOX"):self.Components.append(Checkbox(self.surf,tmpX,tmpY,20,SETTING[2]))

            tmpY = tmpY+self.heightGap+20 if(SETTING[1] == "TITLE") else tmpY+self.heightGap

    def hover(self) -> None:
        for Component in self.Components:
            if(Component.isHover()): return True
        return False

    def render(self) -> None:
        self.hover()
        for Text in self.Texts:self.surf.blit(Text[0],Text[1])
        for Component in self.Components:Component.render()

class SettingsSurfManager:
    def __init__(self,SettingsSurface:pygame.Surface) -> None:
        self.SettingsSurface = SettingsSurface
        self.Surfaces = []
        self.OPTIONS = {}

        startpos = (0,10)
        for SETTINGS in SETTINGS_LIST:

            for SETTING in SETTINGS:
                if(SETTING[1] != "TITLE"):
                    self.OPTIONS[SETTING[0].replace(' ','_')] = SETTING[2]
            
            self.Surfaces.append(SettingsSurf(SETTINGS,self.SettingsSurface,startpos))
            startpos = (0,self.Surfaces[-1].Texts[-1][1][1] + 50)

    def hover(self):
        for Surface in self.Surfaces:
            if(Surface.hover()):
                pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
                return 
        pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def render(self) -> None:
        self.SettingsSurface.fill(COLOR_BLACK)

        self.hover()
        for Surface in self.Surfaces:
            Surface.render()
            
        