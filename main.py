radio.set_group(5)
servos.P2.set_angle(0)
#pins.servo_write_pin(AnalogPin.P2, 0)
on_received_number(3)
def on_received_number(receivedNumber):
    if receivedNumber == 0:
        basic.show_leds("""
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        """)
        pins.digital_write_pin(DigitalPin.P0, 1)
        pins.digital_write_pin(DigitalPin.P1, 0)
        servos.P2.set_angle(90)
        #pins.servo_write_pin(AnalogPin.P2, 0)
    elif receivedNumber == 1:
        basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
        pins.digital_write_pin(DigitalPin.P0, 0)
        pins.digital_write_pin(DigitalPin.P1, 1)
        servos.P2.set_angle(45)
        #pins.servo_write_pin(AnalogPin.P2, 30)
    elif receivedNumber == 3:
        basic.show_leds("""
        . . . . .
        . # # # .
        . # . # .
        . # # # .
        . . . . .
        """)
        pins.digital_write_pin(DigitalPin.P0, 0)
        pins.digital_write_pin(DigitalPin.P1, 0)
        servos.P2.set_angle(90)
        #pins.servo_write_pin(AnalogPin.P2, 0)

radio.on_received_number(on_received_number)

def on_button_pressed_a():
    on_received_number(0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    on_received_number(1)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_button_pressed_ab():
    on_received_number(3)
input.on_button_pressed(Button.AB, on_button_pressed_ab)
