import time
start = time.perf_counter()

######################
nums = set(map(int, input().split()))
print(len(nums))

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder