import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Playground!"


class Playground(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)


    def setup(self):
        pass

    def on_draw(self):
        self.clear()

    def on_update(self, delta_time):
        pass

    def on_key_press(self, key, key_modifiers):
        pass

def main():
    game = Playground(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
