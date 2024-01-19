import time
start = time.perf_counter()

######################
N = int(input())
A = list(map(int, input().split()))
is_called_list = [False for _ in range(N)]

for idx, a in enumerate(A):
  if is_called_list[idx] == False:
    is_called_list[a-1] = True

not_called_list = [idx+1 for idx, is_called in enumerate(is_called_list) if is_called==False]
print(len(not_called_list))
print(*not_called_list)

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder