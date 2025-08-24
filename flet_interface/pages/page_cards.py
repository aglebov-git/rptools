import flet as ft

def go_to_cards_page(page):
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

    print("Hello from cards page")
    print(page.page_content)

    go_back_button = ft.Container(
        content=ft.Text(
            value="Go Back",
            size=page.button_settings["text_size"],
            color=page.button_settings["text_color"],
        ),
        height=page.button_settings["height"],
        width=page.button_settings["width"],

        border_radius=16,
        bgcolor=page.button_settings["bg_color"],
        alignment=ft.alignment.center,

        on_hover=on_button_hover,
        # on_click=lambda e: go_to_cards_page(page)
    )

    header = ft.Row(
        controls=[
            ft.Text(
                value="Cards page"
            ),
            go_back_button,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    page_cards_controls = [
        header,
    ]

    page_cards = ft.Column(
        controls=page_cards_controls,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    page.page_content.content = page_cards
    page.update()
