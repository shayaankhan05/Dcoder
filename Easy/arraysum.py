N = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(sum(arr) % arr[-1])
