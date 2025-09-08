class Solution:
    def addBinary(self, a: str, b: str) -> str:
        output = ""
        carry = 0
        rev_a, rev_b = a[::-1], b[::-1]
        i = 0
        while carry or i < len(a) or i < len(b):
            if i < len(a):
                carry += int(rev_a[i])
            if i < len(b):
                carry += int(rev_b[i])
            
            output = str(carry % 2) + output
            carry = carry // 2
            i += 1
    
        return output
