radio.set_group(5)
drsOn = False

def on_received_number(receivedNumber):
    if receivedNumber == 0:
        basic.show_leds("""
        # # # # #
        # . . . .
        # # # # #
        . . . . #
        # # # # #
        """)
        pins.digital_write_pin(DigitalPin.P0, 1)
        pins.digital_write_pin(DigitalPin.P1, 0)
        if drsOn == True:
            drsOn = False
            servos.P2.set_angle(0)
    elif receivedNumber == 1:
        basic.show_leds("""
        # # # # #
        # . . . .
        # # # # #
        # . . . .
        # . . . .
        """)
        pins.digital_write_pin(DigitalPin.P0, 0)
        pins.digital_write_pin(DigitalPin.P1, 1)
        if drsOn == False:
            drsON = True
            servos.P2.set_angle(30)
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
        if drsOn == True:
            drsOn = False
            servos.P2.set_angle(0)


radio.on_received_number(on_received_number)
