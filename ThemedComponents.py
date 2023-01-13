from Icon import Icon
from Row import Row
from Button import Button
from Container import Container
from Themes import theme


row = lambda tag,numCols: Row(**{
            "tag": tag,
            "numCols":numCols,
            "sizing":0, #,1,2,3,
            "border":True,
            "bkgColor":theme.bkg.dark,
            "padding": [10,10], # Default is [10,0]
            "user_data": None,
        }
    )

primaryBtn = lambda tag, text, callback = None: Button(
                    **{
                    "tag": tag,
                    "w": -1,
                    "h": 100,
                    "text": text,
                    "textColor": theme.text.active,
                    "font": theme.font.med,
                    "callback": callback, 
                    "user_data": ...,
                    "border": False,
                    "borderRadius": 0,
                    "borderColor": [0,0,0,0], 
                    "bkgColor": theme.primary.active,
                    "bkgColorHovered": theme.primary.hovered,
                    'bkgColorClicked': theme.primary.clicked,
                    "bkgColorDisabled": theme.primary.disabled,
                    "bkgColorHoveredDisabled": theme.primary.disabled,
                    'bkgColorClickedDisabled': theme.primary.disabled,
                    "padding": [0,0] ,
                    }
)

warningBtn = lambda tag, text, callback = None: Button(
                    **{
                    "tag": tag,
                    "w": -1,
                    "h": 100,
                    "text": text,
                    "textColor": theme.text.active,
                    "font": theme.font.med,
                    "callback": callback, 
                    "user_data": ...,
                    "border": False,
                    "borderRadius": 0,
                    "borderColor": [0,0,0,0], 
                    "bkgColor": theme.warning.active,
                    "bkgColorHovered": theme.warning.hovered,
                    'bkgColorClicked': theme.warning.clicked,
                    "bkgColorDisabled": theme.warning.disabled,
                    "bkgColorHoveredDisabled": theme.warning.disabled,
                    'bkgColorClickedDisabled': theme.warning.disabled,
                    "padding": [0,0] ,
                    }
)

successBtn = lambda tag, text, callback = None: Button(
                    **{
                    "tag": tag,
                    "w": -1,
                    "h": 100,
                    "text": text,
                    "textColor": theme.text.active,
                    "font": theme.font.med,
                    "callback": callback, 
                    "user_data": ...,
                    "border": False,
                    "borderRadius": 0,
                    "borderColor": [0,0,0,0], 
                    "bkgColor": theme.success.active,
                    "bkgColorHovered": theme.success.hovered,
                    'bkgColorClicked': theme.success.clicked,
                    "bkgColorDisabled": theme.success.disabled,
                    "bkgColorHoveredDisabled": theme.success.disabled,
                    'bkgColorClickedDisabled': theme.success.disabled,
                    "padding": [0,0] ,
                    }
)
