def reward_function(params):
    # Example of rewarding the agent to follow center line

    # Read input parameters
    track_width = params['track_width']
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    abs_steering_angle = abs(params['steering_angle'])
    speed = params['speed']
    wp= params['closest_waypoints'][1]

    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3 # likely crashed/ close to off track
    
    # Steering penalty threshold, change the number based on your action space setting
    ABS_STEERING_THRESHOLD = 15
    if abs_steering_angle > ABS_STEERING_THRESHOLD:
        reward *= 0.8

    # the car is somewhere in between the track borders 
    if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
        reward += 1.0
    else:
        reward = 1e-3
    
    if wp in (list(range(59,82))):
        if speed >=2 :
            reward = 1e-3
        reward += 1.0
        
    return float(reward)