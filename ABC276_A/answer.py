import time
start = time.perf_counter()

######################
S = input()
idx_reversed = S[::-1].find('a') ## rfind() is better
print(len(S) - idx_reversed if idx_reversed != -1 else -1 )

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder