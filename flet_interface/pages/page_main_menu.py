import flet as ft

from flet_interface.pages.page_settings import go_to_settings_page
from flet_interface.pages.page_cards import go_to_cards_page

def go_to_main_menu(page):
    '''
        This function builds the main menu, that consists of:
        - A Title;
        - Several buttons.
    '''
    def on_button_hover(e):
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

    title = ft.Container(
        content=ft.Text(
            value="RP With Me",
            color=page.header_settings["text_color_alt"],
            size=page.header_settings["text_size"],
        ),
        # bgcolor=ft.Colors.AMBER_200,
    )

    cards_button = ft.Container(
        content=ft.Text(
            value="Cards",
            size=page.button_settings["text_size"],
            color=page.button_settings["text_color"],
        ),
        height=page.button_settings["height"],
        width=page.button_settings["width"],

        border_radius=16,
        bgcolor=page.button_settings["bg_color"],
        alignment=ft.alignment.center,

        on_hover=on_button_hover,
        on_click=lambda e: go_to_cards_page(page)
    )

    settings_button = ft.Container(
        content=ft.Text(
            value="Settings",
            size=page.button_settings["text_size"],
            color=page.button_settings["text_color"],
        ),
        height=page.button_settings["height"],
        width=page.button_settings["width"],

        border_radius=16,
        bgcolor=page.button_settings["bg_color"],
        alignment=ft.alignment.center,

        on_hover=on_button_hover,
        on_click=lambda e: go_to_settings_page(page),
    )

    menu_controls = [
        title,
        cards_button,
        settings_button,
    ]

    page_main_menu = ft.Column(
        controls=menu_controls,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    page.page_content.content = page_main_menu
    page.update()
