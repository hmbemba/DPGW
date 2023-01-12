import dearpygui.dearpygui as dpg
import dearpygui.demo as demo
from utilities import PrimaryWindow, startDPG

@startDPG
def start():
    with PrimaryWindow(title="Main", w=850,h=600) as win:
        demo.show_demo()

start()


