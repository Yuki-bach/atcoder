import time
start = time.perf_counter()

######################
S = list(map(int, input()))
print(sum(range(10)) - sum(S))

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder