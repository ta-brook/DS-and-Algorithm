from matplotlib.style import use


class Solution:
    def lengthOfLongestSubstring(s: str) -> int:
        '''
        Given a string s, find the length of the longest substring without repeating characters.

        Example 1:
        Input: s = "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with the length of 3.

        Example 2:
        Input: s = "bbbbb"
        Output: 1
        Explanation: The answer is "b", with the length of 1.

        Example 3:
        Input: s = "pwwkew"
        Output: 3

        Explanation: The answer is "wke", with the length of 3.
        Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

        Constraints:
        0 <= s.length <= 5 * 104
        s consists of English letters, digits, symbols and spaces.
        '''

        '''
        TODO sliding window & two pointer
        index: 0  *1*  2  3  4  *5*  6  7  8
        str:   a  *b*  c  d  e  *b*  l  k  a
               ^                 ^
               |                 |
              left              right
        map: {a:0, b:1, c:2, d:3, e:4}
        case: 1. map[b] = 1, current window  is s[0:5] and b is inside current window
                 map[b] = 1 > left = 0. Move left pointer to map[b] + 1 = 2

        index: *0*  1  2  3  4  5  6  7  *8*
        str:   *a*  b  c  d  e  b  l  k  *a*
                       ^                  ^
                       |                  |
                      left              right       
        case 2: map[a] = 0,which means a not in current window s[2:8]  
                since map[a] = 0 < left = 2, we can keep moving right pointer.       
        '''
        map = {}
        left = 0
        output = 0
        for right, char in enumerate(s):
            if char not in map.keys():
                output = max(output, right-left+1)
            else:
                if map[char] >= left:
                    left = map[char] + 1
                else:
                    output = max(output, right-left+1)
            map[char] = right
        return output



# s = ''
# s = "abcabcbb"
# s = "bbbbb"
# s = "pwwkew"
# s = "au"
# s = "dvdf"
s = "anviaj"
print(Solution.lengthOfLongestSubstring(s))

