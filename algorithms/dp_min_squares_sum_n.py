from math import ceil, sqrt

def getMinSquares(n):
    dp = [0, 1, 2, 3]

    for i in range(4, n+1):
        # max value is i as can always be formed with 1*1 + 1*1 ...
        dp.append(i)

        # Walk through all smaller values
        for x in range(1, int(ceil(sqrt(i)))+1):
            t = x * x
            if t > i:
                break
            else:
                dp[i] = min(dp[i], 1+dp[i - t])
    return dp[n]

print(getMinSquares(6))