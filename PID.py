#Working with PID for drone stabilization

def pid_controller(desired_state, current_state, previous_error, kp, ki, kd, integral_sum):
    #Calculate for error
