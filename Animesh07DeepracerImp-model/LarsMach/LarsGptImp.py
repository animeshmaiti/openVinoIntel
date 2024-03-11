import math
def reward_function(params):
    # Extracting parameters
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    is_left_of_center = params['is_left_of_center']
    speed = params['speed']
    steering_angle = abs(params['steering_angle'])
    progress = params['progress']
    track_width = params['track_width']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
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
    
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]

    # Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
    # Convert to degree
    track_direction = math.degrees(track_direction)

    # Calculate the difference between the track direction and the heading direction of the car
    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff

    # Penalize the reward if the difference is too large
    DIRECTION_THRESHOLD = 10.0
    if direction_diff > DIRECTION_THRESHOLD:
        reward *= 0.5

    return float(reward)
