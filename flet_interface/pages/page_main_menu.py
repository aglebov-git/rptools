import flet as ft

from flet_interface.utils.on_hover import on_button_hover

def go_to_main_menu(page, go_to_page):
    '''
        This function builds the main menu, that consists of:
        - A Title;
        - Several buttons.
    '''
    page.header.content = ft.Container()

    title = ft.Container(
        content=ft.Text(
            value="RP With Me",
            color=page.logo_settings["text_color_alt"],
            size=page.logo_settings["text_size"],
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

        on_hover=lambda e: on_button_hover(e, page),
        on_click=lambda e: go_to_page(page, go_to_page, 1),
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

        on_hover=lambda e: on_button_hover(e, page),
        on_click=lambda e: go_to_page(page, go_to_page, 2),
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
