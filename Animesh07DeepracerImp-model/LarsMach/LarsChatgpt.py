# Training Time = 2hr
# Time =
import math

def reward_function(params):
    # Extracting parameters
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    abs_steering = abs(params['steering_angle'])
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
    progress = params['progress']
    objects_distance = params['objects_distance']
    objects_heading = params['objects_heading']
    objects_speed = params['objects_speed']
    waypoints = params['waypoints']

    # Set the speed threshold based on your action space
    SPEED_THRESHOLD = 2.0

    # Initialize reward
    reward = 1.0

    # Penalty for going off track or being too slow
    if not all_wheels_on_track:
        reward = 1e-3
    elif speed < SPEED_THRESHOLD:
        reward = 0.1
    else:
        # High reward if the car stays on track and goes fast
        reward = 1.0

    # Distance markers from the center of the track
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Reward based on distance from center
    if distance_from_center <= marker_1:
        reward += 1.0
    elif distance_from_center <= marker_2:
        reward += 0.5
    elif distance_from_center <= marker_3:
        reward += 0.1
    else:
        reward += 1e-3

    # Penalty for excessive steering
    ABS_STEERING_THRESHOLD = 20.0
    if abs_steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8

    # Direction difference between track and car heading
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
    track_direction = math.degrees(track_direction)
    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff

    # Penalize large direction difference
    DIRECTION_THRESHOLD = 10.0
    if direction_diff > DIRECTION_THRESHOLD:
        reward *= 0.5

    # Reward for staying close to objects (optional)
    for obj_dist, obj_heading, obj_speed in zip(objects_distance, objects_heading, objects_speed):
        if obj_dist < track_width / 2:  # considering objects within half the track width
            reward += 0.1 * (track_width / 2 - obj_dist)  # closer objects yield higher reward

    # Reward for making progress
    PROGRESS_THRESHOLD = 80.0  # Adjust as needed
    if progress > PROGRESS_THRESHOLD:
        reward += 2.0

    return float(reward)
