import dearpygui.dearpygui as dpg
from typing import TypeVar
from colour import Color


DPG_Tag = TypeVar("DPG_Tag")


class setStyles:
    def childRounding(amt):
        return dpg.add_theme_style(
            dpg.mvStyleVar_ChildRounding, amt, category=dpg.mvThemeCat_Core
        )

    def childBorderSize(amt):
        return dpg.add_theme_style(
            dpg.mvStyleVar_ChildBorderSize, amt, category=dpg.mvThemeCat_Core
        )

    def buttonTextAlign(amt1, amt2):
        return dpg.add_theme_style(
            dpg.mvStyleVar_ButtonTextAlign, amt1, amt2, category=dpg.mvThemeCat_Core
        )

    def frameBorder(val: bool):
        return dpg.add_theme_style(
            dpg.mvStyleVar_FrameBorderSize, val, category=dpg.mvThemeCat_Core
        )

    def frameRounding(amt1):
        return dpg.add_theme_style(
            dpg.mvStyleVar_FrameRounding, amt1, category=dpg.mvThemeCat_Core
        )

    def borderRadius(amt1):
        return dpg.add_theme_style(
            dpg.mvStyleVar_FrameRounding, amt1, category=dpg.mvThemeCat_Core
        )

    def indentSpacing(amt1):
        return dpg.add_theme_style(
            dpg.mvStyleVar_IndentSpacing, amt1, category=dpg.mvThemeCat_Core
        )

    def itemInnerSpacing(amt1, amt2):
        return dpg.add_theme_style(
            dpg.mvStyleVar_ItemInnerSpacing, amt1, amt2, category=dpg.mvThemeCat_Core
        )

    def itemSpacing(amt1, down: int):
        return dpg.add_theme_style(
            dpg.mvStyleVar_ItemSpacing, amt1, down, category=dpg.mvThemeCat_Core
        )

    def windowPadding(rightPositiveLeftNegative: int, downPositiveUpNegative: int):
        dpg.add_theme_style(
            dpg.mvStyleVar_WindowPadding,
            rightPositiveLeftNegative,
            downPositiveUpNegative,
            category=dpg.mvThemeCat_Core,
        )

    def windowBorder(val: bool):
        dpg.add_theme_style(
            dpg.mvStyleVar_WindowBorderSize, val, category=dpg.mvThemeCat_Core
        )

    def windowRounding(amt):
        dpg.add_theme_style(
            dpg.mvStyleVar_WindowRounding, amt, category=dpg.mvThemeCat_Core
        )

    def padding(rightPositiveLeftNegative: int, downPositiveUpNegative: int):
        return dpg.add_theme_style(
            dpg.mvStyleVar_FramePadding,
            rightPositiveLeftNegative,
            downPositiveUpNegative,
            category=dpg.mvThemeCat_Core,
        )

    def cellPadding(rightPositiveLeftNegative: int, downPositiveUpNegative: int):
        return dpg.add_theme_style(
            dpg.mvStyleVar_CellPadding,
            rightPositiveLeftNegative,
            downPositiveUpNegative,
            category=dpg.mvThemeCat_Core,
        )

class setColor:

    def textToColorList(colorname, alpha = 255) -> list:
        '''
        Converts a textual color like 'red' into a color list [r,g,b,a]
        '''
        vals = [value*255 for value in Color(colorname).rgb]
        vals.append(alpha)
        return vals
    
    def validateColorList(colorList:list):
        '''
        can only have a len of 4        
        '''
        if len(colorList) != 4:
            raise Exception(f'The color list must be 4 values [r,g,b,a] you entered {colorList} ')
        return colorList
        
    def fmtColor(color: list | str) -> list:
        '''
        takes either a list or a string and returns a valid color list 
        '''
        return setColor.textToColorList(color) if isinstance(color, str) else setColor.validateColorList(color)


    def textColor(color):
        return dpg.add_theme_color(
            dpg.mvThemeCol_Text, setColor.fmtColor(color), category=dpg.mvThemeCat_Core
        )

    def textDisabledColor(color):
        return dpg.add_theme_color(
            dpg.mvThemeCol_TextDisabled, setColor.fmtColor(color), category=dpg.mvThemeCat_Core
        )

    def textSelectedBgColor(color):
        return dpg.add_theme_color(
            dpg.mvThemeCol_TextSelectedBg, setColor.fmtColor(color), category=dpg.mvThemeCat_Core
        )

    def childBgColor(color):
        return dpg.add_theme_color(
            dpg.mvThemeCol_ChildBg, setColor.fmtColor(color), category=dpg.mvThemeCat_Core
        )

    def windowBgColor(color):
        return dpg.add_theme_color(
            dpg.mvThemeCol_WindowBg, setColor.fmtColor(color), category=dpg.mvThemeCat_Core
        )

    def borderColor(color):
        return dpg.add_theme_color(
            dpg.mvThemeCol_Border, setColor.fmtColor(color), category=dpg.mvThemeCat_Core
        )

    def frameBgColor(color):
        return dpg.add_theme_color(
            dpg.mvThemeCol_FrameBg, setColor.fmtColor(color), category=dpg.mvThemeCat_Core
        )

    def frameBgHoveredColor(color):
        return dpg.add_theme_color(
            dpg.mvThemeCol_FrameBgHovered, setColor.fmtColor(color), category=dpg.mvThemeCat_Core
        )

    def frameBgActiveColor(color):
        return dpg.add_theme_color(
            dpg.mvThemeCol_FrameBgActive, setColor.fmtColor(color), category=dpg.mvThemeCat_Core
        )

    def buttonBgColor(color):
        return dpg.add_theme_color(
            dpg.mvThemeCol_Button, setColor.fmtColor(color), category=dpg.mvThemeCat_Core
        )

    def buttonBgHoveredColor(color):
        return dpg.add_theme_color(
            dpg.mvThemeCol_ButtonHovered, setColor.fmtColor(color), category=dpg.mvThemeCat_Core
        )

    def buttonBgClickedColor(color):
        return dpg.add_theme_color(
            dpg.mvThemeCol_ButtonActive, setColor.fmtColor(color), category=dpg.mvThemeCat_Core
        )


def addStyles(item, stylesFunction):
    with dpg.theme() as item_theme:
        with dpg.theme_component(dpg.mvAll):
            stylesFunction()
        dpg.bind_item_theme(item, item_theme)
