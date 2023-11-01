arr = [1,2,3]
print(*arr) ## 1 2 3

N = 255
print(f"{N:02X}") ## 2桁の16進数 (大文字)

## bit OR  ABC270_A
A = 5  # 二進数で 0101
B = 3  # 二進数で 0011
print(A | B)  # 二進数で 0111、10進数で 7

n,x,y,z = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
abi = [[a[i],b[i],i+1] for i in range(n)]
abi.sort(key=lambda ABI:(-ABI[0],ABI[2]))