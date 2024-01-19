from itertools import permutations
from math import factorial
C = [list(map(int, input().split())) for _ in range(3)]

check_idx_list = [
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8],
  [0, 3, 6],
  [1, 4, 7],
  [2, 5, 8],
  [0, 4, 8],
  [2, 4, 6]
]

def is_gakkari(sq):
  for i, j, k in check_idx_list:
    if (sq[i] != 0 and sq[j] != 0 and sq[k] == 0 and sq[i] == sq[j]):
      return True
    if (sq[j] != 0 and sq[k] != 0 and sq[i] == 0 and sq[j] == sq[k]):
      return True
    if (sq[k] != 0 and sq[i] != 0 and sq[j] == 0 and sq[k] == sq[i]):
      return True
  return False

cnt = 0
for p in permutations(range(9)):
  tmp_sq = [0] * 9
  for x in p:
    tmp_sq[x] = C[x//3][x%3]
    if is_gakkari(tmp_sq):
      cnt += 1
      break
total = factorial(9)
print((total - cnt) / total)








## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder