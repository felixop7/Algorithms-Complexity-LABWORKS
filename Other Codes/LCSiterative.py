def lcs(s1, s2):
    m, n = len(s1), len(s2)
    
    # Create a 2D table to store the lengths of the LCS
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Create a 2D table to store the actual LCS
    lcs_table = [[""] * (n + 1) for _ in range(m + 1)]
    
    # Fill the tables using the iterative approach
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                lcs_table[i][j] = lcs_table[i - 1][j - 1] + s1[i - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                if dp[i - 1][j] > dp[i][j - 1]:
                    lcs_table[i][j] = lcs_table[i - 1][j]
                else:
                    lcs_table[i][j] = lcs_table[i][j - 1]
    
    return dp[m][n], lcs_table[m][n]

# Example usage
s1 = "ABCBDAB"
s2 = "BDCABA"
length, lcs_string = lcs(s1, s2)
print("Length of the Longest Common Subsequence:", length)
print("Longest Common Subsequence:", lcs_string)
