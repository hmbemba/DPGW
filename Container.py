from dataclasses import dataclass, field
from typing import List
from BaseItem import BaseItem
from Styles import setColor, setStyles
import dearpygui.dearpygui as dpg
import tkinter as tk



root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


@dataclass(slots=True)
class Container(BaseItem):
    """
    # GOTCHAS
        - border must be True for padding to work
        
    # Styles

        **{
            "tag": f"top_{self.id}",
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
            "bkgColor": [0, 0, 255,255],
            "padding": [0, 0],  # [LR,TB] !Can also be negative
            "onHover": None,
            "noScrollBar": True,
            "font": None,  # "main_20"
        }
    """
    itemOrientation: str = "col"
    horzGap: int = 0
    borderSize: int = 0
    autoSizeX: bool = False
    autoSizeY: bool = False
    show: bool = True
    noScrollBar: bool = True
    verticalItemSpacing: List = field(default_factory=lambda: [0, 0])

    def __post_init__(self):
        self.validateItemOrientation(self.itemOrientation)
        self.validateWH(self.w)
        self.validateWH(self.h)

        
        self.w = self.mapWidthHeight(self.w)
        self.h = self.mapWidthHeight(self.h)

    
    def validateWH(self, param):
        if isinstance(param, int) or isinstance(param, float):
            pass
        else:
            raise ValueError(
                f"The '{self.__class__}' parameter must be of type int OR float you entered : {param} which is a {type(param)}"
            )
    
    
    def validateItemOrientation(self, param):
        if isinstance(param, str):
            if param not in ["col", "row"]:
                raise ValueError(
                    f"The '{self.__class__}' parameter must be one of two values 'col' or 'row', you entered : {param} "
                )
        else:
            raise ValueError(
                f"The '{self.__class__}' parameter must be of type str you entered : {param} which is a {type(param)}"
            )

    def Styles(self):
        setColor.borderColor(self.borderColor)
        setColor.childBgColor(self.bkgColor)

        setStyles.childRounding(self.borderRadius)     
        setStyles.windowBorder(self.border)
        setStyles.windowPadding(self.padding[0], self.padding[1])
        setStyles.itemSpacing(self.verticalItemSpacing[0], self.verticalItemSpacing[1])

    def create(self, Parent=None) -> object:
        values  = {
                'tag':self.tag,
                'width':self.w,
                'height':self.h,
                'border':self.border,
                'autosize_x':self.autoSizeX,
                'autosize_y':self.autoSizeY,
                'show':self.show,
                'no_scrollbar':self.noScrollBar,
            
        }
        
        if Parent:
            values['parent'] = Parent
            
        dpg.add_child_window(**values)

        if self.itemOrientation == "row":
            dpg.add_group(
                tag=f"{self.tag}_group",
                parent=f"{self.tag}",
                horizontal=True,
                horizontal_spacing=self.horzGap,
            )

        self.addStyles()
        return self

    def link(self) -> str:
        if self.itemOrientation == "row":
            return f"{self.tag}_group"
        else:
            return self.tag

    