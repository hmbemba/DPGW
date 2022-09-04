from dataclasses import dataclass, field
from pathlib import Path
from textwrap import wrap
from .Styles import DpgColor, DpgStyles
from .BaseItem import BaseItem
import dearpygui.dearpygui as dpg
from typing import List


@dataclass
class Text(BaseItem):
    """
    Styles = {
         "tag": f"_{self.id}",
         "w": 0, # 0 is default 
         "h": 0, # 0 is default 
         "color": [255,255,255,255], 
         "text": '',
         "bullet": False,
         "font": None, #"mainFont_20"
         
    }

    """
    bullet: bool = False
    text: str = ''
    color: List = field(default_factory=lambda: [255,255,255,255])
    def __post_init__(self):
        ...
    
    def Styles(self):
        ...

    def create(self, Parent=None):
        values = {
            "tag": self.tag,
            # "width": self.w,
            # "height": self.h,
            "default_value": self.text,
            "color": self.color
            
        }
        if Parent:
            values["parent"] = Parent
        
        dpg.add_text(**values)

        self.addStyles()

        self.addFont()


