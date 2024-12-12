import reflex as rx

def notifyScreen() -> rx.Component:
    return rx.mobile_and_tablet(
        rx.container(
            rx.hstack(
            rx.color_mode.button(position="top-right"),
            rx.text("notificaciones", margin_top="15px", margin_bottom="10px"),
            style={
                "border_bottom":"2px solid #c56dfc"},
            margin_bottom="100px"),
            rx.vstack(
                rx.button("ya tienes los procductos", height="50px", background_color="pink"),
                rx.button("se añadio los productos", height="50px", background_color="pink"),
                rx.button("tienes un prodicto pendiente", height="50px", background_color="pink"),
                rx.button("ya puedes recoger tu producto", height="50px", background_color="pink")
            )))