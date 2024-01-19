import time
start = time.perf_counter()

######################
N = int(input())
print("\n".join([str(i) for i in range(N, -1, -1)]))

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder