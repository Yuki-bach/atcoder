N = int(input())
T = input()
ans = [0, 0]
round = [[1, 0], [0, -1], [-1, 0], [0, 1]]
round_i = 0
direction = round[round_i]

for t in T:
  if (t == 'S'):
    ans[0] += direction[0]
    ans[1] += direction[1]
  else:
    round_i = round_i + 1 if round_i + 1 < 4 else 0
    direction = round[round_i]
print(*ans)

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder