import reflex as rx
import datetime

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="favicon.ico"
        ),
        rx.link(
            f"© 2024-{datetime.date.today().year} Vshop BY VIEPAIX V1.",
            href="https://viepaix.dev"
            ),
        rx.text(
            " Hacker and Programmer"
        )
    )