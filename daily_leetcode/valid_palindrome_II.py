from audioop import reverse


class Solution:
    def validPalindrome(s: str):
        '''
        Given a string s, return true if the s can be palindrome after deleting at most one character from it.

        Example 1:
        Input: s = "aba"
        Output: true

        Example 2:
        Input: s = "abca"
        Output: true
        Explanation: You could delete the character 'c'.

        Example 3:
        Input: s = "abc"
        Output: false

        Constraints:
        1 <= s.length <= 105
        s consists of lowercase English letters.
        '''

        # TODO my own try 
        # I belive it work BUT the leet code is saying time limit exceeded :<
        for i, char in enumerate(s): # O(n)
            deleted = s[:i] + s[i+1:]
            # reverse_list = [deleted[j] for j in reversed(range(len(deleted)))] # TODO reverse string found a faster way
            if deleted == deleted[::-1]:
                return True
        return False


print(Solution.validPalindrome(
    "abca"))
