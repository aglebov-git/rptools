import flet as ft

from flet_interface.utils.back_button import make_go_back_button
from flet_interface.utils.header import make_header
from flet_interface.utils.save_character import save_character

def go_to_card_page(page, go_to_page, card_name):
    print("[DEBUG] You are in the Card page!")

    # Always head back to the cards list.
    go_back_button = make_go_back_button(page, go_to_page, 1)

    if card_name == "":
        header_text = "New Card"
    else:
        header_text = "Card " + card_name
    
    name_ref   = ft.Ref[ft.TextField]()
    level_ref  = ft.Ref[ft.TextField]()
    class_ref  = ft.Ref[ft.TextField]()
    history_ref = ft.Ref[ft.TextField]()

    cards_name_row = ft.Container(
        content=ft.Row(
            controls=[
                ft.Container(
                    content=ft.Text(
                        value="Name:",
                        size=page.regular_settings["text_size"],
                        color=page.regular_settings["text_color_alt"]
                    ),
                    width=page.regular_settings["container_width"],
                ),
                ft.TextField(
                    label="Name",
                    hint_text="Type character's name",
                    ref=name_ref,
                )
            ],
        ),
    )

    cards_level_row = ft.Container(
        content=ft.Row(
            controls=[
                ft.Container(
                    content=ft.Text(
                        value="Level:",
                        size=page.regular_settings["text_size"],
                        color=page.regular_settings["text_color_alt"]
                    ),
                    width=page.regular_settings["container_width"],
                ),
                ft.TextField(
                    label="Level",
                    hint_text="Type character's level",
                    ref=level_ref,
                )
            ],
        ),
    )

    cards_class_row = ft.Container(
        content=ft.Row(
            controls=[
                ft.Container(
                    content=ft.Text(
                        value="Class:",
                        size=page.regular_settings["text_size"],
                        color=page.regular_settings["text_color_alt"]
                    ),
                    width=page.regular_settings["container_width"],
                ),
                ft.TextField(
                    label="Class",
                    hint_text="Type character's class",
                    ref=class_ref,
                )
            ],
        ),
    )

    cards_history_row = ft.Container(
        content=ft.Row(
            controls=[
                ft.Container(
                    content=ft.Text(
                        value="History:",
                        size=page.regular_settings["text_size"],
                        color=page.regular_settings["text_color_alt"]
                    ),
                    width=page.regular_settings["container_width"],
                ),
                ft.TextField(
                    label="History",
                    hint_text="Write character's story",
                    ref=history_ref,
                    multiline=True,
                    min_lines=10,
                    max_lines=10,
                    width=500
                )
            ],
        ),
    )

    avatar_name_ref = ft.Ref[ft.Text]()
    avatar_preview_ref = ft.Ref[ft.Image]()

    def on_avatar_selected(e: ft.FilePickerResultEvent):
        if not e.files:
            avatar_name_ref.current.value = "No file chosen"
            avatar_preview_ref.current.visible = False
            page.update()
            return

        f = e.files[0]
        avatar_name_ref.current.value = f.name

        if getattr(f, "path", None):
            avatar_preview_ref.current.src = f.path
            avatar_preview_ref.current.visible = True
            page.update()
            return

        # 2) Веб: пути нет — загружаем и показываем по URL
        page.upload_targets.clear()
        url = page.get_upload_url(f.name, expires=600)
        page.upload_targets[f.name] = url

        page.file_picker.upload([
            ft.FilePickerUploadFile(
                f.name,
                upload_url=url
            )
        ])

    def on_upload(e: ft.FilePickerUploadEvent):
        # когда загрузка завершилась, progress == 1
        if e.progress == 1:
            url = page.upload_targets.get(e.file_name)
            if url:
                avatar_preview_ref.current.src = url
                avatar_preview_ref.current.visible = True
                page.update()

    # подвязываем обработчики к единому file_picker
    page.file_picker.on_result = on_avatar_selected
    page.file_picker.on_upload = on_upload

    cards_image_row = ft.Row(
        controls=[
            ft.Container(
                ft.Text(
                    value="Avatar:",
                    size=page.regular_settings["text_size"],
                    color=page.regular_settings["text_color_alt"]
                ),
                width=page.regular_settings["container_width"],
            ),
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            text="Choose image...",
                            on_click=lambda _: page.file_picker.pick_files(
                                allow_multiple=False,
                                file_type=ft.FilePickerFileType.CUSTOM,
                                allowed_extensions=["png", "jpg", "jpeg", "gif", "webp"],
                            ),
                        ),
                        ft.Text(
                            value="No file chosen",
                            ref=avatar_name_ref
                        ),
                    ],
                ),
                expand=True,
            ),
        ]
    )

    avatar_preview = ft.Image(
        ref=avatar_preview_ref, visible=False,
        width=200, height=200, fit=ft.ImageFit.CONTAIN
    )

    card_controls = [
        cards_name_row,
        cards_level_row,
        cards_class_row,
        cards_image_row,
        avatar_preview,
        cards_history_row,
    ]

    page_card_settings = ft.Column(
        controls=card_controls,
        # alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    save_button = save_character(page, go_to_page, name_ref, level_ref, class_ref, avatar_name_ref, history_ref)

    page.header.content = make_header(page, header_text, go_back_button)
    page.page_content.content = page_card_settings
    page.footer.content = save_button

    page.update()
