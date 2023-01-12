import dearpygui.dearpygui as dpg


dpg.create_context()

def stage_items():
    with dpg.stage(tag="stage1"):
        dpg.add_text("hello, i was added from a stage", tag="text_tag")

def present_stage_items():
    dpg.move_item("text_tag", parent="main_win")

with dpg.window(label="Tutorial", tag="main_win"):
    dpg.add_button(label="stage items", callback=stage_items)
    dpg.add_button(label="present stages items", callback=present_stage_items)

dpg.show_item_registry()

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()