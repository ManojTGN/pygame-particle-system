
#*
BEST_SUIT_WIDTH = 1366
BEST_SUIT_HEIGHT = 768 

#COLORS
COLOR_BLACK = (0,0,0)
COLOR_WHITE = (255,255,255)
COLOR_GREEN = (0,255,0)

#SETTINGS SECTION
GLOBAL_SETTINGS = [
    ("Global","TITLE"),
    ("Duration","INPUT",5.0),
    ("Looping","CHECKBOX",True),
    ("Start Delay","INPUT",0),
    ("Start Lifetime","INPUT",5),
    ("Start Speed","INPUT",5),
    ("Start Size","INPUT",10),
    ("Color","COLOR",COLOR_WHITE),
    ("Gravity","INPUT",1),
]

EMISSION_SETTINGS = [
    ("Emission","TITLE")
]

SHAPE_SETTINGS = [
    ("Shape","TITLE"),
    ("Shape","DROPDOWN","Circle","Square","Triangle"),
    ("Position(X)","INPUT",0),
    ("Position(Y)","INPUT",0),
]

RENDERER_SETTINGS = [
    ("Renderer","TITLE"),
]

TEXTURE_SETTINGS = [
    ("Texture","TITLE"),
]

#ALL SETTINGS SECTIONS
SETTINGS_LIST = [
    GLOBAL_SETTINGS,
    EMISSION_SETTINGS,
    SHAPE_SETTINGS,
    TEXTURE_SETTINGS,
    RENDERER_SETTINGS
]