import time
start = time.perf_counter()

######################
S = input()
T = input()
print("Yes" if S.find(T) != -1 else "No")

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder