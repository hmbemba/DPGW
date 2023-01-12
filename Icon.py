from dataclasses import dataclass
from pathlib import Path
from textwrap import wrap
#from .Styles import DpgColor, DpgStyles
from BaseItem import BaseItem
import dearpygui.dearpygui as dpg


class NotAFileError(ValueError):
    pass

# Needs to generate the icons on the fly by converting the svg
# need to be able to determine size + color
# before dpg start need to create these icons
'''
with iconRegistry('pathToSaveIcons')
    createIcon('pathToIcon',iconName,w,h,color)


Icon(tag, iconPath)
'''

@dataclass
class Icon(BaseItem):
    '''
    You have to presize the image befoe you laod it in
    There is no real resizing
    '''
    
    """
    **{
         "tag": f"_{self.id}",
         "w": 0, # 0 is default image width
         "h": 0, # 0 is default image height
         "imagePath":"path\to\image"
    }

    """

    imagePath: str = ""
    w = 0
    h = 0

    def __post_init__(self):
        self.isFileOrError(self.imagePath)
        self.is_imageFileOrError(Path(self.imagePath).suffix)

    def isFileOrError(self,_path: Path) -> bool | NotAFileError:
        if not Path(_path).is_file():
            raise NotAFileError(_path, "This is not a valid path to a file")
        else:
            return True

    def is_imageFileOrError(self,pathSuffix: str) -> bool:
        pathSuffix = pathSuffix.lower()
        allowedSuffixes = [
            ".png",
            ".jpeg",
            ".bmp",
            ".psd",
            ".gif",
            ".hdr",
            ".pic",
            ".ppm",
            ".pgm",
            
        ]
        if not {s.lower(): True for s in allowedSuffixes}.get(pathSuffix, False):
            raise ValueError("This is not an image file")

    def Styles(self):
        ...

    def create(self, Parent=None):

        with dpg.texture_registry():
            if self.w == 0 and self.h == 0:
                width, height, channels, data = dpg.load_image(self.imagePath)
                self.w = width
                self.h = height
            else:
                _, _, _, data = dpg.load_image(self.imagePath)

            dpg.add_static_texture(
                width=self.w,
                height=self.h,
                default_value=data,
                tag=self.tag,
            )
        
        dpg.add_image(self.tag, parent=Parent)
        return self


