import os
import sys

try:

    from genp import password_generation
    import dearpygui.dearpygui as dpg

except:

    os.system('pip3 install genp==0.2')
    from genp import password_generation

    os.system('pip3 install dearpygui==1.8.0')
    import dearpygui.dearpygui as dpg


def create_password():
    digit = dpg.get_value('digits')
    letter = dpg.get_value('letters')
    spec_symbol = dpg.get_value('special_symbols')
    password_len = dpg.get_value('len')

    try:
        print(password_generation(digit, letter, spec_symbol, password_len))

    except:
        pass


dpg.create_context()
dpg.create_viewport(title='Password Generation', width=400, height=450)
with dpg.window(label=None, width=500, height=550, tag='Primary Window'):

    digits = dpg.add_checkbox(
        label='Digits On?', 
        tag='digits')

    letters = dpg.add_checkbox(
        label='Letters On?', 
        tag='letters')

    special_symbols = dpg.add_checkbox(
        label='Special symbols On?',
        tag='special_symbols')

    dpg.add_text('\nEnter password len:')
    user_password_len = (dpg.add_input_int(tag='len'))

    dpg.add_button(label='Create password\n',
                   callback=create_password)  # create password


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window('Primary Window', True)
dpg.start_dearpygui()
