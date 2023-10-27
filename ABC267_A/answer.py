import time
start = time.perf_counter()

######################
S = input()
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
print(len(days) - days.index(S))

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder