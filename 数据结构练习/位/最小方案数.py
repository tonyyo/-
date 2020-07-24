def minMethods(x):
    ans = 1
    for i in range(32):
        if x & (1 << i) != 0: # x该位为1, a、b相同，00或者11
           ans *= 2
    print(ans)

x = int(input().strip())
minMethods(x)