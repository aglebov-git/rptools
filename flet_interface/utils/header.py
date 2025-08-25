import flet as ft

def make_header(page, text, go_back_button):
    header = ft.Row(
        controls=[
            ft.Container(width=page.button_settings["width_back_button"]),
            ft.Text(
                value=text,
                size=page.header_settings["text_size"],
                color=page.header_settings["text_color_alt"]
            ),
            go_back_button,
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        expand=True
    )

    return header
