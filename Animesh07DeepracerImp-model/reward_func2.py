def reward_function(params):
    # Example of rewarding the agent to follow center line

    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    wp = params['closest_waypoints'][1]
    SPEED_THRESHOLD = 2.5
    reward = 0

    if not all_wheels_on_track:
        # Penalize if the car goes off track
        reward = 1e-3
    elif speed < SPEED_THRESHOLD:
        # Penalize if the car goes too slow
        reward = 0.5
    else:
        # High reward if the car stays on track and goes fast
        reward = 1.0

    if reward == 1e-3:
        reward = 1e-3
    elif wp in (list(range(59, 82))):
        if speed >= 2:
            reward = 1e-3
        reward += 1.0

    return float(reward)
