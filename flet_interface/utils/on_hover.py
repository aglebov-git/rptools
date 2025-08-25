def on_button_hover(e, page):
    '''
        This is a hover function that changes button appearance.
    '''
    if e.data == "true":
        # Background color.
        e.control.bgcolor = page.button_settings["bg_color_alt"]
        # Text color.
        e.control.content.color = page.button_settings["text_color_alt"]
    else:
        # Background color.
        e.control.bgcolor = page.button_settings["bg_color"]
        # Text color.
        e.control.content.color = page.button_settings["text_color"]
    e.control.update()