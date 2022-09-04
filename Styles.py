import dearpygui.dearpygui as dpg
from .MyColor import MyColor
from typing import TypeVar

DPG_Tag = TypeVar("DPG_Tag")


class DpgStyles:
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


class DpgColor:
    def __init__(self, color: list | str) -> None:
        if isinstance(color, str):
            self.color = MyColor.get(color)
        else:
            self.color = color

    def text(self):
        return dpg.add_theme_color(
            dpg.mvThemeCol_Text, self.color, category=dpg.mvThemeCat_Core
        )

    def textDisabled(self):
        return dpg.add_theme_color(
            dpg.mvThemeCol_TextDisabled, self.color, category=dpg.mvThemeCat_Core
        )

    def textSelectedBg(self):
        return dpg.add_theme_color(
            dpg.mvThemeCol_TextSelectedBg, self.color, category=dpg.mvThemeCat_Core
        )

    def childBg(self):
        return dpg.add_theme_color(
            dpg.mvThemeCol_ChildBg, self.color, category=dpg.mvThemeCat_Core
        )

    def windowBg(self):
        return dpg.add_theme_color(
            dpg.mvThemeCol_WindowBg, self.color, category=dpg.mvThemeCat_Core
        )

    def border(self):
        return dpg.add_theme_color(
            dpg.mvThemeCol_Border, self.color, category=dpg.mvThemeCat_Core
        )

    def frameBg(self):
        return dpg.add_theme_color(
            dpg.mvThemeCol_FrameBg, self.color, category=dpg.mvThemeCat_Core
        )

    def frameBgHovered(self):
        return dpg.add_theme_color(
            dpg.mvThemeCol_FrameBgHovered, self.color, category=dpg.mvThemeCat_Core
        )

    def frameBgActive(self):
        return dpg.add_theme_color(
            dpg.mvThemeCol_FrameBgActive, self.color, category=dpg.mvThemeCat_Core
        )

    def buttonBg(self):
        return dpg.add_theme_color(
            dpg.mvThemeCol_Button, self.color, category=dpg.mvThemeCat_Core
        )

    def buttonBgHovered(self):
        return dpg.add_theme_color(
            dpg.mvThemeCol_ButtonHovered, self.color, category=dpg.mvThemeCat_Core
        )

    def buttonBgClicked(self):
        return dpg.add_theme_color(
            dpg.mvThemeCol_ButtonActive, self.color, category=dpg.mvThemeCat_Core
        )


def addStyles(item, stylesFunction):
    with dpg.theme() as item_theme:
        with dpg.theme_component(dpg.mvAll):
            stylesFunction()
        dpg.bind_item_theme(item, item_theme)
