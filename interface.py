import os
import flet as ft

from flet_interface.utils.go_to_page import go_to_page
from flet_interface.utils.load_characters import load_characters

from flet_interface.assets.settings import BUTTON_SETTINGS, HEADER_SETTINGS, LOGO_SETTINGS, REGULAR_SETTINGS

os.environ["FLET_SECRET_KEY"] = "dev-secret-12345"

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
    page.logo_settings = LOGO_SETTINGS
    page.regular_settings = REGULAR_SETTINGS
    page.characters = load_characters()
    page.upload_targets = {}

    # for character in page.characters:
    #     print(character["name"])

    page.file_picker = ft.FilePicker()
    page.overlay.append(page.file_picker)

    # # Future stuff.
    # load_user_settings(page)
    # page.theme_mode = getattr(ft.ThemeMode, page.user_settings["settings"]["app_theme"])

    # Initial page header.
    page.header = ft.Container()

    # Add initial page content.
    page.page_content = ft.Container(
        content=ft.Container(), # Empty placeholder.
        expand=True,
        alignment=ft.alignment.center,
    )

    # Initial page footer.
    page.footer = ft.Container(alignment=ft.alignment.center,)

    # Add elements to the page.
    page.add(
        page.header,
        page.page_content,
        page.footer,
    )

    # Show main menu
    go_to_page(page, go_to_page, 0)

ft.app(
    main,
    upload_dir="flet_interface/assets/uploads",
)
