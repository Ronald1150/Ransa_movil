import reflex as rx

def aboutUser2Screen()-> rx.Component:
    return rx.mobile_and_tablet(
        rx.container(
            rx.color_mode.button(position="top-right"),
            rx.vstack(
                rx.image(src="https://i.pinimg.com/736x/f0/b8/b7/f0b8b749a5b89644f5ef6f1609f354cf.jpg", padding="25px", width="250px", margin_top="90px", margin_left="65px"),
                rx.text("Cuando quieres que te recuerde?", margin_bottom="50px"),
                rx.hstack(
                    rx.button("HORA:", background_color="transparent", margin_left="20px", color="purple"),
                    rx.spacer(),
                    rx.button("8:00 am", background_color="gray", margin_left="150px"),
                    margin_bottom="50px"),
                rx.hstack(
                    rx.button("estilos:", background_color="transparent", margin_left="20px", color="purple"),
                    rx.spacer(),
                    rx.button("1 diseño", background_color="gray", margin_left="154px",margin_bottom="90px")),
                rx.button("GUARDAR", margin_left="137px", background_color="green")
                )))