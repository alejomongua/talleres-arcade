
import arcade
import arcade.gui


PLACE_HOLDER = 'Tu nombre...'

class ExampleGui():
    def __init__(self):
        self.custom_manager = arcade.gui.UIManager()
        self.custom_manager.enable()

        self.v_box = arcade.gui.UIBoxLayout()

        # Creación de label text con fuente
        ui_text_label = arcade.gui.UITextArea(text=" REGISTRO DE JUGADOR",
                                              width=500,
                                              height=40,
                                              font_size=24,
                                              font_name="Kenney Future")
        
        # Creación de label text
        self.v_box.add(ui_text_label.with_space_around(bottom=20))
        text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
        self.ui_text_label = arcade.gui.UITextArea(text=text,
                                              width=450,
                                              height=60,
                                              font_size=12,
                                              font_name="Arial")
        self.v_box.add(self.ui_text_label.with_space_around(bottom=20))

        # Creación de un input text
        input_field = arcade.gui.UIInputText(
          text_color=arcade.color.BLACK,
          font_size=16,
          width=300,
          height=60,
          text=PLACE_HOLDER)
        
        self.v_box.add(input_field.with_space_around(bottom=20))  
        
        # Creación de UIFlatButton
        ui_flatbutton = arcade.gui.UIFlatButton(text="Enviar", width=200)
        self.v_box.add(ui_flatbutton.with_space_around(bottom=20))

        # Click handler
        @ui_flatbutton.event("on_click")
        def on_click_flatbutton(event):
            self.ui_text_label.text = "Hola " + input_field.text

        # Creación de UITextureButton
        texture = arcade.load_texture(":resources:onscreen_controls/flat_dark/play.png")
        ui_texture_button = arcade.gui.UITextureButton(texture=texture)

        # Click handler
        @ui_texture_button.event("on_click")
        def on_click_texture_button(event):
            message_box = arcade.gui.UIMessageBox(
                width=450,
                height=300,
                message_text=(
                    "Esta es una alerta"
                ),
                buttons=["Ok", "Cancel"]
            )
            self.custom_manager.add(message_box)

        self.v_box.add(ui_texture_button.with_space_around(bottom=20))


        ui_resources = arcade.gui.UITextArea(text="https://api.arcade.academy/en/latest/resources.html?highlight=onscreen_controls",
                                              width=450,
                                              height=60,
                                              font_size=12,
                                              font_name="Arial")
        self.v_box.add(ui_resources.with_space_around(bottom=20))

        # Creación de widget para contener el v_box widget, permite centrado de objetos
        self.custom_manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def on_click_start(self, event):
        print("Start:", event)

    def draw(self):
        self.custom_manager.draw()