import time
start = time.perf_counter()

######################
s = input()
if s in ["ACE", "BDF", "CEG", "DFA", "EGB", "FAC", "GBD"]:
  print('Yes')
else:
  print(('No'))

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder