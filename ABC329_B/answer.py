import time
start = time.perf_counter()

######################
N = int(input())
A = list(map(int, input().split()))
max_num = max(A)
print(max([num for num in A if num != max_num]))



#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder