class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        replacement = {}
        for i, char in enumerate(order):
            replacement[char] = chr(i+97)
        
        for index, word in enumerate(words):
            new_word = ""
            for char in word:
                new_word += replacement[char]
            words[index] = new_word
            
            if index and words[index] < words[index-1]:
                return False
        
        return True
