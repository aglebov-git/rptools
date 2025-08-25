from flet_interface.pages.page_card import go_to_card_page
from flet_interface.pages.page_cards import go_to_cards_page
from flet_interface.pages.page_main_menu import go_to_main_menu
from flet_interface.pages.page_settings import go_to_settings_page

def go_to_page(page, go_to_page, index, card_name=""):
    if index == 0:
        go_to_main_menu(page, go_to_page)
    elif index == 1:
        go_to_cards_page(page, go_to_page)
    elif index == 2:
        go_to_settings_page(page, go_to_page)
    elif index == 3:
        go_to_card_page(page, go_to_page, card_name)
