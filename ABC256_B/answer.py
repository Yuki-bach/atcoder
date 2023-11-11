import time
start = time.perf_counter()

######################
N = int(input())
players_pos = []
points = 0

for a in map(int, input().split()):
  players_pos = [player_pos+a for player_pos in players_pos]
  players_pos.append(a)
  points += sum(1 for value in players_pos if value >= 4)
  players_pos[:] = [value for value in players_pos if value < 4]

print(points)


#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder