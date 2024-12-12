import reflex as rx

def aboutUserScreen() -> rx.Component:  # Cambié 'aboutUser Screen' a 'aboutUserScreen'
    return rx.mobile_and_tablet(
        rx.container(
            rx.color_mode.button(position="top-right"),
            rx.vstack(
                rx.image(src="C:\Users\rq622\Documents\Proyecto_Ronald\aplicasion_movil\Ransa_apliacasion\assets\mercado.jpeg", padding="25px", width="250px", margin_top="90px", margin_left="25px"),
                rx.text("¿Qué productos desea?", margin_bottom="50px"),
                rx.button("Abarrotes", margin_bottom="40px", margin_left="50px", width="200px", color="blue", background="transparent",
                          _hover={"background_color": "rgba(197, 109, 252, 1)"},
                          style={"border_left": "2px solid #c56dfc", "border_right": "2px solid #c56dfc"}
                          ),
                rx.button("Cereales", margin_bottom="40px", margin_left="50px", width="200px", color="blue", background="transparent",
                          _hover={"background_color": "rgba(197, 109, 252, 1)"},
                          style={"border_left": "2px solid #c56dfc", "border_right": "2px solid #c56dfc"}
                          ),
                rx.button("Menestra", margin_bottom="45px", margin_left="50px", width="200px", color="blue", background="transparent",
                          _hover={"background_color": "rgba(197, 109, 252, 1)"},
                          style={"border_left": "2px solid #c56dfc", "border_right": "2px solid #c56dfc"}
                          ),
                rx.button("Licores", margin_bottom="40px", margin_left="50px", width="200px", color="blue", background="transparent",
                          _hover={"background_color": "rgba(197, 109, 252, 1)"},
                          style={"border_left": "2px solid #c56dfc", "border_right": "2px solid #c56dfc"}
                          ),
                rx.button("SIGUIENTE", width="150px", margin_left="80px", background_color="green"),
                justify_items="center",
                padding="30px"
            )
        )
    )