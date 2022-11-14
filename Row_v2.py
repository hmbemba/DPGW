from dataclasses import dataclass, field
from .BaseItem import BaseItem
from .Styles import DpgColor, DpgStyles
import dearpygui.dearpygui as dpg
from .Container import Container
from typing import Any

@dataclass(slots=True)
class Row(BaseItem):
    """
    **{
        "tag": f"row_1_{self.id}",
        "parent":self.top.link(),
        "numCols":2,
        "sizing":0, #,1,2,3,
        "border":True,
        "bkgColor":[255,0,0,255],
        "padding": [10,0], # Default is [10,0]
        "user_data": None,

        }
    """

    numCols : int = 0# = numCols
    w: int = 0 
    sizing: int = 0# = sizing


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
        self.addStyles(tag=f"{self.tag}_table")
        
        return self

    def buildColumns(self):
        for col in range(0, self.numCols):
            dpg.add_table_column(
                tag=f"{self.tag}_col_{col}",
                parent=f"{self.tag}_table",
            )

    def link(self):
        return f"{self.tag}_row"

    def Styles(self):
        dpg.highlight_table_row(f"{self.tag}_table", 0, self.bkgColor)
        DpgStyles.cellPadding(self.padding[0], self.padding[1])
