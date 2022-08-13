import pygame
from ParticleSystem.Configs import *
from ParticleSystem.UI.Font import Font

class Input:
    def __init__(self,WINDOW:pygame.Surface,x:int,y:int,width:int,height:int=20,default:int = 0,value:int = 0) -> None:
        self.WINDOW = WINDOW
        self.x,self.y = x,y
        self.width,self.height = width,height
        self.default = default
        self.value = str(value)

        self.FONT = Font()
        self.isTyping = False
        self.text = self.FONT.render( self.value,COLOR_WHITE, int(16*self.WINDOW.get_height()/BEST_SUIT_HEIGHT) )

    def isClicked(self,pos:tuple) -> bool:
        if pygame.Rect(self.x,self.y,self.width,self.height).collidepoint(pos[0],pos[1]):
            self.isTyping = True
            pygame.mouse.set_visible(False)
        return self.isTyping

    def DoneTyping(self) -> None:
        if(not self.isTyping): return
        
        self.isTyping = False
        pygame.mouse.set_visible(True)

    def Type(self,event) -> None:
        if event.key == pygame.K_BACKSPACE:self.value = self.value[:-1]
        else:
            try:
                float(self.value+event.unicode)
                self.value += event.unicode
            except:pass
    
    def isHover(self) -> bool:
        pos = pygame.mouse.get_pos()
        pos = (pos[0] - (pygame.display.get_surface().get_width()-self.WINDOW.get_size()[0]),pos[1])
        return pygame.Rect(self.x,self.y,self.width,self.height).collidepoint(pos) 

    def render(self) -> None:
        if(self.isTyping):self.text = self.FONT.render(self.value,COLOR_WHITE,16)
        if( (self.value == "" or self.value == " ") and not self.isTyping):
            self.value = str(self.default)
            self.text = self.FONT.render(self.value,COLOR_WHITE,16)

        if(self.isTyping):pygame.draw.rect(self.WINDOW,COLOR_GREEN,pygame.Rect(self.x,self.y,self.width,self.height),1)
        else:pygame.draw.rect(self.WINDOW,COLOR_WHITE,pygame.Rect(self.x,self.y,self.width,self.height),1)
        self.WINDOW.blit(self.text,(self.x+2,self.y))