import os
import arcade
from PIL import Image

import sys
sys.path.append("..")
from helpers import CustomSprite

class ExampleSprite():
    def __init__(self):
        # Atributos privados para el jugador y animaciones
        self.__player = None
        self.__player_idle = None
        self.__player_roll = None
        self.__speed = 300

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
        ball_path = os.path.join(current_directory, '../assets/ball.png')

        # Crear sprites y animaciones para el jugador
        self.__player = CustomSprite(ball_path, 3, 5)

    def draw(self):
        print("Test")