import time
start = time.perf_counter()

######################
N = int(input())
def get(value):
  if value < 10: return str(value)
  return chr(ord("A")+value-10)

print(get(N//16) + get(N%16))



#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder