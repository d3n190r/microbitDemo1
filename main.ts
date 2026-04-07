input.onButtonPressed(Button.A, function () {
    if (x_position > 0) {
        led.unplot(x_position, 4)
        x_position += -1
        led.plot(x_position, 4)
    }
})
input.onButtonPressed(Button.B, function () {
    if (x_position < 4) {
        led.unplot(x_position, 4)
        x_position += 1
        led.plot(x_position, 4)
    }
})
let x_position = 0
x_position = 0
let enemy_x = randint(0, 4)
let enemy_y = 0
led.plot(x_position, 4)
loops.everyInterval(500, function () {
    if (enemy_y < 4) {
        led.unplot(enemy_x, enemy_y)
        enemy_y += 1
        led.plot(enemy_x, enemy_y)
    } else if (enemy_x == x_position && enemy_y == 4) {
        enemy_x = randint(0, 4)
        enemy_y = -1
    } else {
        basic.showIcon(IconNames.Sad)
    }
})
basic.forever(function () {
	
})
