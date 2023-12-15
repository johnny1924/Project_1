# the sort line between two points is a straight line
# # the sort line between two points is a straight line
# # write a python code that receives x'y of 2 points and
# # if the points are not equals or the same calc the distance between the 2 points
# # d = sqrt((x2-x1)^2 +(y2-y1)^2)

# import math
#
# def calculate_distance(p1, y1, p2, y2):
#     if x1 == x2 and y1 == y2:
#         return "The points are the same."
#     else:
#         distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
#         return f"The distance between the points ({x1}, {y1}) and ({x2}, {y2}) is: {distance}"
#
# # Example usage:
# x1 = float(input("Enter x coordinate of the first point: "))
# y1 = float(input("Enter y coordinate of the first point: "))
# x2 = float(input("Enter x coordinate of the second point: "))
# y2 = float(input("Enter y coordinate of the second point: "))
#
# result = calculate_distance(x1, y1, x2, y2)
# print(result)

# ===============elevator=================
# in my building there are 2 elevators we call them the left and the right
# the building manager (av bayet) called and wants to program the elevator
# the algorithm works like this:
# we calc the abs distance and we check which of the elevators are closer
# the code will print the name of the elevator that is going to pick you up

# write a python code that receives the left elevator position and the right elevator position
# and the call floor and print which elevator is coming.

# left_p = int(input("Enter the left elevator position: "))
# right_p = int(input("Enter the right elevator position: "))
# call = int(input("Enter the call floor: "))

# left_distance = abs(left_p - call)
# right_distance = abs(right_p - call)

# if left_distance < right_distance:
   # print('Left elevator is coming')
# elif right_distance < left_distance:
   # print('Right elevator is coming')
# else:
   # print('Both of them are the same distance, anyone can come.')
