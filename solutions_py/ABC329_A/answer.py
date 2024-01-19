import time
start = time.perf_counter()

######################
S = list(input())
print(" ".join(S))

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder