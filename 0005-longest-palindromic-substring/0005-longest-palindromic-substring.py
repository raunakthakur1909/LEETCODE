class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 1:
            return ""
        
        start, end = 0, 0
        
        def expand_around_center(left: int, right: int) -> int:
            # Expand outwards as long as characters match and pointers are in bounds
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the length of the palindrome found
            return right - left - 1

        for i in range(len(s)):
            # Case 1: Odd-length palindromes (e.g., "aba", center is 'b')
            len1 = expand_around_center(i, i)
            
            # Case 2: Even-length palindromes (e.g., "abba", center is between 'b' and 'b')
            len2 = expand_around_center(i, i + 1)
            
            # Find the longer of the two expansions
            max_len = max(len1, len2)
            
            # Update the boundaries of the longest palindrome found so far
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
                
        return s[start : end + 1]

