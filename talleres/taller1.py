import arcade

arcade.open_window(600, 600, "Zombie sprite")
sprite_list = arcade.SpriteList()
img = 'images/zombie.png'
zombie = arcade.Sprite(img)
zombie.center_x = 250
zombie.center_y = 250
sprite_list.append(zombie)
sprite_list.draw()
arcade.finish_render()
arcade.run()
