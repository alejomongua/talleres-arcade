import arcade
import math
from PIL import Image

class CustomSprite():
    def __init__(self, path:str, columns:int, rows:int):

        image = Image.open(path)

        self.image_width, self.image_height = image.size

        self.columns = columns
        self.rows = rows
        self.path = path
        self.spritesize_x = self.image_width // columns
        self.spritesize_y = self.image_height // rows
        self.textures = []
        self.setup()

    def setup(self):
        for i in range(self.rows):
            for j in range(self.columns):
                texture = arcade.load_texture(self.path, 
                                              x=j*self.spritesize_x,
                                              y=i*self.spritesize_y,
                                              width=self.spritesize_x,
                                              height=self.spritesize_y)
                self.textures.append(texture)


class CustomAnimation(arcade.AnimatedTimeBasedSprite):
    def __init__(self, scale, custom_sprite:CustomSprite, frames:list, duration:int):
        self.custom_sprite = custom_sprite

        super().__init__(scale=scale, image_width=custom_sprite.image_width, image_height=custom_sprite.image_height)

        self.frames_ = frames
        self.duration = duration

        self.setup()


    def setup(self):
        for i in range(len(self.custom_sprite.textures)):
            if i not in self.frames_:
                continue
            texture = self.custom_sprite.textures[i]
            self.textures.append(texture)
            frame = arcade.AnimationKeyframe(0, self.duration, texture)
            self.frames.append(frame)
    

class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(200,200)

        arcade.set_background_color(arcade.color.WHITE)
        self.player = None
        self.player_idle = None
        self.player_roll = None
        self.speed = 300

        self.move_right = False
        self.move_left = False

        self.setup()

    def setup(self):
        self.player_list = arcade.SpriteList()

        self.player = CustomSprite("./ball.png", 3, 5)
        
        self.player_idle = CustomAnimation(3, self.player, [0,1,2], 100)
        self.player_idle.center_x = 800 //2
        self.player_idle.center_y = 600 //2
        self.player_idle.enabled = True
        self.player_roll = CustomAnimation(3, self.player, [7,8,9,10,11,12], 60)
        self.player_roll.center_x = 800 //2
        self.player_roll.center_y = 600 //2
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

        if self.move_right:
            self.player_idle.center_x += self.speed * delta_time
            self.player_roll.center_x += self.speed * delta_time
        if self.move_left:
            self.player_idle.center_x -= self.speed * delta_time
            self.player_roll.center_x -= self.speed * delta_time

        if(self.player_idle.center_x > 824):
            self.player_idle.center_x = -24
            self.player_roll.center_x = -24

        if(self.player_idle.center_x < -24):
            self.player_idle.center_x = 823
            self.player_roll.center_x = 823
        


GameWindow(800,600, "Ejemplo encapsulamento")
arcade.run()