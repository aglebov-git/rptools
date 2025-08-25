import flet as ft

from flet_interface.utils.on_hover import on_button_hover

def make_cards_list(page, go_to_page):
    print("[DEBUG] Requested to make cards list.")
    # Import existing cards.
    cards_list = []
    # if page.characters:
    #     for card in page.characters:
    #         cards_list.append(card)

    make_new_card_button = ft.Container(
        content=ft.Text(
            value="+",
            size=page.button_settings["text_size"],
            color=page.button_settings["text_color"],
        ),
        height=page.button_settings["height_new_card"],
        width=page.button_settings["width_new_card"],

        border_radius=16,
        bgcolor=page.button_settings["bg_color"],
        alignment=ft.alignment.center,

        on_hover=lambda e: on_button_hover(e, page),
        on_click=lambda e: go_to_page(page, go_to_page, 3),
    )
    cards_list.append(make_new_card_button)

    return cards_list