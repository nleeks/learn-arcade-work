import arcade

arcade.open_window(500, 500, "Own Drawing")

# draw sky

arcade.set_background_color(arcade.csscolor.SKY_BLUE)

arcade.start_render()

# draw a stop sign

arcade.draw_polygon_filled(((400, 475),
                            (300, 475),
                            (250, 400),
                            (250, 300),
                            (300, 225),
                            (400, 225),
                            (450, 300),
                            (450, 400)
                            ), arcade.csscolor.CRIMSON)

# draw grass

arcade.draw_rectangle_filled(300, 100, 600, 200, arcade.csscolor.GREEN)

# draw stop sign post

arcade.draw_rectangle_filled(350, 175, 20, 100, arcade.csscolor.LIGHT_GREY)

# draw the stop text

arcade.draw_text("STOP", 285, 320, arcade.csscolor.WHITE, 50)

# draw the sun

arcade.draw_circle_filled(20, 500, 50, arcade.csscolor.YELLOW)

# draw the road

arcade.draw_polygon_filled(((100, 0), (400, 0), (225, 230), (275, 230)), arcade.csscolor.BLACK)

# a small patch for the road extending too far

arcade.draw_rectangle_filled(255, 220, 70, 40, arcade.csscolor.SKY_BLUE)

# draw the line down the middle of the road

arcade.draw_polygon_filled(((245, 0), (255, 0), (270, 200), (268, 200)), arcade.csscolor.WHITE)

arcade.finish_render()

arcade.run()
