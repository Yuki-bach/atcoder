import time
start = time.perf_counter()

######################
M = int(input())
D = list(map(int, input().split()))

center_date = sum(D) // 2 + 1
counter = 0
for i in range(M):
  if counter + D[i] < center_date:
    counter += D[i]
  else:
    print(i+1, center_date - counter)
    exit()

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder