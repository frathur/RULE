#Working with PID for drone stabilization

def pid_controller(desired_state, current_state, previous_error, kp, ki, kd, integral_sum,dt):

    #calculate for error
    error =  desired_state - current_state

    #Proportional Gained
    p_term = kp * error

    #Integral Gained
    integral_sum += error * dt
    i_term = ki * integral_sum

    #Derivative Gained
    derivative = (error - previous_error) / dt
    d_term = kd * derivative

    #Calculate PID
    output = p_term + i_term + d_term

    previous_error = error

    return output , previous_error, integral_sum

roll_output, roll_previous_error, roll_integral_sum = pid_controller()
yaw_output, yaw_previous_error, yaw_integral_sum = pid_controller()
pitch_output, pitch_previous_error, pitch_integral_sum = pid_controller()



