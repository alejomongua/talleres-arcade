import arcade
from PIL import Image

class CustomSprite():
    def __init__(self, path:str, columns:int, rows:int):
        self.__image = Image.open(path)
        self.__image_width, self.__image_height = self.__image.size
        self.__columns = columns
        self.__rows = rows
        self.__path = path
        self.__spritesize_x = self.__image_width // columns
        self.__spritesize_y = self.__image_height // rows
        self.__textures = []
        self.__setup()

    def __setup(self):
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
        return self.__textures


class CustomAnimation(arcade.AnimatedTimeBasedSprite):
    def __init__(self, scale, custom_sprite:CustomSprite, frames:list, duration:int):
        self.__custom_sprite = custom_sprite
        super().__init__(scale=scale, 
                         image_width=custom_sprite._CustomSprite__image_width, 
                         image_height=custom_sprite._CustomSprite__image_height)
        self.__frames_ = frames
        self.__duration = duration
        self.__setup()

    def __setup(self):
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
        return self.center_x, self.center_y
    
    @position.setter
    def position(self, value):
        self.center_x, self.center_y = value

    def update_position(self, delta_x, delta_y):
        self.center_x += delta_x
        self.center_y += delta_y

        if(self.center_x > 824):
            self.center_x = -24
        if(self.center_x < -24):
            self.center_x = 823

        if (self.center_y > 624):
            self.center_y = -24
        if (self.center_y < -24):
            self.center_y = 623

    

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
        self.player_idle.position = (800 //2, 600 //2)
        self.player_idle.enabled = True
        self.player_roll = CustomAnimation(3, self.player, [7,8,9,10,11,12], 60)
        self.player_roll.position = (800 //2, 600 //2)
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
            self.player_idle.update_position(self.speed * delta_time, 0)
            self.player_roll.update_position(self.speed * delta_time, 0)
        if self.move_left:
            self.player_idle.update_position(-self.speed * delta_time, 0)
            self.player_roll.update_position(-self.speed * delta_time, 0)


GameWindow(800,600, "Ejemplo encapsulamento")
arcade.run()