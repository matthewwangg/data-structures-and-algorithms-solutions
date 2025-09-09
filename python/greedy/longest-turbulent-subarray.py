class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        max_length, length = 1, 1
        previous, first = 0, True
        for k in range(len(arr)-1):
            if arr[k] == arr[k+1]:
                first = True
                length = 1
                continue

            if first or ((arr[k] > arr[k+1]) != previous):
                length += 1
                first = False
            else:
                length = 2
            
            previous = arr[k] > arr[k+1]
        
            max_length = max(max_length, length)
        
        return max_length
