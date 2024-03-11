def reward_function(params):
    # Extracting parameters
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    is_left_of_center = params['is_left_of_center']
    speed = params['speed']
    steering_angle = abs(params['steering_angle'])
    progress = params['progress']
    track_width = params['track_width']
    steps = params['steps']
    is_offtrack = params['is_offtrack']
    track_length = params['track_length']

    # Initialize reward
    reward = 1.0

    # Penalty for going off track, excessive steering, or being too slow
    if not all_wheels_on_track or is_offtrack or steering_angle > 20 or speed < 1.0:
        reward = 1e-3
    else:
        # High reward if the car stays on track and goes fast
        reward = 1.0

    # Penalty for distance from center
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    if distance_from_center >= marker_3:
        reward *= 0.5
    elif distance_from_center >= marker_2:
        reward *= 0.8
    elif distance_from_center >= marker_1:
        reward *= 0.9

    # Reward for staying on the correct side of the track
    if is_left_of_center:
        reward += 0.1
    else:
        reward -= 0.1

    # Reward for speed
    SPEED_THRESHOLD = 2.0
    if speed > SPEED_THRESHOLD:
        reward += 1.0

    # Reward for progress
    PROGRESS_THRESHOLD = 80.0  # Adjust as needed
    if progress > PROGRESS_THRESHOLD:
        reward += 2.0

    # Penalty for excessive steps (optional)
    MAX_STEPS = 500  # Adjust as needed
    if steps > MAX_STEPS:
        reward *= 0.5

    # Penalty for distance traveled (optional)
    DISTANCE_PENALTY_THRESHOLD = track_length / 2
    if progress < DISTANCE_PENALTY_THRESHOLD:
        reward *= 0.5

    return float(reward)
