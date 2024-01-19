import time
start = time.perf_counter()

######################
import numpy as np
N = int(input())
A = np.array([[int(digit) for digit in input()] for _ in range(N)])

max_indices = np.where(A == A.max())
start_points = list(zip(max_indices[0], max_indices[1]))

max_values = []
for point in start_points:
  x, y = point
  neighbors = [
    (i, j)
    for i in range(x-1,x+2)
    for j in range(y-1,y+2)
    if (i, j) != (x, y)
  ]

  for neighbor in neighbors:
    nx, ny = neighbor
    tmp = ""
    for i in range(N):
      tx = x+(nx-x)*i if x+(nx-x)*i<N else x+(nx-x)*i - N
      ty = y+(ny-y)*i if y+(ny-y)*i<N else y+(ny-y)*i - N
      tmp += str(A[tx][ty])
    max_values.append(int("".join(tmp)))
    
print(max(max_values))



#########################
end = time.perf_counter()
print(f"time: {(end-start)*1000:.3f}")

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder