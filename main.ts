radio.setGroup(5)
servos.P2.setAngle(0)
on_received_number(3)
function on_received_number(receivedNumber: number) {
    if (receivedNumber == 0) {
        basic.showLeds(`
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        `)
        pins.digitalWritePin(DigitalPin.P0, 1)
        pins.digitalWritePin(DigitalPin.P1, 0)
        servos.P2.setAngle(90)
    } else if (receivedNumber == 1) {
        basic.showLeds(`
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        `)
        pins.digitalWritePin(DigitalPin.P0, 0)
        pins.digitalWritePin(DigitalPin.P1, 1)
        servos.P2.setAngle(60)
    } else if (receivedNumber == 3) {
        // pins.servo_write_pin(AnalogPin.P2, 30)
        basic.showLeds(`
        . . . . .
        . # # # .
        . # . # .
        . # # # .
        . . . . .
        `)
        pins.digitalWritePin(DigitalPin.P0, 0)
        pins.digitalWritePin(DigitalPin.P1, 0)
        servos.P2.setAngle(90)
    }
    
}

radio.onReceivedNumber(on_received_number)
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    on_received_number(0)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    on_received_number(1)
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    on_received_number(3)
})
