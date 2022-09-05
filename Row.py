from dataclasses import dataclass, field
from .BaseItem import BaseItem
from .Styles import DpgColor, DpgStyles
import dearpygui.dearpygui as dpg
from .Container import Container

class Row(BaseItem):
    """
    Styles = {
        "tag": f"row_1_{self.id}",
        "parent":self.top.link(),
        "numCols":2,
        "sizing":0, #,1,2,3,
        "border":True,
        "bkgColor":[255,0,0,255],
        "padding": [10,0] # Default is [10,0]
        "user_data": None,

        }
    """

    def __init__(
        self,
        tag,
        parent,
        numCols,
        font=None,
        w=0,
        h=0,
        border=False,
        sizing=None,
        bkgColor=[0, 0, 0, 0],
        padding=[10, 0],
        user_data = None,
    ):
        self._parent = parent
        self._numCols = numCols
        self.tag = tag
        self.font = font
        self.w = w
        self.h = h
        self.border = border
        self.sizing = sizing
        self.bkgColor = bkgColor
        self.padding = padding
        self.user_data = user_data

    def create(self):

        sizingPolicy = {
            0: dpg.mvTable_SizingStretchProp,
            1: dpg.mvTable_SizingFixedFit,
            2: dpg.mvTable_SizingFixedSame,
            3: dpg.mvTable_SizingStretchSame,
        }

        dpg.add_table(
            header_row=False,
            parent=self._parent,
            scrollY=False,
            scrollX=False,
            tag=f"{self.tag}_table",
            borders_innerV=self.border,
            borders_outerH=self.border,
            borders_outerV=self.border,
            width=self.w,
            # height=self.h,
            policy=sizingPolicy.get(self.sizing, dpg.mvTable_SizingStretchProp),
            pad_outerX=True,
            user_data= self.user_data
        )
        dpg.add_table_row(
            tag=f"{self.tag}_row",
            parent=f"{self.tag}_table",
        )

        self.buildColumns()
        self.addFont(tag=f"{self.tag}_table")
        self.addStyles(tag=f"{self.tag}_table")
        
        return self

    def buildColumns(self):
        for col in range(0, self._numCols):
            dpg.add_table_column(
                tag=f"{self.tag}_col_{col}",
                parent=f"{self.tag}_table",
            )

    def link(self):
        return f"{self.tag}_row"

    def Styles(self):
        dpg.highlight_table_row(f"{self.tag}_table", 0, self.bkgColor)
        DpgStyles.cellPadding(self.padding[0], self.padding[1])
