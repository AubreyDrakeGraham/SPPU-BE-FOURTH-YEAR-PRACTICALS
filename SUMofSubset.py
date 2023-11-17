def isSubsetSumBacktracking(arr, n, target, subset=[]):
    if target == 0:
        print("Subset with the given sum exists:", subset)
        return True
    if n == 0 or target < 0:
        return False

    # Include the last element and recur
    include = isSubsetSumBacktracking(arr, n - 1, target - arr[n - 1], subset + [arr[n - 1]])

    # Exclude the last element and recur
    exclude = isSubsetSumBacktracking(arr, n - 1, target, subset)

    return include or exclude

arr = [3, 34, 4, 12, 5, 2]
target = 9
n = len(arr)
if not isSubsetSumBacktracking(arr, n, target):
    print("No subset with the given sum exists.")




def isSubsetSumDP(arr, n, target):
    dp = [[False] * (target + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][target]

arr = [3, 34, 4, 12, 5, 2]
target = 9
n = len(arr)
if isSubsetSumDP(arr, n, target):
    print("Subset with the given sum exists.")
else:
    print("No subset with the given sum exists.")

