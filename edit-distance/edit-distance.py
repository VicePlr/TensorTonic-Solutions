def edit_distance(s1, s2):
    """
    Compute the minimum edit distance between two strings.
    """
    # Write code here
    dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    for j in range(len(s2)+1):
        dp[0][j] = j
    for i in range(len(s1)+1):
        dp[i][0] = i
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    for row in dp:
        print(row)
    return dp[-1][-1]