import reflex as rx

from Vshop.components.navbar import navbar
from Vshop.views.header.header import header
from Vshop.views.body.body import body
from Vshop.components.footer import footer

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                body(),
                margin_y="20px"
            ), 
            align_items="center"
        ),
        footer(),
    )


app = rx.App()
app.add_page(index)