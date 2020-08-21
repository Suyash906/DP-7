class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp  = [[False for col in range(len(p)+1)] for row in range(len(s)+1)]
        
        dp[0][0] = True
        
        for i in range(1, len(p)+1):
            if p[i-1] == '*':
                dp[0][i] = dp[0][i-2]
                
                
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] != '*':
                    if p[j-1] == '.' or s[i-1] == p[j-1]:
                        dp[i][j] = dp[i-1][j-1]
                else:
                    # case 0
                    dp[i][j] = dp[i][j-2]
                    
                    # case 1
                    # check if preceding character in p matches current char in s
                    if p[j-2] == s[i-1] or p[j-2] == '.':
                        if dp[i-1][j]:
                            dp[i][j] = True
                        
        return dp[len(s)][len(p)]