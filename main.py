"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "My Epic Game"
MOVEMENT_SPEED = 3

class PlayerSprite:
    def __init__(self, pos_x, pos_y, vel_x, vel_y, width, height, color):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.height = height
        self.width = width
        self.color = color

    def draw(self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.height, self.width, self.color)

    def update(self):
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y

class TileSprite:
    def __init__(self,pos_x, pos_y, width, height, color):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.height = height
        self.width = width
        self.color = color

    def draw(self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.height, self.width, self.color)

class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK)

        # If you have sprite lists, you should create them here,
        self.player = PlayerSprite(50,50, 0,0, 20, 20, arcade.color.WHITE)
        self.tile = TileSprite(SCREEN_WIDTH/2, 10, 20, 20, arcade.color.BLUE)

    def setup(self):
        # Create your sprites and sprite lists here
        pass

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()
        # Call draw() on all your sprite lists below
        self.player.draw()
        self.tile.draw()

    def check_for_collission(self, object1, object2):
        if object1.pos_x + object1.width > object2.pos_x and object1.pos_x < object2.pos_x + object2.width and object1.pos_y + object1.height > object2.pos_y and object1.pos_y < object2.pos_y + object2.height:
            print("collission")
            if object1.vel_x > 0:
                object1.pos_x = object2.pos_x - object1.width
            if object1.vel_x < 0:
                object1.pos_x = object2.pos_x + object2.width
            if object1.vel_y > 0:
                object1.pos_y = object2.pos_y - object2.height
            if object1.vel_y < 0:
                object1.pos_y = object2.pos_y + object1.height

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.player.update()
        self.check_for_collission(self.player, self.tile)

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        if key == arcade.key.LEFT:
            self.player.vel_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player.vel_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.player.vel_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player.vel_y = -MOVEMENT_SPEED

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.vel_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.vel_y = 0

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()