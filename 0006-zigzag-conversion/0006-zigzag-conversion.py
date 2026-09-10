class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: If only 1 row is needed or the string is too short, no change is made
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create an array of strings, one for each row
        rows = [""] * numRows
        current_row = 0
        going_down = False
        
        # Step through each character in the string
        for char in s:
            rows[current_row] += char
            
            # Change direction when hitting the top row or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
                
            # Move up or down based on the current direction flag
            current_row += 1 if going_down else -1
            
        # Combine all rows into a single string
        return "".join(rows)
