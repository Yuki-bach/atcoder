N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
same_cnt = 0
diff_cnt = 0

for i, a in enumerate(A):
  if (a == B[i]):
    same_cnt += 1
  if (a in B and a!=B[i]):
    diff_cnt += 1

print(same_cnt)
print(diff_cnt)

## python3 ./folder/answer.py < ./folder/input.txt
## cp -r sample folder