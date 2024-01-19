import time
start = time.perf_counter()

######################
H, W = map(int, input().split())
matrix = [list(input()) for _ in range(H)]

## horizontal
for r in range(H):
  for c in range(W-4):
    if matrix[r][c:c+5] == ['s', 'n', 'u', 'k', 'e']:
      for u in range(5):
        print(f'{r+1} {c+u+1}')
      exit()
    if matrix[r][c:c+5] == ['e', 'k', 'u', 'n', 's']:
      for u in range(4, -1, -1):
        print(f'{r+1} {c+u+1}')
      exit()

## vertical
for c in range(W):
  for r in range(H-4):
    if [matrix[r+i][c] for i in range(5)]  == ['s', 'n', 'u', 'k', 'e']:
      for u in range(5):
        print(f'{r+u+1} {c+1}')
      exit()
    if [matrix[r+i][c] for i in range(5)]  == ['e', 'k', 'u', 'n', 's']:
      for u in range(4, -1, -1):
        print(f'{r+u+1} {c+1}')
      exit()

## diagonal
for r in range(H-4):
  for c in range(W-4):
    if [matrix[r+i][c+i] for i in range(5)] == ['s', 'n', 'u', 'k', 'e']:
      for u in range(5):
        print(f'{r+u+1} {c+u+1}')
      exit()
    if [matrix[r+i][c+i] for i in range(5)] == ['e', 'k', 'u', 'n', 's']:
      for u in range(4, -1, -1):
        print(f'{r+u+1} {c+u+1}')
      exit()

## anti-diagonal
for r in range(H-1, 3, -1):
  for c in range(W-4):
    if [matrix[r-i][c+i] for i in range(5)] == ['s', 'n', 'u', 'k', 'e']:
      for u in range(5):
        print(f'{r-u+1} {c+u+1}')
      exit()
    if [matrix[r-i][c+i] for i in range(5)] == ['e', 'k', 'u', 'n', 's']:
      for u in range(4, -1, -1):
        print(f'{r-u+1} {c+u+1}')
      exit()

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder