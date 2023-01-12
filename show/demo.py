import dearpygui.dearpygui as dpg
import dearpygui.demo as demo

import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from utilities import PrimaryWindow, startDPG

@startDPG
def start():
    with PrimaryWindow(title="Main", w=850,h=600, itemRegistry=True) as win:
        demo.show_demo()

start()


