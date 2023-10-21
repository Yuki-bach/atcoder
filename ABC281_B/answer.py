import time
start = time.perf_counter()

######################
S = input()
is_true = (
  len(S)==8 and
  "A"<=S[0]<="Z" and
  "A"<=S[-1]<="Z" and
  S[1:7].isdigit() and 100000 <= int(S[1:7]) <= 999999
)
print("Yes" if is_true else "No")

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder