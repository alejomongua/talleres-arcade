import os
import arcade
from PIL import Image

class CustomSprite():
    """
    Clase para manejar sprites personalizados.
    """
    def __init__(self, path:str, columns:int, rows:int):
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
                texture = arcade.load_texture(self.__path, 
                                              x=j*self.__spritesize_x,
                                              y=i*self.__spritesize_y,
                                              width=self.__spritesize_x,
                                              height=self.__spritesize_y)
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
    def __init__(self, scale:int, custom_sprite:CustomSprite, frames:list, duration:int):
        """
        Inicializa una nueva animación personalizada.
        
        :param scale: Escala del sprite.
        :param custom_sprite: Objeto CustomSprite.
        :param frames: Lista de frames a usar.
        :param duration: Duración de cada frame.
        """
        self.__custom_sprite = custom_sprite
        super().__init__(scale=scale, 
                         image_width=custom_sprite._CustomSprite__image_width, 
                         image_height=custom_sprite._CustomSprite__image_height)
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

class GameWindow(arcade.Window):
    """
    Clase para la ventana del juego.
    """
    def __init__(self, width, height, title):
        """
        Inicializa la ventana del juego.

        :param width: Ancho de la ventana.
        :param height: Alto de la ventana.
        :param title: Título de la ventana.
        """
        super().__init__(width, height, title)
        self.set_location(200, 200)

        # Configurar el color de fondo
        arcade.set_background_color(arcade.color.WHITE)

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
        """
        Configura los elementos iniciales del juego.
        """
        self.__player_list = arcade.SpriteList()

        # Obtener la ruta del directorio donde se encuentra el archivo de Python actual
        current_directory = os.path.dirname(os.path.abspath(__file__))

        # Construir la ruta completa al archivo 'ball.png'
        ball_path = os.path.join(current_directory, 'ball.png')

        # Crear sprites y animaciones para el jugador
        self.__player = CustomSprite(ball_path, 3, 5)
        self.__player_idle = CustomAnimation(3, self.__player, [0, 1, 2], 100)
        self.__player_idle.position = (800 // 2, 600 // 2)
        self.__player_idle.enabled = True
        self.__player_roll = CustomAnimation(3, self.__player, [7, 8, 9, 10, 11, 12], 60)
        self.__player_roll.position = (800 // 2, 600 // 2)
        self.__player_roll.enabled = False

        # Añadir animaciones a la lista de sprites
        self.__player_list.append(self.__player_idle)
        self.__player_list.append(self.__player_roll)

    def on_key_press(self, symbol, modifiers):
        """
        Maneja los eventos de presionar una tecla.
        """
        if symbol == arcade.key.RIGHT:
            self.__move_right = True
        if symbol == arcade.key.LEFT:
            self.__move_left = True

        # Activar animación de rodar y desactivar animación de estar quieto
        self.__player_idle.enabled = False
        self.__player_roll.enabled = True

    def on_key_release(self, symbol, modifiers):
        """
        Maneja los eventos de soltar una tecla.
        """
        self.__move_right = False
        self.__move_left = False

        # Activar animación de estar quieto y desactivar animación de rodar
        self.__player_idle.enabled = True
        self.__player_roll.enabled = False

    def on_draw(self):
        """
        Renderiza los elementos del juego.
        """
        arcade.start_render()
        for anim in self.__player_list:
            if anim.enabled:
                anim.draw()

    def on_update(self, delta_time):
        """
        Actualiza los elementos del juego.
        """
        for anim in self.__player_list:
            if anim.enabled:
                anim.update_animation()

        # Actualizar posición del jugador según las teclas presionadas
        if self.__move_right:
            self.__player_idle.update_position(self.__speed * delta_time, 0)
            self.__player_roll.update_position(self.__speed * delta_time, 0)
        if self.__move_left:
            self.__player_idle.update_position(-self.__speed * delta_time, 0)
            self.__player_roll.update_position(-self.__speed * delta_time, 0)

if __name__ == '__main__':
    GameWindow(800,600, "Ejemplo encapsulamento")
    arcade.run()