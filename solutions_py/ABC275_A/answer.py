import time
start = time.perf_counter()

######################
N = int(input())
H = list(map(int, input().split()))
max_num = max(H)
print(H.index(max_num) + 1)



#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder