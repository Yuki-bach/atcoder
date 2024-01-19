import time
start = time.perf_counter()

######################
X,Y = map(int, input().split())
print("Yes" if 0<=Y-X<=2 or 0<=X-Y<=3 else "No")

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder