from abc import ABCMeta
import dearpygui.dearpygui as dpg
from dataclasses import dataclass
import uuid


@dataclass
class BaseView(metaclass=ABCMeta):
    '''
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
    windowTag: str

    def getId(self):
        return uuid.uuid4()
    

    def show(self):
        dpg.push_container_stack(self.windowTag)
        dpg.unstage(f"Stage_{self.id}")
        dpg.pop_container_stack()
    
    '''
    Implement functionality to delete the view itself
    '''
    def hide(self):
        dpg.delete_item(self.windowTag, children_only=True)

    def setNextPage(self, View):
        self.gotoNextPage = View.show 

    def nextPageBtnClicked(self):
        self.hide()
        try:
            self.gotoNextPage()
        except Exception as e:
            raise e

    def refreshPage(self):
        self.hide()
        self.show()

    def auto_align(self,item, alignment_type: int, x_align: float = 0.5, y_align: float = 0.5):
        def _center_h(_s, _d, data):
            parent = dpg.get_item_parent(data[0])
            while dpg.get_item_info(parent)['type'] != "mvAppItemType::mvWindowAppItem":
                parent = dpg.get_item_parent(parent)
            parentWidth = dpg.get_item_rect_size(parent)[0]
            width = dpg.get_item_rect_size(data[0])[0]
            newX = (parentWidth // 2 - width // 2) * data[1] * 2
            dpg.set_item_pos(data[0], [newX, dpg.get_item_pos(data[0])[1]])

        def _center_v(_s, _d, data):
            parent = dpg.get_item_parent(data[0])
            while dpg.get_item_info(parent)['type'] != "mvAppItemType::mvWindowAppItem":
                parent = dpg.get_item_parent(parent)
            parentWidth = dpg.get_item_rect_size(parent)[1]
            height = dpg.get_item_rect_size(data[0])[1]
            newY = (parentWidth // 2 - height // 2) * data[1] * 2
            dpg.set_item_pos(data[0], [dpg.get_item_pos(data[0])[0], newY])

        if 0 <= alignment_type <= 2:
            with dpg.item_handler_registry():
                if alignment_type == 0:
                    # horizontal only alignment
                    dpg.add_item_visible_handler(callback=_center_h, user_data=[item, x_align])
                elif alignment_type == 1:
                    # vertical only alignment
                    dpg.add_item_visible_handler(callback=_center_v, user_data=[item, y_align])
                elif alignment_type == 2:
                    # both horizontal and vertical alignment
                    dpg.add_item_visible_handler(callback=_center_h, user_data=[item, x_align])
                    dpg.add_item_visible_handler(callback=_center_v, user_data=[item, y_align])

            dpg.bind_item_handler_registry(item, dpg.last_container())
    
    def centerTop(self,item):
        self.auto_align(item, 0)
        
    def centerLeft(self,item):
        self.auto_align(item, 1)
        
    def centerMiddle(self,item):
        self.auto_align(item, 2)

