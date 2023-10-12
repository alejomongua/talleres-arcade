import arcade
import os

# Definición de la clase base: Plataforma
class Plataforma(arcade.Sprite):
    def __init__(self, imagen, escala):
        super().__init__(imagen, escala)

    def update(self):
        pass  # Las plataformas base no se mueven

# Definición de la clase derivada: PlataformaHorizontal
class PlataformaHorizontal(Plataforma):
    def __init__(self, imagen, escala, velocidad):
        super().__init__(imagen, escala)
        self.velocidad = velocidad

    def update(self):
        self.center_x += self.velocidad  # Mover horizontalmente
        if self.left < 0 or self.right > 800:  # Suponiendo una ventana de 800 píxeles de ancho
            self.velocidad *= -1  # Cambiar la dirección

# Definición de la clase derivada: PlataformaVertical
class PlataformaVertical(Plataforma):
    def __init__(self, imagen, escala, velocidad):
        super().__init__(imagen, escala)
        self.velocidad = velocidad

    def update(self):
        self.center_y += self.velocidad  # Mover verticalmente
        if self.bottom < 0 or self.top > 600:  # Suponiendo una ventana de 600 píxeles de alto
            self.velocidad *= -1  # Cambiar la dirección


# Creación de la ventana del juego
class Juego(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Ejemplo de Herencia y Polimorfismo con Plataformas")

        self.lista_plataformas = arcade.SpriteList()

        self.crear_plataforma(PlataformaHorizontal, 400, 300, 2)
        self.crear_plataforma(PlataformaVertical, 200, 300, 2)
        self.crear_plataforma(Plataforma, 600, 100)


    def crear_plataforma(self, ClasePlataforma, x, y, velocidad=None):
        plataforma_path = os.path.join(os.path.dirname(__file__), "plataforma.png")
        escala = 1.0
        if velocidad:
            plataforma = ClasePlataforma(plataforma_path, escala, velocidad)
        else:
            plataforma = ClasePlataforma(plataforma_path, escala)
        plataforma.center_x = x
        plataforma.center_y = y
        self.lista_plataformas.append(plataforma)

    def on_draw(self):
        arcade.start_render()  # Iniciar el proceso de dibujo
        self.lista_plataformas.draw()  # Dibujar todas las plataformas

    def on_update(self, delta_time):
        self.lista_plataformas.update()  # Actualizar todas las plataformas

# Ejecución del juego
if __name__ == "__main__":
    juego = Juego()
    arcade.run()
