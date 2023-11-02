import os
import arcade
from PIL import Image


class CustomSprite:
    """
    Clase para manejar sprites personalizados.
    """

    def __init__(self, path: str, columns: int, rows: int):
        """
        Inicializa un nuevo sprite personalizado.

        :param path: Ruta al archivo de imagen.
        :param columns: Número de columnas en la imagen.
        :param rows: Número de filas en la imagen.
        """
        # Abrir la imagen y obtener sus dimensiones
        self.__image = Image.open(path)
        self.__image_width, self.__image_height = self.__image.size

        # Inicializar variables
        self.__columns = columns
        self.__rows = rows
        self.__path = path
        self.__spritesize_x = self.__image_width // columns
        self.__spritesize_y = self.__image_height // rows
        self.__textures = []

        # Configurar las texturas
        self.__setup()

    def __setup(self):
        """
        Configura las texturas del sprite.
        """
        # Recorrer cada fila y columna para crear texturas
        for i in range(self.__rows):
            for j in range(self.__columns):
                texture = arcade.load_texture(
                    self.__path,
                    x=j * self.__spritesize_x,
                    y=i * self.__spritesize_y,
                    width=self.__spritesize_x,
                    height=self.__spritesize_y,
                )
                self.__textures.append(texture)

    @property
    def textures(self):
        """
        Devuelve las texturas del sprite.
        """
        return self.__textures


class CustomAnimation(arcade.AnimatedTimeBasedSprite):
    """
    Clase para manejar animaciones personalizadas.
    """

    def __init__(
        self, scale, custom_sprite: CustomSprite, frames: list, duration: int, loop=True
    ):
        """
        Inicializa una nueva animación personalizada.

        :param scale: Escala del sprite.
        :param custom_sprite: Objeto CustomSprite.
        :param frames: Lista de frames a usar.
        :param duration: Duración de cada frame.
        """
        self.__custom_sprite = custom_sprite
        super().__init__(
            scale=scale,
            image_width=custom_sprite._CustomSprite__image_width,
            image_height=custom_sprite._CustomSprite__image_height,
        )
        self.loop = loop
        self.__frames_ = frames
        self.__duration = duration

        # Configurar las texturas y frames de la animación
        self.__setup()

    def __setup(self):
        """
        Configura las texturas y frames de la animación.
        """
        textures = self.__custom_sprite.textures
        for i in range(len(textures)):
            if i not in self.__frames_:
                continue
            texture = textures[i]
            self.textures.append(texture)
            # Para que se quede congelado en el último frame si no es loop
            # se agrega un frame con duración 999999
            if not self.loop and i == len(textures) - 1:
                frame = arcade.AnimationKeyframe(0, 999999, texture)
            else:
                frame = arcade.AnimationKeyframe(0, self.__duration, texture)
            self.frames.append(frame)

    @property
    def position(self):
        """
        Devuelve la posición del sprite.
        """
        return self.center_x, self.center_y

    @position.setter
    def position(self, value):
        """
        Establece la posición del sprite.

        :param value: Tupla (x, y) con las nuevas coordenadas.
        """
        self.center_x, self.center_y = value

    def set_position(self, x, y):
        self.center_x = x
        self.center_y = y

    def update_position(self, delta_x, delta_y):
        """
        Actualiza la posición del sprite según los deltas dados.

        :param delta_x: Cambio en la coordenada x.
        :param delta_y: Cambio en la coordenada y.
        """
        self.center_x += delta_x
        self.center_y += delta_y

        # Condiciones de borde para que el sprite aparezca al otro lado de la pantalla
        if self.center_x > 824:
            self.center_x = -24
        if self.center_x < -24:
            self.center_x = 823

        if self.center_y > 624:
            self.center_y = -24
        if self.center_y < -24:
            self.center_y = 623
