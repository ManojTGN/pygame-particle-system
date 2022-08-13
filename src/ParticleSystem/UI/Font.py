import pygame

class Font:
    def __init__(self) -> None:
        self.FontPath = "src\\ParticleSystem\Fonts\JetBrainsMono-Regular.ttf"

    def render(self,Text:str,Color:tuple,Size:int) -> pygame.Surface:
        FONT = pygame.font.Font(self.FontPath, Size)
        return FONT.render(Text, True,Color)