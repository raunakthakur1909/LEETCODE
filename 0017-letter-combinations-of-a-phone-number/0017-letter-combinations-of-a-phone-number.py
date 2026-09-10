class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
            
        digit_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        result = []
        
        def backtrack(index: int, current_combination: list[str]):
            if len(current_combination) == len(digits):
                result.append("".join(current_combination))
                return
                
            current_digit = digits[index]
            letters = digit_map[current_digit]
            
            for letter in letters:
                current_combination.append(letter)
                backtrack(index + 1, current_combination)
                current_combination.pop()
                
        backtrack(0, [])
        return result
