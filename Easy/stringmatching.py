t = int(input())
for i in range(t):
    s1, s2 = input().split()
    if s2 in s1:
        print("Yes")
    else:
        print("No")
