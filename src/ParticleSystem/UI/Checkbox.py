import pygame
from ParticleSystem.Configs import *

class Checkbox:
    def __init__(self,WINDOW:pygame.Surface,x:int,y:int,width:int = 20,isChecked:bool = False) -> None:
        self.WINDOW = WINDOW
        self.x,self.y = x,y
        self.width = width
        self.isChecked = isChecked

    def isClicked(self,pos:tuple) -> bool:
        if pygame.Rect(self.x,self.y,self.width,self.width).collidepoint(pos[0],pos[1]):
            self.isChecked = True if(not self.isChecked) else False
        return self.isChecked

    def render(self) -> None:
        if(self.isChecked):
            pygame.draw.rect(self.WINDOW,COLOR_WHITE,pygame.Rect(self.x+2,self.y+2,self.width-4,self.width-4))

        pygame.draw.rect(self.WINDOW,COLOR_WHITE,pygame.Rect(self.x,self.y,self.width,self.width),1)