class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = {}
        length = 0
        has_odd = False

        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        max_odd = 0
        for count in char_count.values():     
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                has_odd = True
        if has_odd:
            length += 1


        return length
        
        