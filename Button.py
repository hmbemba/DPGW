from typing import List, Any
from BaseItem import BaseItem
from Styles import setColor, setStyles
import dearpygui.dearpygui as dpg
from dataclasses import dataclass, field
import uuid


@dataclass(slots=True)
class Button(BaseItem):
    """
    **{
        "tag": f"_{self.id}",
        "w": -1,
        "h": -1,
        "text": "Btn Text",
        "textColor": [255,255,255,255],#"white",
        "font": "mainFont_50",
        "callback": None, #self.autoFind,
        "user_data": ...,
        "border": False,
        "borderRadius": 0,
        "borderColor": [0,0,0,0], #'red',
        "bkgColor": [0, 0, 0, 0],
        "bkgColorHovered": [0, 0, 0, 0],#[37 * 0.7, 37 * 0.7, 38 * 0.7, 255],
        'bkgColorClicked': [0, 0, 0, 0],#'green',
        "padding": [0,0] ,#[10, 10],
    }

    """

    def __post_init__(self):
        self.id = self.getId()
        self.stage = dpg.add_stage(tag=f'item_stage_{self.id}')


    """Methods to style and create this Item"""

    def enabledStyles(self):
        setColor.buttonBgColor(self.bkgColor)
        setColor.buttonBgHoveredColor(self.bkgColorHovered)
        setColor.buttonBgClickedColor(self.bkgColorClicked)
        setColor.textColor(self.textColor)
        setColor.borderColor(self.borderColor)

        setStyles.frameBorder(self.border)
        setStyles.borderRadius(self.borderRadius)

        setStyles.padding(self.padding[0], self.padding[1])

    def disabledStyles(self):
        setColor.buttonBgColor(self.bkgColorDisabled)
        setColor.buttonBgHoveredColor(self.bkgColorHoveredDisabled)
        setColor.buttonBgClickedColor(self.bkgColorClickedDisabled)
        setColor.textColor(self.textColorDisabled)
        setColor.borderColor(self.borderColor)

        setStyles.frameBorder(self.border)
        setStyles.borderRadius(self.borderRadius)

        setStyles.padding(self.padding[0], self.padding[1])

    def create(self, Parent=None) -> object:
        values = {
            "tag": self.tag,
            "width": self.w,
            "height": self.h,
            "label": self.text,
            "callback": self.callback,
            "user_data": self.user_data,
        }

        '''
        If you supply a parent to the create function that will take precendence
        '''
        if Parent:
            values["parent"] = Parent
            self.parent = Parent
        else:
            values["parent"] = self.parent

        self.enabledComp = dpg.add_button(**values)
        self.disabledComp = dpg.add_button(**{**values,'parent': self.stage,"tag":f"{self.tag}_disabled", 'callback':...})

        self.addStyles(self.enabledStyles,self.enabledComp)
        self.addStyles(self.disabledStyles,self.disabledComp)

        self.addFont(self.enabledComp)
        self.addFont(self.disabledComp)

        #self.setHoverCallback(self.enabledComp,'print')
        if self.onHover:
            self.setHoverCallback(self.onHover)
        
        return self





