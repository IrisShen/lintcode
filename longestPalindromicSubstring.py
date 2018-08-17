class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here
        n = len(s)
        left = 0
        right = 0
        long_P = 0
        is_Palindrome = [[False] * n for _ in range(n)]
        for i in range(n):
            is_Palindrome[i][i] = True
            is_Palindrome[i][i-1] = True
            for j in range(i):
                is_Palindrome[j][i] = ( s[j] == s[i] and is_Palindrome[j+1][i-1] )
                if is_Palindrome[j][i] and i - j + 1 > long_P:
                    long_P = i - j + 1
                    left = j
                    right = i
        
        return s[left:right+1]
                    