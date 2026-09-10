class Solution:
    def reverse(self, x: int) -> int:
        # Define the 32-bit signed integer limits
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Track the sign of the integer and work with the absolute value
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        reversed_num = 0
        while x > 0:
            # Extract the last digit
            digit = x % 10
            # Remove the last digit from x
            x //= 10
            
            # Build the reversed number
            reversed_num = (reversed_num * 10) + digit
            
        # Apply the original sign
        result = sign * reversed_num
        
        # Check if the result overflows 32-bit integer boundaries
        if result < INT_MIN or result > INT_MAX:
            return 0
            
        return result
