from collections import defaultdict
x_dict = defaultdict(int)
y_dict = defaultdict(int)

for _ in range(3):
  x, y = map(int, input().split())
  x_dict[x] += 1
  y_dict[y] += 1
ans_x = [key for key, value in x_dict.items() if value == 1][0]
ans_y = [key for key, value in y_dict.items() if value == 1][0]

print(ans_x, ans_y)
## counter使ったほうが良かったか


## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder