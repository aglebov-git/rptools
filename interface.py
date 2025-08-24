import flet as ft

from flet_interface.pages.page_main_menu import go_to_main_menu
from flet_interface.assets.settings import BUTTON_SETTINGS, HEADER_SETTINGS

async def main(page: ft.Page):
    '''
        This is a main interface function that starts whole interface.  
        Each page should always consist of:
        - Title/Header;
        - Main content of the page;
        - Button "Go Back" if user not in the main menu.
    '''
    # Page basics.
    page.title = "RP with me"
    page.button_settings = BUTTON_SETTINGS
    page.header_settings = HEADER_SETTINGS

    page.page_list = [
        
    ]

    # # Future stuff.
    # load_user_settings(page)
    # page.theme_mode = getattr(ft.ThemeMode, page.user_settings["settings"]["app_theme"])

    # Add initial page content.
    page.page_content = ft.Container(
        content=ft.Container(), # Empty placeholder.
        expand=True,
        alignment=ft.alignment.center,
    )

    # Add elements to the page.
    page.add(page.page_content)

    # Show main menu
    go_to_main_menu(page)

ft.app(main)
