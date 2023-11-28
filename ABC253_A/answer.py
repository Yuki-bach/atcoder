import time
start = time.perf_counter()

######################
import numpy as np
a = list(map(int, input().split()))
print("Yes" if np.median(a) == a[1] else "No")

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder