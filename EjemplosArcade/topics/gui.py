import arcade
import arcade.gui
import webbrowser

PLACE_HOLDER = "Tu nombre..."
LOREM = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent ipsum eros, pretium quis nisi ut, suscipit elementum dolor. Mauris sed nulla iaculis, condimentum sapien ut, venenatis elit. Vivamus nisi enim, convallis eget lobortis eu, sagittis eu enim. Donec laoreet nunc neque, sed malesuada sem rhoncus sit amet. Curabitur ornare a dolor vitae commodo. Sed volutpat odio sed orci egestas tristique. Sed ac lobortis odio. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Praesent aliquam tempor tellus, non aliquet nibh faucibus at. Nullam nec placerat turpis. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Ut at posuere risus. Vivamus eget lacus sed libero convallis viverra quis et turpis. Pellentesque ac purus nec tortor convallis faucibus. In eget magna cursus, aliquet sapien eget, congue ex. Nulla et ante semper, eleifend lectus ac, suscipit mauris. Vivamus purus sem, sodales eget elit ac, dignissim luctus enim. Praesent pretium justo urna, in elementum ligula lobortis vel. Donec egestas purus bibendum nibh cursus, in ultricies sem lobortis. Proin fringilla vitae elit eget posuere."

class ExampleGui:
    def __init__(self):
        self.custom_manager = arcade.gui.UIManager()
        self.scroll_manager = arcade.gui.UIManager()

        self.v_box = arcade.gui.UIBoxLayout()
        self.scroll_open = False

        # Creación de label text con fuente
        ui_text_label = arcade.gui.UITextArea(
            text=" REGISTRO DE JUGADOR",
            width=500,
            height=40,
            font_size=24,
            font_name="Kenney Future",
        )

        # Creación de label text
        self.v_box.add(ui_text_label.with_space_around(bottom=20))
        text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
        self.ui_text_label = arcade.gui.UITextArea(
            text=text, width=450, height=60, font_size=12, font_name="Arial"
        )
        self.v_box.add(self.ui_text_label.with_space_around(bottom=20))

        # Creación de un input text
        input_field = arcade.gui.UIInputText(
            text_color=arcade.color.BLACK, font_size=16, width=300, height=30, text=" ", multiline=True
        )

        self.v_box.add(input_field.with_border())

        # Creación de UIFlatButton
        ui_flatbutton = arcade.gui.UIFlatButton(text="Enviar", width=200)
        self.v_box.add(ui_flatbutton.with_space_around(bottom=20, top=20))

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
                message_text=("Esta es una alerta"),
                buttons=["Ok", "Cancel"],
            )
            self.custom_manager.add(message_box)

        self.v_box.add(ui_texture_button.with_space_around(bottom=30))


        # Creación de UITextureButton
        ui_texture_button_2 = arcade.gui.UITextureButton(texture=texture)

        bg_tex = arcade.load_texture(":resources:gui_basic_assets/window/grey_panel.png")
        text_area = arcade.gui.UITextArea(
                            width=400,
                            height=300,
                            text=LOREM,
                            text_color=(0, 0, 0, 255))
        
        self.scroll_manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x", 
                anchor_y="center_y", 
                child=arcade.gui.UITexturePane(
                    text_area.with_space_around(right=20),
                    tex=bg_tex,
                    padding=(30, 30, 30, 30)
                )
            )
        )
        texture_2 = arcade.load_texture(":resources:onscreen_controls/flat_dark/close.png")
        close_scroll_btn = arcade.gui.UITextureButton(texture=texture_2)

        # Click handler
        @close_scroll_btn.event("on_click")
        def on_click_close_scroll_btn(event):
            self.scroll_manager.disable()
            self.scroll_open = False
        
        self.scroll_manager.add(close_scroll_btn)

        # Click handler
        @ui_texture_button_2.event("on_click")
        def on_click_texture_button_2(event):
            self.scroll_manager.enable()
            self.scroll_open = True

        self.v_box.add(ui_texture_button_2.with_space_around(bottom=20))


        # Creación de un input text
        multi_input_field = arcade.gui.UIInputText(
            text_color=arcade.color.BLACK, font_size=16, width=300, height=90, text=" ", multiline=True
        )

        self.v_box.add(multi_input_field.with_border().with_space_around(bottom=20))


        #Link a recursos
        ui_resources = arcade.gui.UILabel(
            text="https://api.arcade.academy/en/latest/resources.html?highlight=onscreen_controls#id24",
            width=450,
            height=60,
            font_size=12,
            text_color=arcade.color.BLUE,
            font_name="Arial",
        )

        #Ya que label no es clickable se incluye dentro de un elemento interactive para poder detectar el click
        ui_resources_clickable = arcade.gui.UIInteractiveWidget(
            width=450,
            height=60,
        )
        ui_resources_clickable.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x", anchor_y="center_y", child=ui_resources
            )
        )

        @ui_resources_clickable.event("on_click")
        def on_ui_resources_click(event):
            webbrowser.open(ui_resources.text)

        self.v_box.add(ui_resources_clickable)

        # Creación de widget para contener el v_box widget, permite centrado de objetos
        self.custom_manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x", anchor_y="center_y", child=self.v_box
            )
        )

    def draw(self):
        if not self.scroll_open:
            self.custom_manager.draw()
        else:
            self.scroll_manager.draw()
