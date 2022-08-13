import pygame
from ParticleSystem.Configs import *
from ParticleSystem.UI.Font import Font

class Input:
    def __init__(self,WINDOW:pygame.Surface,x:int,y:int,value:float,width:int,height:int=20,default:int = 0) -> None:
        self.WINDOW = WINDOW
        self.x,self.y = x,y
        self.width,self.height = width,height
        self.default = default
        self.value = str(value)

        self.FONT = Font()
        self.isTyping = False
        self.text = self.FONT.render(self.value,COLOR_WHITE,16)

    def isClicked(self,pos:tuple) -> bool:
        if pygame.Rect(self.x,self.y,self.width,self.width).collidepoint(pos[0],pos[1]):
            self.isTyping = True
            pygame.mouse.set_visible(False)
        return self.isTyping

    def DoneTyping(self) -> None:
        self.isTyping = False
        pygame.mouse.set_visible(True)

    def Type(self,event) -> None:
        if event.key == pygame.K_BACKSPACE:self.value = self.value[:-1]
        else:self.value += event.unicode

    def render(self) -> None:
        if(self.isTyping ):
            self.text = self.FONT.render(self.value,COLOR_WHITE,16)
        pygame.draw.rect(self.WINDOW,COLOR_WHITE,pygame.Rect(self.x,self.y,self.width,self.height),1)
        self.WINDOW.blit(self.text,(self.x,self.y))