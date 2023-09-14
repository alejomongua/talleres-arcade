import arcade
import math

class CustomAnimation(arcade.AnimatedTimeBasedSprite):
    def __init__(self, scale, image_width, image_height, init_frame, end_frame):
        super().__init__(scale=scale, image_width=image_width, image_height=image_height)
        
        self.image_width= image_width
        self.image_height = image_height
        self.init_frame = init_frame
        self.end_frame = end_frame

        self.setup()

        
    def setup(self):
        for i in range(self.init_frame, self.end_frame+1):
            texture = arcade.load_texture("./ball.png", x=(i-(3*math.floor(i/3)))*self.image_width, y=math.floor(i/3)*self.image_height, width=self.image_width, height=self.image_height)
            self.textures.append(texture)

            frame = arcade.AnimationKeyframe(0, 0.00142, texture)
            self.frames.append(frame)

        self.center_x = 800 // 2
        self.center_y = 600 // 2
    

class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(200,200)

        arcade.set_background_color(arcade.color.WHITE)
        self.player_idle = None
        self.player_roll = None

        self.move_right = False
        self.move_left = True

        self.setup()

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.player_idle = CustomAnimation(3, 24, 24, 0, 2)
        self.player_idle.enabled = True
        self.player_roll = CustomAnimation(3, 24, 24, 7, 12)
        self.player_roll.enabled = False

        self.player_list.append(self.player_idle)
        self.player_list.append(self.player_roll)

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT:
            self.move_right = True
        if symbol == arcade.key.LEFT: 
            self.move_left = True
        
        self.player_idle.enabled = False
        self.player_roll.enabled = True

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT:
            self.move_right = False
        if symbol == arcade.key.LEFT: 
            self.move_left = False

        self.player_idle.enabled = True
        self.player_roll.enabled = False
    
    def on_draw(self):
        arcade.start_render()
        for anim in self.player_list:
            if(anim.enabled == True):
                anim.draw()

    def on_update(self, delta_time):
        for anim in self.player_list:
            if(anim.enabled == True):
                anim.update_animation()


GameWindow(800,600, "Ejemplo encapsulamento")
arcade.run()