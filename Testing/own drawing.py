import arcade

arcade.open_window(500, 500, "Own Drawing")

arcade.set_background_color(arcade.csscolor.SKY_BLUE)

arcade.start_render()

arcade.draw_polygon_filled(((400, 475),
                            (300, 475),
                            (250, 400),
                            (250, 300),
                            (300, 225),
                            (400, 225),
                            (450, 300),
                            (450, 400)
                            ), arcade.csscolor.CRIMSON)

arcade.draw_rectangle_filled(300, 100, 600, 200, arcade.csscolor.GREEN)

arcade.draw_rectangle_filled(350, 175, 20, 100, arcade.csscolor.LIGHT_GREY)

arcade.draw_text("STOP", 285, 320, arcade.csscolor.WHITE, 50)

arcade.draw_circle_filled(20, 500, 50, arcade.csscolor.YELLOW)

arcade.draw_polygon_filled(((100, 0), (400, 0), (225, 230), (275, 230)), arcade.csscolor.BLACK)

arcade.draw_rectangle_filled(255, 220, 70, 40, arcade.csscolor.SKY_BLUE)

arcade.draw_polygon_filled(((245, 0), (255, 0), (270, 200), (268, 200)), arcade.csscolor.WHITE)

arcade.finish_render()

arcade.run()
