import time
start = time.perf_counter()

######################
K = int(input())
if K < 60:
  print("21:{:0>2}".format(K))
else:
  print("22:{:0>2}".format(K-60))

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder