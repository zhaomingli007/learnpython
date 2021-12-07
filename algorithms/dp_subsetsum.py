# Recursive
def isSubsetSum(arr, n, sum):
    if sum == 0:
        return True
    if n == 0:
        return False
    if arr[n-1] > sum:
        return isSubsetSum(arr, n-1, sum)
    return isSubsetSum(arr, n-1, sum) or isSubsetSum(arr, n-1, sum-arr[n-1])


arr = [3, 34, 4, 12, 5, 2]
sum = 30
n = len(arr)
# print(isSubsetSum(arr, n, sum))

# DP 
def isSubsetSumDP(input, n, sum):
    #Initialization
    subset = ([[False for i in range(sum+1)]
               for i in range(n+1)])
    #If sum is 0
    for i in range(n+1):
        subset[i][0] = True
    #if input is empty and sum is not 0
    for j in range(1, sum+1):
        subset[0][j] = False
    #if j < input[i]:
    #   dp[i][j] = dp[i-1][j]
    # else
    #   dp[i][j] = dp[i-1][j] or dp[i-1][j-input[i]]
    for i in range(1, n+1):
        for j in range(1, sum+1):
            if j < input[i-1]:
                subset[i][j] = subset[i-1][j]
            else :
                subset[i][j] = subset[i-1][j] or subset[i-1][j-input[i-1]]
    
    return subset[n][sum]


input = [3, 34, 4, 12, 5, 2]
n = len(input)
print(isSubsetSumDP(input,n, 9))
