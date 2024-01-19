N, Q = map(int, input().split())
dragon = [[i, 0] for i in range(N, 0, -1)]

for _ in range(Q):
  [num, C] = input().split()
  if (num == '1'):
    head = dragon[-1].copy()
    if (C == 'R'):
      head[0] += 1
    if (C == 'L'):
      head[0] -= 1
    if (C == 'U'):
      head[1] += 1
    if (C == 'D'):
      head[1] -= 1
    dragon.append(head)
  else:
    print(*dragon[-int(C)])


## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder