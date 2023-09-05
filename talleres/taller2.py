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

class Pato:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dibujar(self):
        # Cuerpo del pato
        arcade.draw_ellipse_filled(self.x, self.y, 40, 30, arcade.color.YELLOW)
        # Pico del pato
        arcade.draw_triangle_filled(self.x + 20, self.y, self.x + 30, self.y + 5, self.x + 30, self.y - 5, arcade.color.ORANGE)
        # Ojo del pato
        arcade.draw_circle_filled(self.x + 15, self.y + 5, 3, arcade.color.BLACK)

class Perro:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dibujar(self):
        # Cuerpo del perro
        arcade.draw_ellipse_filled(self.x, self.y, 60, 40, arcade.color.BROWN)
        
        # Cabeza del perro
        arcade.draw_circle_filled(self.x + 40, self.y + 10, 20, arcade.color.BROWN)
        
        # Ojos del perro
        arcade.draw_circle_filled(self.x + 45, self.y + 15, 3, arcade.color.BLACK)
        arcade.draw_circle_filled(self.x + 35, self.y + 15, 3, arcade.color.BLACK)
        
        # Nariz del perro
        arcade.draw_circle_filled(self.x + 40, self.y + 5, 3, arcade.color.BLACK)
        
        # Orejas del perro
        arcade.draw_ellipse_filled(self.x + 30, self.y + 20, 10, 20, arcade.color.DARK_BROWN)
        arcade.draw_ellipse_filled(self.x + 50, self.y + 20, 10, 20, arcade.color.DARK_BROWN)

class MiniMundo(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    def setup(self):
        arcade.set_background_color(arcade.color.SKY_BLUE)

    def on_draw(self):
        arcade.start_render()

        # Dibujar árboles
        for x in range(100, 701, 150):
            arbol = Arbol(x, 300)
            arbol.dibujar()

        # Dibujar animales
        for x in range(150, 651, 150):
            animal = Pato(x, 500)
            animal.dibujar()

        # Dibujar perros
        perro = Perro(400, 100)
        perro.dibujar()

if __name__ == "__main__":
    app = MiniMundo()
    app.setup()
    arcade.run()
