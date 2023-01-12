import dearpygui.dearpygui as dpg
from utilities import PrimaryWindow, startDPG
from Icon import Icon
from Row import Row
from Button import Button
from Container import Container
from Themes import theme, loudContainer, blue

@startDPG
def start():
    
    theme.font.loadFont()

    with PrimaryWindow(title="Main", w=850, h=600, debug=False) as win:
        ...
    #     top = Container(**loudContainer("top"))  # .create(Parent=win)

    #     r = Row(
    #         **{
    #             "tag": f"row_1_",
    #             "numCols": 3,
    #             "sizing": 3,  # ,1,2,3,
    #             "border": True,
    #             "bkgColor": theme.bkg.dark,
    #             "padding": [10, 10],  # Default is [10,0]
    #             "user_data": None,
    #         }
    #     ).create(Parent=top.link())
        
    #     b = Button(
    #             **{
    #     "tag": f"btn",
    #     "w": -1,
    #     "h": 100,
    #     "text": "Btn Text",
    #     "textColor": [255,255,255,255],#"white",
    #     "font": theme.font.med,
    #     "callback": None, #self.autoFind,
    #     "user_data": ...,
    #     "border": False,
    #     "borderRadius": 0,
    #     "borderColor": [0,0,0,0], #'red',
    #     "bkgColor": theme.primary.active,
    #     "bkgColorHovered": theme.primary.hovered,#[37 * 0.7, 37 * 0.7, 38 * 0.7, 255],
    #     'bkgColorClicked': theme.primary.clicked,#'green',
    #     "padding": [0,0] ,#[10, 10],
    # }
    #     ).create(Parent=r.link())

start()


# import cairosvg
# cairosvg.svg2pdf(url=r'C:\Users\hmbem\Desktop\SVG\Apps.svg', write_to='image.png')
