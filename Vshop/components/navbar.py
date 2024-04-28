import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.hstack(
        rx.text(
            "Vshop",
            height="40px"
        )
    ),
    rx.spacer(),
    rx.menu.root(
        rx.menu.trigger(
            rx.button("Options")
        ),
        rx.menu.content(
            rx.menu.item("Prueba1"),
            rx.menu.separator(),
            rx.menu.item("Prueba1"),
            rx.menu.item("Prueba1"),
            rx.menu.item("Prueba1")
        )
    ),
        position="sticky",
        bg="rgb(98,98,98)",
        padding_y="5px",
        padding_x="12px",
        z_index="999"
    )