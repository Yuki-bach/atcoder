import time
start = time.perf_counter()

######################
a,b,c,d = map(int, input().split())
print((a+b) * (c-d))
print("Takahashi")

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder