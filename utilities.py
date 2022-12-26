from contextlib import contextmanager
import dearpygui.dearpygui as dpg
from contextlib import ContextDecorator

class PrimaryWindow(ContextDecorator):
    def __init__(self) -> None:
        self.tag = "PrimaryWindow"        
    def __enter__(self):
        dpg.add_window(tag=self.tag, no_scrollbar=True)
        
        return self

    def __exit__(self, *exc):
        return False
    
    def __repr__(self) -> str:
        return self.tag

