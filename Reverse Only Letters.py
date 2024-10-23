class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = [char for char in s if char.isalpha()]
        letters.reverse()
        result = []
        j = 0
        for char in s:
            if char.isalpha():
                result.append(letters[j])
                j += 1
            else:
                result.append(char)
        return ''.join(result)