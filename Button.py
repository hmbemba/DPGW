from typing import List
from .BaseItem import BaseItem
from .Styles import DpgColor, DpgStyles
import dearpygui.dearpygui as dpg
import tkinter as tk
from dataclasses import dataclass, field

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


@dataclass(slots=True)
class Button(BaseItem):
    """
    styles = {
        "tag": f"_{self.id}",
        "w": -1,
        "h": -1,
        "text": "Btn Text",
        "textColor": [255,255,255,255],#"white",
        "font": "mainFont_50",
        "callback": None, #self.autoFind,
        "border": False,
        "borderRadius": 0,
        "borderColor": [0,0,0,0], #'red',
        "bkgColor": [0, 0, 0, 0],
        "bkgColorHovered": [0, 0, 0, 0],#[37 * 0.7, 37 * 0.7, 38 * 0.7, 255],
        'bkgColorClicked': [0, 0, 0, 0],#'green',
        "padding": [0,0] ,#[10, 10],

    }

    """

    """Style and Configuration Properties"""

    bkgColorHovered: List = field(default_factory=lambda: [0, 0, 0, 0])
    bkgColorClicked: List = field(default_factory=lambda: [0, 0, 0, 0])
    textColor: List = field(default_factory=lambda: [0, 0, 0, 0])

    text: str = None

    def __post_init__(self):
        self.w = self.mapWidthHeight(self.w)
        self.h = self.mapWidthHeight(self.h)

    """Methods to style and create this Item"""

    def Styles(self):
        DpgColor(self.bkgColor).buttonBg()
        DpgColor(self.bkgColorHovered).buttonBgHovered()
        DpgColor(self.bkgColorClicked).buttonBgClicked()
        DpgColor(self.textColor).text()
        DpgColor(self.borderColor).border()

        DpgStyles.frameBorder(self.border)
        DpgStyles.borderRadius(self.borderRadius)

        DpgStyles.padding(self.padding[0], self.padding[1])

    def create(self, Parent=None) -> object:
        values = {
            "tag": self.tag,
            "width": self.w,
            "height": self.h,
            "label": self.text,
            "callback": self.callback,
        }

        if Parent:
            values["parent"] = Parent

        dpg.add_button(**values)

        self.addStyles()

        self.addFont()

        if self.onHover:
            self.setHoverCallback(self.onHover)
        
        return self
