import dearpygui.dearpygui as dpg
# from gui.Views.MainView import MyView
# from gui.DPGW.Styles import DpgStyles
# from gui.DPGW.Styles import DpgColor
from utilities import PrimaryWindow, startDPG
from grid import Grid




#dpg.create_context()



@startDPG
def start():
    with dpg.font_registry():
        dpg.add_font(r"C:\Windows\Fonts\bahnschrift.ttf", 20, tag="mainFont_20")
        dpg.add_font(r"C:\Windows\Fonts\bahnschrift.ttf", 25, tag="mainFont_25")
        dpg.add_font(r"C:\Windows\Fonts\bahnschrift.ttf", 30, tag="mainFont_30")
        dpg.add_font(r"C:\Windows\Fonts\bahnschrift.ttf", 40, tag="mainFont_40")
        dpg.add_font(r"C:\Windows\Fonts\bahnschrift.ttf", 50, tag="mainFont_50")

    with PrimaryWindow(title="Main") as win:
        grid = Grid(win, cols=6, rows=6, padding=(0,0), spacing=(10,10))
        j = dpg.add_button(label = "Hello, world")
        #grid.pack(j,5,0)


        dpg.set_viewport_resize_callback(grid.redraw)

start()

    
    



