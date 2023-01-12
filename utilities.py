from contextlib import contextmanager
import dearpygui.dearpygui as dpg
import tkinter as tk
from functools import wraps


root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

@contextmanager
def PrimaryWindow(
        title = "Primary Window", 
        w = int(screen_width*1),
        h = int(screen_height*1),
        metrics = False,
        itemRegistry = False,
        styleEditor = False,
        fontManager = False,
        debug = False
        
        
        ):
    try:
        widget = dpg.add_window(tag="PrimaryWindow" , no_scrollbar=True)
        dpg.set_primary_window("PrimaryWindow", True)
        dpg.create_viewport(title=title, width=w, height=h)
        dpg.push_container_stack(widget)
        yield widget
        
        if metrics:
            dpg.show_metrics()
        if itemRegistry:
            dpg.show_item_registry()
        if styleEditor:
            dpg.show_style_editor()     
        if fontManager:
            dpg.show_font_manager()
        if debug:
            dpg.show_debug()
    finally:
        dpg.pop_container_stack()
        

# @contextmanager
# def StartDPG():
#     try:
#         # widget = dpg.add_window(tag="PrimaryWindow" , no_scrollbar=True)
#         # dpg.set_primary_window("PrimaryWindow", True)
#         # dpg.create_viewport(title=title, width=w, height=h)
#         # dpg.push_container_stack(widget)
#         # yield widget
#         dpg.create_context()
#         dpg.setup_dearpygui()
#         dpg.show_viewport()
#         dpg.set_viewport_resize_callback(grid.redraw)
#         dpg.start_dearpygui()
#         dpg.destroy_context()

#     finally:
#         dpg.pop_container_stack()

# def startDPG(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         dpg.create_context()
#         fn(*args, **kwargs)
        

#     return wrapper    

def startDPG(func):
    @wraps(func)
    def wrapper():
        dpg.create_context()
        func()
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()    
    return wrapper


