from dataclasses import dataclass, field
from pathlib import Path
from textwrap import wrap
from .Styles import DpgColor, DpgStyles
from .BaseItem import BaseItem
import dearpygui.dearpygui as dpg
from typing import List


'''
Just use Button
'''

# @dataclass
# class Text(BaseItem):
#     """
#     **{
#          "tag": f"_{self.id}",
#          "color": [255,255,255,255], 
#          "text": '',
#          "bullet": False,
#          "font": None, #"mainFont_20"
         
#     }

#     """
#     bullet: bool = False
#     text: str = ''
#     color: List = field(default_factory=lambda: [255,255,255,255])
#     def __post_init__(self):
#         ...
    
#     def Styles(self):
#         ...
#     def setValue(self, value:str):
#         dpg.set_value(self.tag,value)   
    
#     def create(self, Parent=None):
#         values = {
#             "tag": self.tag,
#             "default_value": self.text,
#             "color": MyColor.get(self.color) if isinstance(self.color, str) else self.color
            
#         }
#         if Parent:
#             values["parent"] = Parent
        
#         dpg.add_text(**values)

#         self.addStyles()

#         self.addFont()
#         return self


