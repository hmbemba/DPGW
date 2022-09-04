import dearpygui.dearpygui as dpg
from GUI.Views.SelectVideoView import SelectVideoView
from GUI.MyDPG.Styles import DpgColor, addStyles, DpgStyles
from GUI.Views.ClientFormView import ClientFormView
from GUI.Views.ProcessingVideoView import ProcessingVideoView
#from GUI.Views.SelectSongView import SelectSongView
# from GUI.Views.ShareVideoView import ShareVideoView
import tkinter as tk


root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

dpg.create_context()

with dpg.font_registry():
    dpg.add_font(r"C:\Windows\Fonts\bahnschrift.ttf", 20, tag="mainFont_20")
    dpg.add_font(r"C:\Windows\Fonts\bahnschrift.ttf", 25, tag="mainFont_25")
    dpg.add_font(r"C:\Windows\Fonts\bahnschrift.ttf", 30, tag="mainFont_30")
    dpg.add_font(r"C:\Windows\Fonts\bahnschrift.ttf", 40, tag="mainFont_40")
    dpg.add_font(r"C:\Windows\Fonts\bahnschrift.ttf", 50, tag="mainFont_50")

with dpg.window(tag="Primary Window", no_scrollbar=True):
    
    #Define Views
    svv = SelectVideoView()
    cfv = ClientFormView()
    #ssv = SelectSongView()
    pvv = ProcessingVideoView()
    # shvv = ShareVideoView()

    # Configure View Routing
    svv.setNextPage(cfv)
    cfv.setNextPage(pvv)
    # ssv.setNextPage(pvv)
    pvv.setNextPage(svv)
    # shvv.setNextPage(svv)

    # Show Starting View
    svv.show()


with dpg.theme() as item_theme:
    with dpg.theme_component(dpg.mvAll):
        DpgStyles.windowPadding(0,0)
        DpgColor([31, 31, 31, 255]).windowBg()
dpg.bind_item_theme("Primary Window", item_theme)

dpg.create_viewport(title="RevOH", width=int(screen_width*1), height=int(screen_height*1))
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()


