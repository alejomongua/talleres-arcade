import os
import arcade

import sys

sys.path.append("..")
from helpers import CustomSprite, CustomAnimation


class ExampleAnimation:
    def __init__(self, anim_path: str):
        # Atributos privados para el jugador y animaciones
        self.__anim_path = anim_path
        self.__player = None
        self.__player_idle = None
        self.__player_talk = None

        # Atributos privados para el movimiento
        self.__move_right = False
        self.__move_left = False

        # Inicializar el juego
        self.setup()

    def setup(self):
        self.__player_list = arcade.SpriteList()

        # Obtener la ruta del directorio donde se encuentra el archivo de Python actual
        current_directory = os.path.dirname(os.path.abspath(__file__))

        # Construir la ruta completa al archivo 'ball.png'
        anim_path = os.path.join(current_directory, "../assets/frog.png")

        # Crear sprites y animaciones para el jugador
        self.__player = CustomSprite(anim_path, 5, 3)
        self.__player_idle = CustomAnimation(1, self.__player, [0, 1], 120)
        self.__player_idle.position = (300, 600 // 2)
        self.__player_idle.enabled = True
        self.__player_talk = CustomAnimation(1, self.__player, [5, 6, 7, 8, 9], 100)
        self.__player_talk.position = (500, 600 // 2)
        self.__player_talk.enabled = True

        # Añadir animaciones a la lista de sprites
        self.__player_list.append(self.__player_idle)
        self.__player_list.append(self.__player_talk)

    def key_press(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT:
            self.__move_right = True
        if symbol == arcade.key.LEFT:
            self.__move_left = True

        # Activar animación de rodar y desactivar animación de estar quieto
        if self.__move_right or self.__move_left:
            self.__player_idle.enabled = False
            self.__player_talk.enabled = True

    def key_release(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT:
            self.__move_right = False

        if symbol == arcade.key.LEFT:
            self.__move_left = False

        # Activar animación de estar quieto y desactivar animación de rodar
        if self.__move_right == False and self.__move_left == False:
            self.__player_idle.enabled = True
            self.__player_talk.enabled = False

    def draw(self):
        for anim in self.__player_list:
            if anim.enabled:
                anim.draw()

    def update(self, delta_time):
        for anim in self.__player_list:
            if anim.enabled:
                anim.update_animation()


class ExampleInputsAnim:
    def __init__(self, anim_path: str):
        # Atributos privados para el jugador y animaciones
        self.__anim_path = anim_path
        self.__player = None
        self.__player_idle = None
        self.__player_roll = None
        self.__speed = 300

        # Atributos privados para el movimiento
        self.__move_right = False
        self.__move_left = False
        self.time_left = 5
        self.dead = False

        # Inicializar el juego
        self.setup()

    def setup(self):
        self.__player_list = arcade.SpriteList()

        # Obtener la ruta del directorio donde se encuentra el archivo de Python actual
        current_directory = os.path.dirname(os.path.abspath(__file__))

        # Construir la ruta completa al archivo 'ball.png'
        anim_path = os.path.join(current_directory, "../assets/ball.png")

        # Crear sprites y animaciones para el jugador
        self.__player = CustomSprite(anim_path, 3, 5)
        self.__player_idle = CustomAnimation(3, self.__player, [0, 1, 2], 100)
        self.__player_idle.position = (800 // 2, 600 // 2)
        self.__player_idle.enabled = True
        self.__player_roll = CustomAnimation(
            3, self.__player, [7, 8, 9, 10, 11, 12], 60
        )
        self.__player_roll.position = (800 // 2, 600 // 2)
        self.__player_roll.enabled = False

        self.__player_die = CustomAnimation(
            3, self.__player, [2, 13, 14], 100, loop=False
        )
        self.__player_die.position = (800 // 2, 600 // 2)
        self.__player_die.enabled = False

        # Añadir animaciones a la lista de sprites
        self.__player_list.append(self.__player_idle)
        self.__player_list.append(self.__player_roll)
        self.__player_list.append(self.__player_die)

    def key_press(self, symbol, modifiers):
        if self.dead:
            return

        if symbol == arcade.key.RIGHT:
            self.__move_right = True
        if symbol == arcade.key.LEFT:
            self.__move_left = True

        # Activar animación de rodar y desactivar animación de estar quieto
        if self.__move_right or self.__move_left:
            self.__player_idle.enabled = False
            self.__player_roll.enabled = True

    def key_release(self, symbol, modifiers):
        if self.dead:
            if symbol == arcade.key.SPACE:
                self.dead = False
                self.__player_idle.enabled = True
                self.__player_roll.enabled = False
                self.__player_die.enabled = False
                self.time_left = 5
            return

        if symbol == arcade.key.RIGHT:
            self.__move_right = False

        if symbol == arcade.key.LEFT:
            self.__move_left = False

        # Activar animación de estar quieto y desactivar animación de rodar
        if self.__move_right == False and self.__move_left == False:
            self.__player_idle.enabled = True
            self.__player_roll.enabled = False

    def draw(self):
        if self.dead:
            time_text = "Has muerto, presiona espacio para reiniciar"
        else:
            time_text = f"Tiempo restante: {int(round(self.time_left))}"
        arcade.draw_text(
            time_text,
            320,
            200,
            arcade.color.BLACK,
            24,
            anchor_x="center",
            anchor_y="center",
        )

        for anim in self.__player_list:
            if anim.enabled:
                anim.draw()

    def update(self, delta_time):
        # Disminuir el temporizador
        self.time_left -= delta_time

        if self.time_left <= 0:
            self.time_left = 0
            self.on_timer_finish()

        for anim in self.__player_list:
            if anim.enabled:
                anim.update_animation()

        # Actualizar posición del jugador según las teclas presionadas
        if self.__move_right:
            self.__player_idle.update_position(self.__speed * delta_time, 0)
            self.__player_roll.update_position(self.__speed * delta_time, 0)
            self.__player_die.update_position(self.__speed * delta_time, 0)
        if self.__move_left:
            self.__player_idle.update_position(-self.__speed * delta_time, 0)
            self.__player_roll.update_position(-self.__speed * delta_time, 0)
            self.__player_die.update_position(-self.__speed * delta_time, 0)

    def set_position(self, x, y):
        self.__player_idle.set_position(x, y)
        self.__player_roll.set_position(x, y)

    def on_timer_finish(self):
        if self.dead:
            return

        self.dead = True
        self.__move_left = False
        self.__move_right = False
        self.__player_die.reset_animation()
        self.__player_idle.enabled = False
        self.__player_roll.enabled = False
        self.__player_die.enabled = True
