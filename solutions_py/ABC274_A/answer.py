import time
start = time.perf_counter()

######################
A, B = map(int, input().split())
print(f"{round(B/A, 3): .3f}")

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder