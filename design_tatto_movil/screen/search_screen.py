import reflex as rx

def searchScreen() -> rx.Component:
    return rx.mobile_and_tablet(
        rx.container(
            rx.color_mode.button(position="top-right"),
            rx.vstack(
                rx.input(placeholder="busca diseño o estilo  de tatuaje...", width="70%", border_width="2px"),
                rx.text("encontrararas los estilo de tatuaje que buscas ", text_align="center", color="gray", margin_top="300px", margin_left="-50px", size="4"),
                margin_top="15px",
                margin_left="50px"
            ),
            )
        )