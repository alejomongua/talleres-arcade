import math

import arcade
import arcade.gui
from topics.sprite import ExampleSprite
from topics.animation_inputs import ExampleAnimation, ExampleInputsAnim

# Definición de constantes
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

OPCION_HOME = 0
OPCION_SPRITE = 1
OPCION_ANIM = 2
OPCION_INPUT = 3
OPCION_DRAG_N_DROP = 4

def get_distance_between_points(x1, y1, x2, y2):
    """ Calculate the distance between two points """
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()

class MyWindow(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, "Ejemplos Arcade", resizable=True)

        #Variables de control
        self.level = OPCION_HOME

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

        #Input button
        input_button = arcade.gui.UIFlatButton(text="Input", width=200)
        self.v_box.add(input_button.with_space_around(bottom=20))

        #Drag and drop button
        drag_and_drop_button = arcade.gui.UIFlatButton(text="Drag and drop", width=200)
        self.v_box.add(drag_and_drop_button.with_space_around(bottom=20))

        #Return button
        return_button = arcade.gui.UIFlatButton(text="Volver", width=200)
        self.return_box.add(return_button.with_space_around(bottom=20))
        
        #Opcion 1: Generar instancia de elemento 'Button' a partir de clase
        quit_button = QuitButton(text="Salir", width=200)
        self.v_box.add(quit_button)

        #Opción 2 Por medio de decoradoradores @sprite_button es posible realizar la gestión de eventos y propiedades
        @sprite_button.event("on_click")
        def on_click_sprite(event):
            self.level = OPCION_SPRITE

        #Opción 3: Consumir funciones definidas dentro del contexto de la clase
        anim_button.on_click = self.on_click_anim
        return_button.on_click = self.on_click_return
        input_button.on_click = self.on_click_input
        drag_and_drop_button.on_click = self.on_click_drag_n_drop

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
        self.example_sprite = ExampleSprite(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        self.example_animation = ExampleAnimation('../assets/ball.png')
        self.example_input = ExampleInputsAnim('../assets/frog.png')

        # Atributos para el objeto "drag and drop"
        self.circle_x = WINDOW_WIDTH // 2
        self.circle_y = WINDOW_HEIGHT // 2
        self.circle_radius = 50
        self.is_circle_being_dragged = False

    def on_click_anim(self, event):
        self.level = OPCION_ANIM

    def on_click_input(self, event):
        self.level = OPCION_INPUT

    def on_click_drag_n_drop(self, event):
        self.level = OPCION_DRAG_N_DROP
        self.main_manager.disable()

    def on_click_return(self, event):
        self.level = OPCION_HOME
        self.main_manager.enable()

    def on_draw(self):
        arcade.start_render()
        self.clear()
        if self.level == OPCION_HOME:
            self.main_manager.draw()#Permite dibujar el objeto 'manager' que contiene los elementos de UI
        else:
            self.level_manager.draw()
        

        if self.level == OPCION_SPRITE:
            self.example_sprite.draw()
        
        if self.level == OPCION_ANIM:
            self.example_animation.draw()#Permite dibujar el objeto 'manager' que contiene los elementos de UI

        if self.level == OPCION_DRAG_N_DROP:
            arcade.draw_circle_filled(self.circle_x, self.circle_y, self.circle_radius, arcade.color.BLUE)

        if self.level == OPCION_INPUT:
            self.example_input.draw()#Permite dibujar el objeto 'manager' que contiene los elementos de UI


    def on_update(self, delta_time):
        if self.level == OPCION_ANIM:
            self.example_animation.update(delta_time)#Permite dibujar el objeto 'manager' que contiene los elementos de UI

        if self.level == OPCION_INPUT:
            self.example_input.update(delta_time)#Permite dibujar el objeto 'manager' que contiene los elementos de UI


    def on_key_press(self, symbol, modifiers):
        if self.level == OPCION_INPUT:
            self.example_input.key_press(symbol, modifiers)#Permite dibujar el objeto 'manager' que contiene los elementos de UI
    

    def on_key_release(self, symbol, modifiers):
        if self.level == OPCION_INPUT:
            self.example_input.key_release(symbol, modifiers)#Permite dibujar el objeto 'manager' que contiene los elementos de UI


    def on_mouse_press(self, x, y, button, key_modifiers):
        """ Called when the user presses a mouse button. """
        if not self.level == OPCION_DRAG_N_DROP:
            return
        # Verifica si el círculo fue presionado
        if get_distance_between_points(x, y, self.circle_x, self.circle_y) < self.circle_radius:
            self.is_circle_being_dragged = True

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        if not self.level == OPCION_DRAG_N_DROP:
            return
        """ Called when the user releases a mouse button. """
        self.is_circle_being_dragged = False

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        """ User moves mouse """
        if not self.level == OPCION_DRAG_N_DROP:
            return
        if self.is_circle_being_dragged:
            self.circle_x += dx
            self.circle_y += dy



window = MyWindow()
arcade.run()