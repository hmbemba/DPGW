from dataclasses import dataclass
from textwrap import wrap
from .Styles import setColor, setStyles
from .BaseItem import BaseItem
import dearpygui.dearpygui as dpg


@dataclass
class TextInput(BaseItem):
    """
    ** {
         "tag": f"_{self.id}",
         "w": -1,  # 0.58,
         "h": 200,#-1,
         # "border": True,
         "borderColor": [0,0,0,0],
         #'borderRadius': 5,
         "padding": [10, 70],
         "bkgColor": [255, 0, 0, 255],
         # "bkgColorHovered": [37 * 0.7, 37 * 0.7, 38 * 0.7, 255],
         #'bkgColorClicked': 'green',
         "defaultValue": '',#self.getLastModifiedFile(DOWNLOADED_VIDEOS_PATH),
         "focus": True,
         # "textColor": "red",
         "font": "mainFont_40",
         "multiLine": False,
         #"onHover": self.stopShow
         "hint":'',
     }.create(Parent=)

    """

    defaultValue: str = "Enter Text Here"
    focus: bool = False
    multiLine: bool = True
    hint: str = None

    def Styles(self):
        setColor.frameBgColor(self.bkgColor)
        # DpgColor(self._bkgColorHovered[0]).buttonBgHovered()
        # DpgColor(self._bkgColorClicked[0]).buttonBgClicked()
        # DpgColor(self._textColor).text()
        # DpgColor("green").frameBgHovered()
        setColor.borderColor(self.borderColor)

        setStyles.frameBorder(self.border)
        setStyles.borderRadius(self.borderRadius)
        setStyles.padding(self.padding[0], self.padding[1])
        # DpgColor('white').frameBgHovered()
        # DpgStyles.windowPadding(0,0)

    def getValue(self):
        return dpg.get_value(self.tag)
    
    def setValue(self, value:str):
        dpg.set_value(self.tag,value)    
    
    def clear(self):
        dpg.set_value(self.tag,'')
    
    def create(self, Parent=None) -> object:
        values = {
            "tag": self.tag,
            "width": self.w,
            "height": self.h,
            "default_value": self.defaultValue,
            "hint": self.hint,
            "multiline": self.multiLine,
        }
        if Parent:
            values["parent"] = Parent

        dpg.add_input_text(**values)

        self.addStyles()

        self.addFont()

        if self.onHover:
            self.setHoverCallback(self.onHover)

        if self.focus:
            dpg.focus_item(self.tag)
        
        return self
