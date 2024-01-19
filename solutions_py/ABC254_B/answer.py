import time
start = time.perf_counter()

######################
N = int(input())

if N==1:
  exit(print(1))

ans = [[1], [1,1]]

for row in range(1, N-1):
  tmp = [1]
  for col in range(row):
    tmp.append(ans[row][col] + ans[row][col+1])
  tmp.append(1)
  ans.append(tmp)

for l in ans:
  print(*l)


#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder