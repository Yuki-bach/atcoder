N, M = map(int, input().split())
S = input()
ans = 0
weared_M_num = 0
weared_A_num = 0

for s in S:
  if (s == '0'):
    weared_M_num = 0
    weared_A_num = 0
  elif (s == '1'):
    if (weared_M_num < M):
      weared_M_num += 1
    else:
      weared_A_num += 1
  else:
    weared_A_num += 1
  ans = max(ans, weared_A_num)
print(ans)


## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder