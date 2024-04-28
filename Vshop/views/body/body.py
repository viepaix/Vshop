import reflex as rx

def body() -> rx.Component:
    return rx.box(
        rx.section(
            rx.heading("TITLE"),
            rx.text("This is the first content section"),
            padding_left="12px",
            padding_right="12px",
            background_color="var(--gray-2)",
        ),
    )