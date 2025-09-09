class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = { "M" : 1000, "D": 500, "CM": 900, "CD": 400, "C": 100, "L": 50, "XC": 90, "XL": 40, "X": 10, "V": 5, "IX": 9, "IV": 4, "I": 1}
        answer = 0
        i = 0
        while i < len(s):
            if s[i:i+2] in mapping:
                answer += mapping[s[i:i+2]]
                i += 1
            else:
                answer += mapping[s[i]]
        
            i += 1
        
        return answer
