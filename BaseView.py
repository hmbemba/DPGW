from abc import ABCMeta, abstractmethod
import dearpygui.dearpygui as dpg
from dataclasses import dataclass, field, asdict
import uuid


@dataclass
class BaseView(metaclass=ABCMeta):
    '''
from dataclasses import dataclass
from DPGW.BaseView import BaseView
from DPGW.Container import Container
import dearpygui.dearpygui as dpg

from dataclasses import dataclass
from gui.DPGW.BaseView import BaseView
from gui.DPGW.Container import Container
import dearpygui.dearpygui as dpg


@dataclass
class MyView(BaseView):
    def __post_init__(self):
        self.id = self.getId()
        with dpg.stage(tag=f"Stage_{self.id}"):
            self.top = Container(
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
                    "bkgColor": [0, 0, 255, 255],
                    "padding": [0, 0],  # [LR,TB] !Can also be negative
                    "onHover": None,
                    "noScrollBar": True,
                    "font": None,  # "main_20"
                }
            ).create()
    
    '''

    def getId(self):
        return uuid.uuid4()
    
    # @abstractmethod
    # def show(self):
    #     ...
    def show(self):
        dpg.push_container_stack("Primary Window")
        dpg.unstage(f"Stage_{self.id}")
        dpg.pop_container_stack()
    

        

    '''
    Implement functionality to delete the view itself
    '''
    def hide(self):
        dpg.delete_item("Primary Window", children_only=True)

    def setNextPage(self, View):
        self.gotoNextPage = View.show 

    def nextPageBtnClicked(self):
        self.hide()
        try:
            self.gotoNextPage()
        except AttributeError as e:
            raise e
            print(e)
            print(f'''
There is no next page set for {self}! 
Make sure you implement {self}.setNextPage()
''')


    def refreshPage(self):
        self.hide()
        self.show()
