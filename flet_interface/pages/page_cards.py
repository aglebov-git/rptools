import flet as ft

from flet_interface.utils.back_button import make_go_back_button
from flet_interface.utils.header import make_header
from flet_interface.utils.make_cards_list import make_cards_list

def go_to_cards_page(page, go_to_page):
    go_back_button = make_go_back_button(page, go_to_page, 0)
    header_text = "Cards page"

    cards_list = ft.Container(
        content=ft.Row(
            controls=make_cards_list(page, go_to_page),
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        ),
        bgcolor=ft.Colors.AMBER_200,
    )

    page_cards_controls = [
        cards_list,
    ]

    page_cards = ft.Column(
        controls=page_cards_controls,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    page.header.content = make_header(page, header_text, go_back_button)
    page.page_content.content = page_cards
    page.footer.content = ft.Container()

    page.update()
