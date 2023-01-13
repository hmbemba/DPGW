from dataclasses import dataclass, field, asdict
import dearpygui.dearpygui as dpg
from abc import ABCMeta, abstractmethod
from typing import List, Any
import uuid




@dataclass(slots=True)
class BaseItem(metaclass=ABCMeta):

    tag: str
    
    '''
    MetaData
    '''
    id:str = ''
    parent: int = None
    stage: Any = 0
    user_data: Any = None
    
    
    '''
    enabled / disabled state
    '''
    enabled: bool = True
    enabledComp: Any = 0
    disabledComp: Any = 0
    
    
    '''
    Base Data
    '''
    w: int = 10
    h: int = 10
    callback: callable = None
    onHover: callable = None
    
    '''
    Style Data
    '''
    # Enabled
    bkgColor: List = field(default_factory=lambda: [0, 0, 0, 0])
    bkgColorHovered: List = field(default_factory=lambda: [0, 0, 0, 0])
    bkgColorClicked: List = field(default_factory=lambda: [0, 0, 0, 0])
    textColor: List = field(default_factory=lambda: [0, 0, 0, 0])
    
    # Disabled
    bkgColorDisabled: List = field(default_factory=lambda: [0, 0, 0, 0])
    bkgColorHoveredDisabled: List = field(default_factory=lambda: [0, 0, 0, 0])
    bkgColorClickedDisabled: List = field(default_factory=lambda: [0, 0, 0, 0])
    textColorDisabled: List = field(default_factory=lambda: [100,100,100,100])
    
    # Border
    border: bool = False
    borderRadius: int = 0
    borderColor: List = field(default_factory=lambda: [0, 0, 0, 0])

    # Other
    padding: List = field(default_factory=lambda: [0, 0, 0, 0])
    font: str = None

    
    '''
    Button Related Attributes
    '''
    text: str = None
    
    '''
    Row Related Attributes
    '''
    numCols : int = 0
    w: int = 0 
    sizing: int = 0
    
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

        
    def addStyles(self,stylesFunc:callable, item):
        with dpg.theme() as item_theme:
            with dpg.theme_component(dpg.mvAll):
                stylesFunc()
        dpg.bind_item_theme(item, item_theme)

    def addFont(self, tag=None):
        if self.font:
            if tag:
                dpg.bind_item_font(tag, self.font)
            else:
                dpg.bind_item_font(self.tag, self.font)
    
    def debug(self, tag) -> None:
        dpg.show_item_debug(tag)


    def setHoverCallback(self, tag, callBack):
        with dpg.item_handler_registry() as ihr:
            if callBack == "print":
                callBack = lambda id, tag,: print(
                    f"hover_handler: id: {id} | tag: {tag} "
                )
            dpg.add_item_hover_handler(callback=callBack)
        dpg.bind_item_handler_registry(tag, ihr)


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
    
