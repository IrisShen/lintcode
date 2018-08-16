class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # write your code here
        len_pal = 0
        counts = dict()

        # count the occurence of each letter using dict
        for i in s:
            counts[i] = counts.get(i, 0) + 1

        # count total even occurence 
        for value in counts.values():
            len_pal += value//2*2

        # add middle element if available
        if len_pal < len(s):
            len_pal += 1

        return len_pal