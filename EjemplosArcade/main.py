import arcade
import arcade.gui
from topics.sprite import ExampleSprite

class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()

class MyWindow(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Ejemplos Arcade", resizable=True)

        #Variables de control
        self.level = 0

        # UIManager para realizar gestión de UI (User Interface).
        self.main_manager = arcade.gui.UIManager()
        self.main_manager.enable()

        self.level_manager = arcade.gui.UIManager()
        self.level_manager.enable()

        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)
        
        # BoxGroup permite alinear elementos de UI de manera organizada
        self.v_box = arcade.gui.UIBoxLayout()
        self.return_box = arcade.gui.UIBoxLayout(0,0)

        #Sprite button
        sprite_button = arcade.gui.UIFlatButton(text="Sprite", width=200)
        self.v_box.add(sprite_button.with_space_around(bottom=20))
        
        #Anim button
        anim_button = arcade.gui.UIFlatButton(text="Animation", width=200)
        self.v_box.add(anim_button.with_space_around(bottom=20))

        #Return button
        return_button = arcade.gui.UIFlatButton(text="Volver", width=200)
        self.return_box.add(return_button.with_space_around(bottom=20))
        
        #Opcion 1: Generar instancia de elemento 'Button' a partir de clase
        quit_button = QuitButton(text="Salir", width=200)
        self.v_box.add(quit_button)

        #Opción 2 Por medio de decoradoradores @sprite_button es posible realizar la gestión de eventos y propiedades
        @sprite_button.event("on_click")
        def on_click_sprite(event):
            self.level = 1

        #Opción 3: Consumir funciones definidas dentro del contexto de la clase
        anim_button.on_click = self.on_click_anim
        return_button.on_click = self.on_click_return

        # Create a widget to hold the v_box widget, that will center the buttons
        self.main_manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

        self.level_manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="left",
                anchor_y="top",
                child=self.return_box)
        )

        #Consumo elementos niveles
        self.example_sprite = ExampleSprite()

    #def setup(self):


    def on_click_anim(self, event):
        print("Anim:")

    def on_click_return(self, event):
        self.level = 0

    def on_draw(self):
        arcade.start_render()
        self.clear()
        if(self.level == 0):
            self.main_manager.draw()#Permite dibujar el objeto 'manager' que contiene los elementos de UI
        else:
            self.level_manager.draw()
        
        
        if(self.level == 1):
            self.level_manager.draw()
            self.example_sprite.draw()#Permite dibujar el objeto 'manager' que contiene los elementos de UI


    def on_update(self, delta_time):
        if(self.level == 1):
            self.example_sprite.update(delta_time)#Permite dibujar el objeto 'manager' que contiene los elementos de UI


    def on_key_press(self, symbol, modifiers):
        if(self.level == 1):
            self.example_sprite.key_press(symbol, modifiers)#Permite dibujar el objeto 'manager' que contiene los elementos de UI
    

    def on_key_release(self, symbol, modifiers):
        if(self.level == 1):
            self.example_sprite.key_release(symbol, modifiers)#Permite dibujar el objeto 'manager' que contiene los elementos de UI

window = MyWindow()
arcade.run()