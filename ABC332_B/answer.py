K, G, M = map(int, input().split())
G_amount = 0
M_amount = 0

for _ in range(K):
  if (G_amount == G):
    G_amount = 0
  elif (M_amount == 0):
    M_amount = M
  else:
    moving = min(G-G_amount, M_amount)
    M_amount -= moving
    G_amount += moving
print(G_amount, M_amount)

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder