import time
start = time.perf_counter()

######################
N = int(input())
S = input()
print("Yes" if ("ab" in S or "ba" in S) else "No")

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder