import os
import arcade

class ExampleSprite():
    """Ejemplo de sprite sin animación"""
    def __init__(self, pos_x, pos_y):
        # Atributos privados para el jugador y animaciones
        self.__x = pos_x
        self.__y = pos_y
        self.__sprite = None

        # Inicializar el sprite
        self.setup()

    def setup(self):
        # Obtener la ruta del directorio donde se encuentra el archivo de Python actual
        current_directory = os.path.dirname(os.path.abspath(__file__))

        # Construir la ruta completa al archivo 'ball.png'
        sprite_path = os.path.join(current_directory, '../assets/robot1.png')

        self.__sprite = arcade.Sprite(sprite_path, 0.5)
        self.__sprite.center_x = self.__x
        self.__sprite.center_y = self.__y

    def draw(self):
        self.__sprite.draw()