#Import barometer sensor

#Initial PID gains
kp = 1.0
ki = 0.5
kd = 0.1

#Initial values
previous_error = 0
integral = 0
dt = 0.01

def altitude_hold(target_altitude, current_altitude):
    global previous_error, integral, dt

    #Error
    error = target_altitude - current_altitude

    #Proportional term
    p_term = kp * error

    #Integral term
    integral += error * dt
    i_term = ki * integral

    #Derivative term
    derivative = (error - previous_error) / dt
    d_term = kd * derivative

    #Compute PID value
    output = p_term + i_term + d_term

    throttle_adjustment = output

    previous_error = error

    return  throttle_adjustment

current_altitude = barometer.read_altitude()
target_altitude = 10.0

altitude_hold(target_altitude, current_altitude)