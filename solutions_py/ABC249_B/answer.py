import time
start = time.perf_counter()

######################
S = input()

has_upper = False
has_lower = False
is_distinct = len(set(S)) == len(S)

for s in S:
  if str.isupper(s):
    has_upper = True
    break

for s in S:
  if str.islower(s):
    has_lower = True
    break

print("Yes" if has_lower and has_upper and is_distinct else "No")


#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder