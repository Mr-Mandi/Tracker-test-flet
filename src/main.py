import flet as ft
from pages.home import initial_view


def main(page: ft.Page):
    page.title = "Control App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Start App
    initial_view(page)


ft.app(target=main)
