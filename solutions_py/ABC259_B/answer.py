import time
start = time.perf_counter()

######################
import math
a,b,d = map(int, input().split())
rad = math.radians(d)
x_prime = a * math.cos(rad) - b * math.sin(rad)
y_prime = a * math.sin(rad) + b * math.cos(rad)
print(x_prime, y_prime)

#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder