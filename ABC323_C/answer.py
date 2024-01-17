N, M = map(int, input().split())
A = list(map(int, input().split()))
S = [input() for _ in range(N)]

scores = []
for i in range(N):
  score = sum([A[j] for j in range(M) if S[i][j] == "o"]) + (i + 1)
  scores.append(score)

for i in range(N):
  maxScore = max(scores[:i] + scores[i + 1:])
  arr_not_solved = sorted([A[j] for j in range(M) if S[i][j] == "x"])[::-1]
  curr_score = scores[i]
  j = 0
  while j < len(arr_not_solved):
    if curr_score > maxScore:
      print(j)
      break
    curr_score += arr_not_solved[j]
    j += 1
  if j == len(arr_not_solved):
    print(j)


## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder