#import pigpio

# Initialise GPIO PIGPIO connection
# Note pigpiod (PIGPIO daemon) must be running
# Start with 'sudo pigpiod'
#gpio = pigpio.pi()

motors = {'FL': 17, # Front left, connected to pin 17
          'FR': 27, # Front right, connected to pin 27
          'BL': 22, # Back left, connected to pin 22
          'BR': 23} # Back right, connected to pin 23


def scale(motorvalue):
    """Scales a value from 0-1000 to the correct range for controlling an ESC.
    
    Args:
        motorvalue: An integer from 0-1000.
    
    Returns:
        The value scaled to the correct range for an ESC (currently 1000-2000).
    
    Raises:
        ValueError: If motorvalue is outside 0-1000.
    """
    if motorvalue < 0 or motorvalue > 1000 or not(isinstance(motorvalue, int)):
        raise ValueError("Input motorvalue must be integer between 0 and 1000.")
    else:
        return motorvalue+1000


def set_all_motors(motorvalue):
    """Set all PWM motor control pulses to motorvalue.
    
    Args:
        motorvalue: an integer from 0-1000.
    """
    for motor, pin in motors.items():
        #gpio.set_servo_pulsewidth(pin, scale(motorvalue))
        print("Set pin {} to {} ({}%)".format(pin, scale(motorvalue), motorvalue/10))
        
        
def set_motor(motor, motorvalue):
    """Set PWM motor control pulse to motorvalue for motor.
    
    Args:
        motor: The motor to set to motorvalue. Must be a key of a motor in the
        `motors' dict.
        
        motorvalue: An integer from 0-1000.
    """
    #gpio.set_servo_pulsewidth(motors[motor], scale(motorvalue))
    print("Set pin {} to {} ({}%)".format(motors[motor], scale(motorvalue), motorvalue/10))