import flet as ft

from flet_interface.utils.on_hover import on_button_hover

def make_go_back_button(page, go_to_page, index):
    '''
        This function returns a button that leads to a certain index.
    '''
    button = ft.Container(
        content=ft.Text(
            value="Go Back",
            size=page.button_settings["text_size"],
            color=page.button_settings["text_color"],
        ),
        height=page.button_settings["height_back_button"],
        width=page.button_settings["width_back_button"],

        border_radius=16,
        bgcolor=page.button_settings["bg_color"],
        alignment=ft.alignment.center,

        on_hover=lambda e: on_button_hover(e, page),
        on_click=lambda e: go_to_page(page, go_to_page, index)
    )

    return button
