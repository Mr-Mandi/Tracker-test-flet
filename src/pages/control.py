import flet as ft
from model.cron import Chronometer
from time import sleep


def timer_view(page: ft.Page, function, word):
    chronometer = Chronometer()

    def go_back_to_initial_view(e):
        page.clean()
        function(page)

    back_button = ft.IconButton(
        icon=ft.icons.ARROW_BACK,
        on_click=go_back_to_initial_view,
        icon_color=ft.colors.BLUE,
    )

    image = ft.Image(
        src="https://picsum.photos/200/200",
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN,
        border_radius=ft.border_radius.all(100),
    )

    title_page = ft.Text(
        word,
        size=40,
        color=ft.colors.BLACK,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )

    time_text = ft.Text(
        "00:00:00",
        size=40,
        color=ft.colors.BLACK,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )

    def initial_timer():
        while chronometer.paused_time is False:
            sleep(1)
            chronometer.start(page, time_text)

    container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    [back_button],
                    alignment=ft.MainAxisAlignment.START
                ),
                image,
                title_page,
                time_text,
                ft.Row(
                    [
                        ft.ElevatedButton(
                            text="Start",
                            on_click=lambda e: initial_timer()
                        ),
                        ft.ElevatedButton(
                            text="Pause",
                            on_click=lambda e: chronometer.pause(page=page)
                        ),
                        ft.ElevatedButton(
                            text="Stop",
                            on_click=lambda e: chronometer.stop(page=page)
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        ),
        padding=40,
        border_radius=10,
        bgcolor=ft.colors.WHITE,
    )

    page.add(container)
