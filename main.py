def on_button_pressed_a():
    global x_position
    if x_position > 0:
        led.unplot(x_position, 4)
        x_position += -1
        led.plot(x_position, 4)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global x_position
    if x_position < 4:
        led.unplot(x_position, 4)
        x_position += 1
        led.plot(x_position, 4)
input.on_button_pressed(Button.B, on_button_pressed_b)

x_position = 0
x_position = 0
enemy_x = randint(0, 4)
enemy_y = 0
led.plot(x_position, 4)

def on_every_interval():
    global enemy_y, enemy_x
    if enemy_y < 4:
        led.unplot(enemy_x, enemy_y)
        enemy_y += 1
        led.plot(enemy_x, enemy_y)
    elif enemy_x == x_position and enemy_y == 4:
        enemy_x = randint(0, 4)
        enemy_y = -1
    else:
        basic.show_icon(IconNames.SAD)
loops.every_interval(500, on_every_interval)

def on_forever():
    pass
basic.forever(on_forever)
