from dataclasses import dataclass, field
from typing import Any, List
import dearpygui.dearpygui as dpg


def loudContainer(tag: str) -> dict:
    return {
        "tag": tag,
        "show": True,
        "w": -1,  # -1 is full, 0 is default, .001 to 1 is multiplied to screenWidth, 1.001+ = pixel values
        "h": -1,  # -1 is full, 0 is default, .001 to 1 is multiplied to screenHeight, 1.001+ = pixel values
        "autoSizeX": False,  # Overtakes w
        "autoSizeY": False,  # Overtakes h
        "itemOrientation": "col",  # row = items stacked left to right, col = items stacked top to btm
        "horzGap": 0,  # space between items when itemOrientation is row
        "verticalItemSpacing": [0, 0],
        "border": True,
        "borderRadius": 0,
        "borderColor": [255, 0, 0, 255],  # "orange",
        "bkgColor": [0, 0, 255, 255],
        "padding": [0, 0],  # [LR,TB] !Can also be negative
        "onHover": None,
        "noScrollBar": True,
        "font": None,  # "main_20"
    }


"""
loudButton
loudRow

"""

red = {
    100: [248, 215, 218, 255],
    200: [241, 174, 181, 255],
    300: [234, 134, 143, 255],
    400: [227, 93, 106, 255],
    500: [220, 53, 69, 255],
    600: [176, 42, 55, 255],
    700: [132, 32, 41, 255],
    800: [88, 21, 28, 255],
    900: [44, 11, 14, 255],
}

blue = {
    100: [207, 226, 255, 255],
    200: [158, 197, 254, 255],
    300: [110, 168, 254, 255],
    400: [61, 139, 253, 255],
    500: [13, 110, 253, 255],
    600: [10, 88, 202, 255],
    700: [8, 66, 152, 255],
    800: [5, 44, 101, 255],
    900: [3, 22, 51, 255],
}

green = {
    100: [209, 231, 221, 255],
    200: [163, 207, 187, 255],
    300: [117, 183, 152, 255],
    400: [71, 159, 118, 255],
    500: [25, 135, 84, 255],
    600: [20, 108, 67, 255],
    700: [15, 81, 50, 255],
    800: [10, 54, 34, 255],
    900: [5, 27, 17, 255],
}

indigo = {
    100: [224, 207, 252, 255],
    200: [194, 159, 250, 255],
    300: [163, 112, 247, 255],
    400: [133, 64, 245, 255],
    500: [102, 16, 242, 255],
    600: [82, 13, 194, 255],
    700: [61, 10, 145, 255],
    800: [41, 6, 97, 255],
    900: [20, 3, 48, 255],
}

purple = {
    100: [226, 217, 243, 255],
    200: [197, 179, 230, 255],
    300: [169, 142, 218, 255],
    400: [140, 104, 205, 255],
    500: [111, 66, 193, 255],
    600: [89, 53, 154, 255],
    700: [67, 40, 116, 255],
    800: [44, 26, 77, 255],
    900: [22, 13, 39, 255],
}

pink = {
    100: [247, 214, 230, 255],
    200: [239, 173, 206, 255],
    300: [230, 133, 181, 255],
    400: [222, 92, 157, 255],
    500: [214, 51, 132, 255],
    600: [171, 41, 106, 255],
    700: [128, 31, 79, 255],
    800: [86, 20, 53, 255],
    900: [43, 10, 26, 255],
}

orange = {
    100: [255, 229, 208, 255],
    200: [254, 203, 161, 255],
    300: [254, 178, 114, 255],
    400: [253, 152, 67, 255],
    500: [253, 126, 20, 255],
    600: [202, 101, 16, 255],
    700: [152, 76, 12, 255],
    800: [101, 50, 8, 255],
    900: [51, 25, 4, 255],
}

gray = {
    100: [248, 249, 250, 255],
    200: [233, 236, 239, 255],
    300: [222, 226, 230, 255],
    400: [206, 212, 218, 255],
    500: [173, 181, 189, 255],
    600: [108, 117, 125, 255],
    700: [73, 80, 87, 255],
    800: [52, 58, 64, 255],
    900: [33, 37, 41, 255],
}

cyan = {
    100: [207, 244, 252, 255],
    200: [158, 234, 249, 255],
    300: [110, 223, 246, 255],
    400: [61, 213, 243, 255],
    500: [13, 202, 240, 255],
    600: [10, 162, 192, 255],
    700: [8, 121, 144, 255],
    800: [5, 81, 96, 255],
    900: [3, 40, 48, 255],
}

teal = {
    100: [210, 244, 234, 255],
    200: [166, 233, 213, 255],
    300: [121, 223, 193, 255],
    400: [77, 212, 172, 255],
    500: [32, 201, 151, 255],
    600: [26, 161, 121, 255],
    700: [19, 121, 91, 255],
    800: [13, 80, 60, 255],
    900: [6, 40, 30, 255],
}

yellow = {
    100: [255, 243, 205, 255],
    200: [255, 230, 156, 255],
    300: [255, 218, 106, 255],
    400: [255, 205, 57, 255],
    500: [255, 193, 7, 255],
    600: [204, 154, 6, 255],
    700: [153, 116, 4, 255],
    800: [102, 77, 3, 255],
    900: [51, 39, 1, 255],
}



class Primary:
    def __init__(self, colorMap: dict) -> None:
        self.colorMap = colorMap
    
    @property
    def active(self):
        return self.colorMap[500]
    
    @property
    def hovered(self): 
        return self.colorMap[400]
    
    @property
    def clicked(self): 
        return self.colorMap[300]
    
    @property
    def border(self): 
        return self.colorMap[900] 
    
    @property
    def disabled(self): 
        return self.colorMap[800] 
    

@dataclass
class Text:
    active: List = field(default_factory=lambda: [255,255,255,255])  
    disabled: List = field(default_factory=lambda: [255,255,255,55]  )



class Bkg:
    def __init__(self, colorMap: dict) -> None:
        self.colorMap = colorMap
        
    @property
    def darkest(self):
        return [0,0,0,0]
    
    @property
    def dark(self):
        return self.colorMap[900]  
    
    @property
    def light(self):
        return self.colorMap[800]  
    
    @property
    def lighter(self):
        return self.colorMap[700]  
    
    @property
    def lightest (self):
        return self.colorMap[600]  


class Font:
    
    def __init__(self, fontFilePath) -> None:
        self.fontFilePath:str = fontFilePath
        self.smallest: str = "fontSmallest_20"
        self.small: str = "fontSmall_25"
        self.med:str = "fontMed_30"
        self.large: str = "fontLarge_40"
        self.largest: str = "fontLargest_50"
    
    def loadFont(self):
        with dpg.font_registry():
            dpg.add_font(self.fontFilePath, 20, tag=self.smallest)
            dpg.add_font(self.fontFilePath, 25, tag=self.small)
            dpg.add_font(self.fontFilePath, 30, tag=self.med)
            dpg.add_font(self.fontFilePath, 40, tag=self.large)
            dpg.add_font(self.fontFilePath, 50, tag=self.largest)



@dataclass
class MyTheme:
    primary:Primary
    bkg: Bkg
    text: Text
    font: Font
    # success: Success
    # danger: Danger
    # warning: Warning
    # font: Font
    

theme = MyTheme(
    primary= Primary(pink),
    bkg = Bkg(gray),
    text = Text(),
    font = Font(r"C:\Windows\Fonts\bahnschrift.ttf")
)

'''
implement functionality to be able to do 

maybe use __new__??

theme = MyTheme(
    primary= Primary(pink, disabled = pink[100]),
    bkg = Bkg(gray),
    text = Text()
)
'''