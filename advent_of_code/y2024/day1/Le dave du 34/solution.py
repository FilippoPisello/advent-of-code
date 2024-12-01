import time

t0 = time.time()
with open("input.txt", "r") as file:
    data = file.readlines()

right_side = []
left_side = []

for i in data:
    left, right = i.split()
    left_side.append(int(left))
    right_side.append(int(right))


left_side = sorted(left_side)
right_side = sorted(right_side)
distance = 0

for i in range(len(left_side)):
    distance += abs(left_side[i-1] - right_side[i-1])

similarity = 0

for position_left_side_tmtc_la_famille in left_side:
    similarity += position_left_side_tmtc_la_famille * right_side.count(position_left_side_tmtc_la_famille)

t1= time.time()

print(distance) ## answer part 1
print(similarity) ## answer part 2

print("script run time: "+ str(round(t1-t0,5)) + " seconds")