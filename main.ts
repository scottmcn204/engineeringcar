radio.setGroup(5)
let drsOn = false
on_received_number(3)
function on_received_number(receivedNumber: number) {
    let drsOn: boolean;
    let drsON: boolean;
    if (receivedNumber == 0) {
        basic.showLeds(`
        # # # # #
        # . . . .
        # # # # #
        . . . . #
        # # # # #
        `)
        pins.digitalWritePin(DigitalPin.P0, 1)
        pins.digitalWritePin(DigitalPin.P1, 0)
        if (drsOn == true) {
            drsOn = false
            servos.P2.setAngle(0)
        }
        
    } else if (receivedNumber == 1) {
        basic.showLeds(`
        # # # # #
        # . . . .
        # # # # #
        # . . . .
        # . . . .
        `)
        pins.digitalWritePin(DigitalPin.P0, 0)
        pins.digitalWritePin(DigitalPin.P1, 1)
        if (drsOn == false) {
            drsON = true
            servos.P2.setAngle(30)
        }
        
    } else if (receivedNumber == 3) {
        basic.showLeds(`
        . . . . .
        . # # # .
        . # . # .
        . # # # .
        . . . . .
        `)
        pins.digitalWritePin(DigitalPin.P0, 0)
        pins.digitalWritePin(DigitalPin.P1, 0)
        if (drsOn == true) {
            drsOn = false
            servos.P2.setAngle(0)
        }
        
    }
    
}

radio.onReceivedNumber(on_received_number)
