import dearpygui.dearpygui as dpg
from utilities import PrimaryWindow, startDPG
from Icon import Icon
from Row import Row
from Button import Button


@startDPG
def start():
    with dpg.font_registry():
        dpg.add_font(r"C:\Windows\Fonts\bahnschrift.ttf", 20, tag="mainFont_20")
        dpg.add_font(r"C:\Windows\Fonts\bahnschrift.ttf", 25, tag="mainFont_25")
        dpg.add_font(r"C:\Windows\Fonts\bahnschrift.ttf", 30, tag="mainFont_30")
        dpg.add_font(r"C:\Windows\Fonts\bahnschrift.ttf", 40, tag="mainFont_40")
        dpg.add_font(r"C:\Windows\Fonts\bahnschrift.ttf", 50, tag="mainFont_50")

    with PrimaryWindow(title="Main", w=850,h=600) as win:
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
        ).create(Parent=win)

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
        
        dpg.add_loading_indicator(parent=r.link(), radius=10)
        
        Icon(
            **{
                "tag": f"icon",
                "w": 0,  # 0 is default image width
                "h": 0,  # 0 is default image height
                "imagePath": "Icons/PNG/Apps.png",
            }
        ).create(Parent=r.link())


start()

# import cairosvg
# cairosvg.svg2pdf(url=r'C:\Users\hmbem\Desktop\SVG\Apps.svg', write_to='image.png')
