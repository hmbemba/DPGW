import dearpygui.dearpygui as dpg
from utilities import PrimaryWindow, startDPG
from Icon import Icon
from Row import Row
from Button import Button
from Container import Container


@startDPG
def start():
    with dpg.font_registry():
        dpg.add_font(r"C:\Windows\Fonts\bahnschrift.ttf", 20, tag="mainFont_20")
        dpg.add_font(r"C:\Windows\Fonts\bahnschrift.ttf", 25, tag="mainFont_25")
        dpg.add_font(r"C:\Windows\Fonts\bahnschrift.ttf", 30, tag="mainFont_30")
        dpg.add_font(r"C:\Windows\Fonts\bahnschrift.ttf", 40, tag="mainFont_40")
        dpg.add_font(r"C:\Windows\Fonts\bahnschrift.ttf", 50, tag="mainFont_50")

    with PrimaryWindow(title="Main", w=850,h=600, debug=False) as win:
        top = Container(
                    **{
            "tag": f"top_",
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
            "borderColor": "grey",#[0, 0, 0, 255],  # "orange",
            "bkgColor": [0, 0, 255,0],
            "padding": [0,0],  # [LR,TB] !Can also be negative
            "onHover": None,
            "noScrollBar": True,
            "font": None,  # "main_20"
        }
        ).create(Parent=win)
        r = Row(
            **{
                "tag": f"row_1_",
                "numCols": 3,
                "sizing": 3,  # ,1,2,3,
                "border": True,
                "bkgColor": [255, 255, 0, 5],
                "padding": [10, 0],  # Default is [10,0]
                "user_data": None,
            }
        ).create(Parent=top.link())

        Button(
            **{
                "tag": f"b1",
                "w": -1,
                "h": 100,
                "text": "Btn Text",
                "textColor": [255, 255, 255, 255],  # "white",
                "font": "mainFont_50",
                "callback": None,  # self.autoFind,
                "user_data": ...,
                "border": False,
                "borderRadius": 0,
                "borderColor": [0, 0, 0, 0],  #'red',
                "bkgColor": [0, 0, 0, 0],
                "bkgColorHovered": [0, 0, 0, 0],  # [37 * 0.7, 37 * 0.7, 38 * 0.7, 255],
                "bkgColorClicked": [0, 0, 0, 0],  #'green',
                "padding": [0, 0],  # [10, 10],
            }
        )#.create(r.link())
        
        #dpg.add_spacer(parent=r.link(), width=100)
        
        Button(
            **{
                "tag": f"b2",
                "w": -1,
                "h": 100,
                "text": "Btn Text",
                "textColor": [255, 255, 255, 255],  # "white",
                "font": "mainFont_50",
                "callback": None,  # self.autoFind,
                "user_data": ...,
                "border": False,
                "borderRadius": 0,
                "borderColor": [0, 0, 0, 0],  #'red',
                "bkgColor": [0, 0, 0, 0],
                "bkgColorHovered": [0, 0, 0, 0],  # [37 * 0.7, 37 * 0.7, 38 * 0.7, 255],
                "bkgColorClicked": [0, 0, 0, 0],  #'green',
                "padding": [0, 0],  # [10, 10],
            }
        ).create(r.link())
        
        k =dpg.add_loading_indicator(parent=r.link(), radius=10)
        
        I = Icon(
            **{
                "tag": f"icon",
                "w": 0,  # 0 is default image width
                "h": 0,  # 0 is default image height
                "imagePath": "Icons/PNG/Apps.png",
            }
        ).create(Parent=r.link())
        
           
        #I.debug()
        #dpg.show_item_debug(I.tag)
        #dpg.show_item_registry()
        #dpg.show_metrics()
        
        


start()


# import cairosvg
# cairosvg.svg2pdf(url=r'C:\Users\hmbem\Desktop\SVG\Apps.svg', write_to='image.png')
