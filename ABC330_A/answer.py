import time
start = time.perf_counter()

######################
N, L = map(int, input().split())
A = list(map(int, input().split()))
print(sum([a>=L for a in A]))

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder