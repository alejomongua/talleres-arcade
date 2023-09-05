import arcade

# Constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Mini-Mundo en Arcade"

class Arbol:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dibujar(self):
        arcade.draw_lrtb_rectangle_filled(self.x, self.x + 20, self.y, self.y - 40, arcade.color.BROWN)
        arcade.draw_circle_filled(self.x + 10, self.y, 30, arcade.color.DARK_GREEN)

class Animal:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dibujar(self):
        arcade.draw_circle_filled(self.x, self.y, 20, arcade.color.BLUE)

class Edificio:
    def __init__(self, x, y, altura):
        self.x = x
        self.y = y
        self.altura = altura

    def dibujar(self):
        arcade.draw_lrtb_rectangle_filled(self.x, self.x + 50, self.y, self.y - self.altura, arcade.color.GRAY)

class MiniMundo(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    def setup(self):
        arcade.set_background_color(arcade.color.SKY_BLUE)

    def on_draw(self):
        arcade.start_render()

        # Dibujar árboles
        for x in range(100, 701, 150):
            arbol = Arbol(x, 100)
            arbol.dibujar()

        # Dibujar animales
        for x in range(150, 651, 150):
            animal = Animal(x, 300)
            animal.dibujar()

        # Dibujar edificios
        for x in range(200, 601, 200):
            edificio = Edificio(x, 500, 50)
            edificio.dibujar()

if __name__ == "__main__":
    app = MiniMundo()
    app.setup()
    arcade.run()
