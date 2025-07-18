# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

class Solution:
    def romanToInt(self, s: str) -> int:
        # Approach 1: hashmap
        # char_to_int = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D': 500, 'M':1000}
        # total = 0
        # i = 0
        # while i < len(s):
        #     if i + 1 < len(s) and char_to_int[s[i+1]] > char_to_int[s[i]]:
        #         temp = char_to_int[s[i+1]] - char_to_int[s[i]]
        #         total += temp
        #         i += 2
        #     else:
        #         total += char_to_int[s[i]]
        #         i += 1
        # return total
    
        # Approach 2: Hardcode all possible numbers
        char_to_int = {
            'I':1, 
            'V':5, 
            'X':10, 
            'L':50, 
            'C':100, 
            'D': 500, 
            'M':1000,  
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,}
        
        total = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and s[i:i + 2] in char_to_int:
                total += char_to_int[s[i:i + 2]]
                i += 2
            else:
                total += char_to_int[s[i]]
                i += 1
        return total