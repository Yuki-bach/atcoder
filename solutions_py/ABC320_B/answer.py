import time
start = time.perf_counter()

######################
S = input()

def is_p(s):
  return s==s[::-1]

output = 0
for i in range(len(S)):
  for j in range(i, len(S)+1):
    if is_p(S[i:j]):
      output = max(output, len(S[i:j]))
print(output)

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder