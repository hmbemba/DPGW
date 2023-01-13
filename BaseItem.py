from dataclasses import dataclass, field, asdict
import dearpygui.dearpygui as dpg
from abc import ABCMeta, abstractmethod
from typing import List, Any
import tkinter as tk
import uuid

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


@dataclass(slots=True)
class BaseItem(metaclass=ABCMeta):
    """
    tag: str

    w: int | float = 10
    h: int | float = 10

    border: bool | int = False
    borderRadius: int = 0
    borderColor: List = field(default_factory=lambda: [0, 0, 0, 0])

    bkgColor: List = field(default_factory=lambda: [0, 0, 0, 0])

    padding: List = field(default_factory=lambda: [0, 0, 0, 0])

    callback: callable = None
    font: str = None

    onHover: str = None

    """

    tag: str

    # w h
    w: int = 10
    h: int = 10

    # Border
    border: bool = False
    borderRadius: int = 0
    borderColor: List = field(default_factory=lambda: [0, 0, 0, 0])


    bkgColor: List = field(default_factory=lambda: [0, 0, 0, 0])

    padding: List = field(default_factory=lambda: [0, 0, 0, 0])

    callback: callable = None
    
    font: str = None

    onHover: str = None
    
    user_data: Any = None
    
    parent: int = None
    
    # enabled / disabled state
    enabled: bool = True
    enabledComp: Any = 0
    disabledComp: Any = 0
    
    # ID
    id:str = ''
    stage: Any = 0
    
    """Style and Configuration Properties"""

    bkgColorDisabled: List = field(default_factory=lambda: [0, 0, 0, 0])
    bkgColorHoveredDisabled: List = field(default_factory=lambda: [0, 0, 0, 0])
    bkgColorClickedDisabled: List = field(default_factory=lambda: [0, 0, 0, 0])
    textColorDisabled: List = field(default_factory=lambda: [100,100,100,100])
    
    bkgColorHovered: List = field(default_factory=lambda: [0, 0, 0, 0])
    bkgColorClicked: List = field(default_factory=lambda: [0, 0, 0, 0])
    textColor: List = field(default_factory=lambda: [0, 0, 0, 0])

    text: str = None
    
    def getId(self):
        return uuid.uuid4()

    def getPars(self):
        return asdict(self)

    def validateParam(self, param, instance):
        if isinstance(param, instance):
            pass
        else:
            raise ValueError(
                f"The '{self.__class__}' parameter must be of type int OR float you entered : {param} which is a {type(param)}"
            )

    def mapWidthHeight(self, param) -> int | float:
        if param == 1 or isinstance(param, float):
            return screen_width * param
        else:
            return param
        
    def addStyles(self,stylesFunc:callable, item):
        with dpg.theme() as item_theme:
            with dpg.theme_component(dpg.mvAll):
                stylesFunc()
        dpg.bind_item_theme(item, item_theme)

    # def addEnabledStyles(self, tag=None):
    #     if tag:
    #         with dpg.theme() as item_theme:
    #             with dpg.theme_component(dpg.mvAll):
    #                 self.enabledStyles()
    #         dpg.bind_item_theme(tag, item_theme)
    #     else:
    #         with dpg.theme() as item_theme:
    #             with dpg.theme_component(dpg.mvAll):
    #                 self.enabledStyles()
    #         dpg.bind_item_theme(self.tag, item_theme)

    # def addDisabledStyles(self, tag=None):
    #     if tag:
    #         with dpg.theme() as item_theme:
    #             with dpg.theme_component(dpg.mvAll):
    #                 self.disabledStyles()
    #         dpg.bind_item_theme(tag, item_theme)
    #     else:
    #         with dpg.theme() as item_theme:
    #             with dpg.theme_component(dpg.mvAll):
    #                 self.disabledStyles()
    #         dpg.bind_item_theme(self.tag, item_theme)

    def addFont(self, tag=None):
        if self.font:
            if tag:
                dpg.bind_item_font(tag, self.font)
            else:
                dpg.bind_item_font(self.tag, self.font)

    def getParentWH(self):
        p = dpg.get_item_parent(self.tag)
        return (dpg.get_item_width(p), dpg.get_item_height(p))

    def deleteSelf(self) -> None:
        dpg.delete_item(self.tag)
    
    def debug(self):
        dpg.show_item_debug(self.tag)

    def onClick(self, callback):
        ...

    def setHoverCallback(self, callBack):
        with dpg.item_handler_registry() as ihr:
            if callBack == "print":
                callBack = lambda s, a, u: print(
                    f"hover_handler: {s} '\t' {a} '\t' {u}"
                )
            dpg.add_item_hover_handler(callback=callBack)
        dpg.bind_item_handler_registry(self.tag, ihr)

        # with dpg.item_handler_registry() as ihr:
        #     #dpg.add_item_clicked_handler(0, callback=lambda s, a, u: print(f"clicked_handler: {s} '\t' {a} '\t' {u}"))
        #     #dpg.add_item_clicked_handler(1, callback=lambda s, a, u: print(f"clicked_handler: {s} '\t' {a} '\t' {u}"))
        #     dpg.add_item_hover_handler(callback=lambda s, a, u: print(f"hover_handler: {s} '\t' {a} '\t' {u}"))
        # dpg.bind_item_handler_registry(self.tag, ihr)

    def disable(self):
        dpg.move_item(f"{self.tag}_disabled", before=f"{self.tag}")
        dpg.move_item(f"{self.tag}",parent= self.stage)
        self.enabled = False

        
    
    def enable(self):
        dpg.move_item(f"{self.tag}",before=f"{self.tag}_disabled")
        dpg.move_item(f"{self.tag}_disabled",parent= self.stage)
        self.enabled = True


    @abstractmethod
    def enabledStyles(self):
        ...

    @abstractmethod
    def disabledStyles(self):
        ...

    @abstractmethod
    def create(self):
        ...
    
