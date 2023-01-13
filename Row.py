from dataclasses import dataclass, field
from BaseItem import BaseItem
from Styles import setColor, setStyles
import dearpygui.dearpygui as dpg
from Container import Container
from typing import Any
from contextlib import contextmanager


@dataclass(slots=True)
class Row(BaseItem):
    """
    **{
        "tag": f"row_1_{self.id}",
        "numCols":2,
        "sizing":0, #,1,2,3,
        "border":True,
        "bkgColor":[255,0,0,255],
        "padding": [10,0], # Default is [10,0]
        "user_data": None,

        }
    """



    def enabledStyles(self):
        dpg.highlight_table_row(f"{self.tag}_table", 0, self.bkgColor)
        setStyles.cellPadding(self.padding[0], self.padding[1])

    def disabledStyles(self):
        ...
        
    @contextmanager
    def create(self, Parent: str = None):

        sizingPolicy = {
            0: dpg.mvTable_SizingStretchProp,
            1: dpg.mvTable_SizingFixedFit,
            2: dpg.mvTable_SizingFixedSame,
            3: dpg.mvTable_SizingStretchSame,
        }

        values = {
            
            "header_row" : False,
            "scrollY" : False,
            "scrollX" : False,
            "tag" : f"{self.tag}_table",
            "borders_innerV" : self.border,
            "borders_outerH" : self.border,
            "borders_outerV" : self.border,
            "width" : self.w,
            "policy" : sizingPolicy.get(self.sizing, dpg.mvTable_SizingStretchProp),
            "pad_outerX" : True,
            "user_data" :  self.user_data,
            }

        if Parent:
            values["parent"] = Parent

        dpg.add_table(**values)
        dpg.add_table_row(
            tag=f"{self.tag}_row",
            parent=f"{self.tag}_table",
        )

        self.buildColumns()
        self.addFont(tag=f"{self.tag}_table")
        self.addStyles(self.enabledStyles,f"{self.tag}_table")
        
        yield self

    def buildColumns(self):
        for col in range(0, self.numCols):
            dpg.add_table_column(
                tag=f"{self.tag}_col_{col}",
                parent=f"{self.tag}_table",
            )

    def link(self):
        return f"{self.tag}_row"


