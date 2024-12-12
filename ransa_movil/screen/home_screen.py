import reflex as rx

def homeScreen() -> rx.Component:
    return rx.mobile_and_tablet(
        rx.container(
            rx.color_mode.button(position="top-right"),
            rx.text("notificaciones", margin_top="15px"),
            rx.vstack(
                rx.text("VIENVENIDO ", size="6", font_size="poppins"),
                rx.text("Buscaste tu producto", size="4", text_align="center"),
                rx.button("Buscar producto ", font_size="poppins", background_color="gray", margin_top="15px",
                          _hover={"background_color": "lightgreen"}),
                display="flex",
                align_items="center",
                margin_top="32vh",
                height="100vh"
            ),
        ),
    )