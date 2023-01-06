import dearpygui.dearpygui as dpg

# from gui.Views.MainView import MyView
# from gui.DPGW.Styles import DpgStyles
# from gui.DPGW.Styles import DpgColor
from utilities import PrimaryWindow, startDPG
from grid import Grid
from Icon import Icon
from Row_v2 import Row


# dpg.create_context()


@startDPG
def start():
    with dpg.font_registry():
        dpg.add_font(r"C:\Windows\Fonts\bahnschrift.ttf", 20, tag="mainFont_20")
        dpg.add_font(r"C:\Windows\Fonts\bahnschrift.ttf", 25, tag="mainFont_25")
        dpg.add_font(r"C:\Windows\Fonts\bahnschrift.ttf", 30, tag="mainFont_30")
        dpg.add_font(r"C:\Windows\Fonts\bahnschrift.ttf", 40, tag="mainFont_40")
        dpg.add_font(r"C:\Windows\Fonts\bahnschrift.ttf", 50, tag="mainFont_50")

    with PrimaryWindow(title="Main") as win:
        r = Row(
            **{
                "tag": f"row_1_",
                "numCols": 3,
                "sizing": 0,  # ,1,2,3,
                "border": True,
                "bkgColor": [255, 0, 0, 255],
                "padding": [10, 0],  # Default is [10,0]
                "user_data": None,
            }
        ).create(Parent=win)
        j = Icon(
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
