import flet as ft
import random

from pages.control import timer_view
from utils.script import get_random_text_options


def initial_view(page: ft.Page):
    actually_word = 'x'

    def get_random_text(e):
        nonlocal actually_word
        options = get_random_text_options()
        random_text.value = options
        actually_word = options
        page.update()

    def textbox_changed(e):
        nonlocal actually_word
        random_text.value = e.control.value
        actually_word = random_text.value
        page.update()

    def navigate_to_timer(e):
        page.clean()
        timer_view(page=page, function=initial_view, word=actually_word)

    image = ft.Image(
        src="https://picsum.photos/200/200",
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN,
        border_radius=ft.border_radius.all(100),
    )

    random_text = ft.Text(
        value="",
        size=16,
        color=ft.Colors.BLACK,
        text_align=ft.TextAlign.CENTER,
    )

    tb1 = ft.TextField(label="texto", width=300, on_change=textbox_changed,)

    random_button = ft.ElevatedButton(
        text="Random Select",
        on_click=get_random_text,
        width=300,
    )

    start_button = ft.ElevatedButton(
        text="Start",
        on_click=navigate_to_timer,
        width=300,
        color=ft.Colors.WHITE,
        bgcolor=ft.Colors.BLUE,
    )

    container = ft.Container(
        content=ft.Column(
            controls=[
                image,
                tb1,
                random_button,
                random_text,
                start_button,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        ),
        padding=40,
        border_radius=10,
        bgcolor=ft.Colors.WHITE,
    )

    page.add(container)
