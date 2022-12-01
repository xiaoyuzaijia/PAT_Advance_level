S = input()
N = len(S)
dp = [[False for _ in range(N)] for _ in range(N)]    # dp[i:j]表示S[i:j+1]是否为回文串

if __name__ == "__main__":
    for j in range(N):
        i = 0
        while j <= N-1:
            if j - i < 2:
                    dp[i][j] = S[i] == S[j]
            else:
                if dp[i+1][j-1]:
                    dp[i][j] = S[i] == S[j]
            i += 1
            j += 1
    
    max_l = 0
    for i in range(N):
        for j in range(i, N):
            if dp[i][j] and max_l < j - i + 1:
                max_l = j - i + 1
    
    print(max_l)


'''
多提交几次才AC,比较极限
'''