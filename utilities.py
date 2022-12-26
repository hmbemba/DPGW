from contextlib import contextmanager
import dearpygui.dearpygui as dpg
import tkinter as tk


root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

@contextmanager
def PrimaryWindow(title = "Primary Window", w = int(screen_width*1), h = int(screen_height*1)):
    try:
        widget = dpg.add_window(tag="PrimaryWindow" , no_scrollbar=True)
        dpg.create_viewport(title=title, width=w, height=h)
        dpg.push_container_stack(widget)
        yield widget
    finally:
        dpg.pop_container_stack()


