
#*
BEST_SUIT_WIDTH = 1366
BEST_SUIT_HEIGHT = 768 

#COLORS
COLOR_BLACK = (0,0,0)
COLOR_WHITE = (255,255,255)


#SETTINGS SECTION
GLOBAL_SETTINGS = [
    ("Global Settings","TITLE"),
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
    ("Emission Settings","TITLE")
]

SHAPE_SETTINGS = [
    ("Shape Settings","TITLE")
]


#ALL SETTINGS SECTIONS
SETTINGS_LIST = [
    GLOBAL_SETTINGS,
    EMISSION_SETTINGS,
    SHAPE_SETTINGS
]