import sys
modulo = 301907
def bracket_sequences(pattern):
    n = len(pattern)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(n + 1):
            if dp[i][j] > 0:
                if pattern[i] in "(?":
                    dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j]) % modulo
                if pattern[i] in ")?":
                    if j > 0:
                        dp[i + 1][j - 1] = (dp[i + 1][j - 1] + dp[i][j]) % modulo
    return dp[n][0]
if __name__ == "__main__":
    pattern = sys.stdin.readline().strip()
    print(bracket_sequences(pattern))
