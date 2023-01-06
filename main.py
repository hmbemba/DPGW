import dearpygui.dearpygui as dpg

# from gui.Views.MainView import MyView
# from gui.DPGW.Styles import DpgStyles
# from gui.DPGW.Styles import DpgColor
from utilities import PrimaryWindow, startDPG
from grid import Grid
from Icon import Icon


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
        grid = Grid(win, cols=6, rows=6, padding=(0, 0), spacing=(10, 10))
        j = dpg.add_button(label="Hello, world")
        Icon(
            **{
                "tag": f"icon",
                "w": 0,  # 0 is default image width
                "h": 0,  # 0 is default image height
                "imagePath": "Icons/PNG/Apps.png",
            }
        ).create(Parent= win)

        dpg.set_viewport_resize_callback(grid.redraw)


start()

# import cairosvg
# cairosvg.svg2pdf(url=r'C:\Users\hmbem\Desktop\SVG\Apps.svg', write_to='image.png')