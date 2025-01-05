#Working with PID for drone stabilization

def pid_controller(desired_state, current_state, previous_error, kp, ki, kd, integral_sum,dt):

    #calculate for error
    error = current_state - desired_state

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