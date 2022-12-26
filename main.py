import dearpygui.dearpygui as dpg
# from gui.Views.MainView import MyView
# from gui.DPGW.Styles import DpgStyles
# from gui.DPGW.Styles import DpgColor
from utilities import PrimaryWindow




dpg.create_context()

with dpg.font_registry():
    dpg.add_font(r"C:\Windows\Fonts\bahnschrift.ttf", 20, tag="mainFont_20")
    dpg.add_font(r"C:\Windows\Fonts\bahnschrift.ttf", 25, tag="mainFont_25")
    dpg.add_font(r"C:\Windows\Fonts\bahnschrift.ttf", 30, tag="mainFont_30")
    dpg.add_font(r"C:\Windows\Fonts\bahnschrift.ttf", 40, tag="mainFont_40")
    dpg.add_font(r"C:\Windows\Fonts\bahnschrift.ttf", 50, tag="mainFont_50")

# with dpg.window(tag="Primary Window", no_scrollbar=True):
#     ...

# with PrimaryWindow() as pw:
#     dpg.add_text(default_value = "Hello, world", parent = pw.tag)

with PrimaryWindow(title="Main"):
    dpg.add_text(default_value = "Hello, world")
    # #Define Views
    # view = MyView()


    # # Show Starting View
    # view.show()


# with dpg.theme() as item_theme:
#     with dpg.theme_component(dpg.mvAll):
#         DpgStyles.windowPadding(0,0)
#         DpgColor([31, 31, 31, 255]).windowBg()
# dpg.bind_item_theme("Primary Window", item_theme)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("PrimaryWindow", True)
dpg.start_dearpygui()
dpg.destroy_context()


