import arcade

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Window"


class MyGame(arcade.Window):
    """
    Clase Principal 'MyGame'
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """
        Función estandar para aplicar la configuración y Setup de los objetos de juego. 
        Es ideal no solo para iniciar el juego sino además para aplicar procesos de reset."""
        pass

    def on_draw(self):
        """
        Aplica el dibujado yu renderizado de objetos en pantalla."""

        self.clear()
        # Code to draw the screen goes here


def main():
    """Función principal 'Main'"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()