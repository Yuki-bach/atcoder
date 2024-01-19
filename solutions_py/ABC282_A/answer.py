import time
start = time.perf_counter()

######################
K = int(input())
output = ""
for i in range(65, 65 + K):
  output += chr(i)
print(output)

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder