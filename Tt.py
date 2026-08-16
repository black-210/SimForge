print("=== AI Training Environment ===")

car_position = 0
car_speed = 10

obstacle_position = 100

print("Car position:", car_position)
print("Car speed:", car_speed)
print("Obstacle position:", obstacle_position)
state = {
    "car_position": car_position,
    "car_speed": car_speed,
    "obstacle_position": obstacle_position
}

print("State:", state)
action = input("AI action: ")

print("Received action:", action)
if action == "BRAKE":
    car_speed = 0

print("New car speed:", car_speed)
if car_position >= obstacle_position:
    result = "COLLISION"
else:
    result = "SAFE"
  
print("Environment result:", result)
if result == "SAFE":
    reward = 1
else:
    reward = -1

print("Reward:", reward)
for episode in range(10):
    print("\nEpisode:", episode)

    car_position = 0
    car_speed = 10

    print("Car reset.")
  
for episode in range(10):
  car_positicon = 0
  car_speed = 10
  obstacle_position = 100
  print("car positicon", car_positicon)
  print("car speed ", car_speed)
  print("obstacle position", obstacle_position)

  action = input ("ai action")
  print ("ai chose:" , action)
for step in range(10):

  print("step", step)
  action = input("ai action: " )
  if action == BRAKE:
   car_positicon = car_positicon + car_speed
