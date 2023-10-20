import time
start = time.perf_counter()

######################
a, b = map(int, input().split())
is_connected = (b == a*2) or (b == a*2+1)
print("Yes" if is_connected else "No")

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder