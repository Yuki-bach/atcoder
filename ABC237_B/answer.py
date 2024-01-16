H, W = map(int, input().split())
arr = []
for _ in range(H):
  arr.append(list(map(int, input().split())))

transposed_arr = [[arr[j][i] for j in range(H)] for i in range(W)]
for row in transposed_arr:
  print(*row)

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder