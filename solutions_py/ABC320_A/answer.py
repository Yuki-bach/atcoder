import time
start = time.perf_counter()

######################
A, B = list(map(int, input().split()))
print(A**B + B**A)

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder