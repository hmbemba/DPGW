import dearpygui.dearpygui as dpg
from utilities import PrimaryWindow, startDPG
from Icon import Icon
from Row import Row
from Button import Button
from Container import Container
from Themes import theme, loudContainer, blue
from ThemedComponents import *


@startDPG
def start():
    
    theme.font.loadFont()

    with PrimaryWindow(title="Main", w=850, h=600, itemRegistry=False) as win:
        with row('r1', 2).create(Parent=win) as r:
            p = primaryBtn('r1', 'Click To Disable', callback= lambda: d.disable() if d.enabled else d.enable()).create(Parent=r.link())
            d = successBtn('g1', 'Enabled',callback = lambda: p.disable() if p.enabled else p.enable()).create(Parent=r.link())
        w = warningBtn('w1', 'THIS IS A WARNING!').create(Parent=win)

start()


# import cairosvg
# cairosvg.svg2pdf(url=r'C:\Users\hmbem\Desktop\SVG\Apps.svg', write_to='image.png')
