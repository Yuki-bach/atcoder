import time
start = time.perf_counter()

######################
nums = list(map(int, input().split()))
counter = {num: 0 for num in nums}
for num in nums:
  counter[num] += 1
print("Yes" if set(counter.values()) == {2, 3} else "No")


#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder