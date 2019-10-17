#!/usr/bin/env python 3

#Created by: Euel Yirga
#Created on: October 2019
#this will constrain the sprite from moving off the screen

import ugame
import stage
import constants

# an image bank for CircuitPython
image_bank_1 = stage.Bank.from_bmp16("ball.bmp")
# a list of sprites that will be updated every frame
sprites = []


def main():
    # this function sets the background

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_1, 10, 8)

    # create a sprite
    # parameters (image_bank_1, image # in bank, x, y)
    ball_one = stage.Sprite(image_bank_1, 3, 64, 56)
    sprites.append(ball_one)
    ball_two = stage.Sprite(image_bank_1, 2, 75, 56)
    sprites.insert(0, ball_two)  # insert at top of sprite list

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the background layer
    game.layers = sprites + [background]
    # render the background
    # most likely you will only render background once per scene
    game.render_block()

    while True:
        # get user inputs
        keys = ugame.buttons.get_pressed()
        # print(keys)

        if keys & ugame.K_UP != 0:
            if ball_one.y < 0:
                ball_one.move(ball_one.x, 0)
            else:
                ball_one.move(ball_one.x, ball_one.y - 1)
            pass
        if keys & ugame.K_DOWN != 0:
            if ball_one.y > constants.SCREEN_Y - constants.SCREEN_GRID_Y:
                ball_one.move(ball_one.x, constants.SCREEN_Y -
                              constants.SPRITE_SIZE)
            else:
                ball_one.move(ball_one.x, ball_one.y + 1)
            pass
        if keys & ugame.K_LEFT != 0:
            if ball_one.x < 0:
                ball_one.move(0, ball_one.y)
            else:
                ball_one.move(ball_one.x - 1, ball_one.y)
            pass
        if keys & ugame.K_RIGHT != 0:
            if ball_one.x > constants.SCREEN_X - constants.SCREEN_GRID_X:
                ball_one.move(constants.SCREEN_X - constants.SPRITE_SIZE,
                              ball_one.y)
            else:
                ball_one.move(ball_one.x + 1, ball_one.y)
            pass
        # update game logic

        # redraw sprtie list
        game.render_sprites(sprites)
        game.tick()  # wait until refresh rate finishes


if __name__ == "__main__":
    main()
