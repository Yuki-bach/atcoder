import time
start = time.perf_counter()

######################
s = input()
boin = ['a', 'i', 'u', 'e', 'o']
output = ""
for c in s:
  if c not in boin:
    output += c
print(output)

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder