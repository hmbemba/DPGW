from abc import ABCMeta, abstractmethod
import dearpygui.dearpygui as dpg
from dataclasses import dataclass, field, asdict
import uuid


@dataclass
class BaseView(metaclass=ABCMeta):
    '''
    Implement This
@dataclass
class MyView(BaseView):
    def __post_init__(self):
        self.id = self.getId()
        with dpg.stage(tag=f"Stage_{self.id}"):
            self.top = Container(
                **{
                    "tag": f"top_{self.id}",
                    "w": 0,
                    "h": 0,
                    "autoSizeX": True,
                    "autoSizeY": True,
                    "itemOrientation": "col",
                    # 'horzGap': 50,
                    "border": True,
                    # "bkgColor": [117, 50, 249],
                    "borderColor": [255, 0, 0, 0],
                    # 'borderRadius': 10,
                    "padding": [5, 50],
                    "verticalItemSpacing": [0, 10],
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
