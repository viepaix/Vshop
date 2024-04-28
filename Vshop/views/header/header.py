import reflex as rx

def header() -> rx.Component:
    return rx.hstack(
        rx.avatar(name="Viepaix Shop",
                        fallback="VS" ,
                        size="8" ,
                        variant="solid",
                        color_scheme="purple",
                        radius="full"
                  ),
        rx.text("Programming shop",
                weight="bold",
                size="3",
                color_scheme="gray"),
        spacing="1"
    )