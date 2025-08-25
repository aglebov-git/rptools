import json
from pathlib import Path
import flet as ft
from flet_interface.utils.on_hover import on_button_hover

CHAR_FILE = Path("characters.json")

def _read_db():
    if CHAR_FILE.exists():
        try:
            return json.loads(CHAR_FILE.read_text(encoding="utf-8"))
        except Exception:
            return []
    return []

def _write_db(data):
    CHAR_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

def save_character(
    page: ft.Page,
    go_to_page,
    name_ref: ft.Ref[ft.TextField],
    level_ref: ft.Ref[ft.TextField],
    class_ref: ft.Ref[ft.TextField],
    avatar_name_ref: ft.Ref[ft.Text],
    history_ref: ft.Ref[ft.TextField],
):
    def on_click(e):
        # Collect data.
        name = name_ref.current.value.strip()
        level = level_ref.current.value.strip()
        clazz = class_ref.current.value.strip()
        avatar = avatar_name_ref.current.value.strip()
        history = history_ref.current.value.strip()

        # Validation.
        if not name:
            dlg = ft.AlertDialog(
                title=ft.Text("ERROR"),
                content=ft.Text("There is no name!"),
                alignment=ft.alignment.center,
                title_padding=ft.padding.all(25),
            )
            page.open(dlg)
            return

        record = {
            "name": name,
            "level": level,
            "class": clazz,
            "avatar": avatar,
            "history": history,
        }

        # Read and append new character.
        db = _read_db()

        # Check if character already exists.
        if record in db:
            dlg = ft.AlertDialog(
                title=ft.Text("ERROR"),
                content=ft.Text("This character already exists!"),
                alignment=ft.alignment.center,
                title_padding=ft.padding.all(25),
            )
            page.open(dlg)
            return

        db.append(record)
        _write_db(db)

        # Notification.
        dlg = ft.AlertDialog(
            title=ft.Text("SUCCESS!"),
            content=ft.Text("Your character has been created!"),
            alignment=ft.alignment.center,
            title_padding=ft.padding.all(25),
        )
        page.open(dlg)
        go_to_page(page, go_to_page, 1)

    save_button = ft.Container(
        content=ft.Text(
            value="Save",
            size=page.button_settings["text_size"],
            color=page.button_settings["text_color"],
        ),
        height=page.button_settings["height_back_button"],
        width=page.button_settings["width_back_button"],

        border_radius=16,
        bgcolor=page.button_settings["bg_color"],
        alignment=ft.alignment.center,

        on_hover=lambda e: on_button_hover(e, page),
        on_click=on_click,
    )
    return save_button
