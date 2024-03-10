distance_from_center = [1,3,5,4,4]
track_width = 10
steering = [17, 12, 5, 20, 10] # Only need the absolute steering angle
# Calculate 3 markers that are at varying distances away from the center line
marker_1 = 0.1 * track_width
marker_2 = 0.25 * track_width
marker_3 = 0.5 * track_width
# Give higher reward if the agent is closer to center line and vice versa
total_reward = 0
for i in range(5):
    if distance_from_center[i] <= marker_1:
        reward = 1
    elif distance_from_center[i] <= marker_2:
        reward = 0.5
    elif distance_from_center[i] <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track
    # Steering penality threshold, change the number based on your action space setting
    ABS_STEERING_THRESHOLD = 15
    # Penalize reward if the agent is steering too much
    if steering[i] > ABS_STEERING_THRESHOLD:
        reward *= 0.8
    total_reward += reward
print(total_reward)