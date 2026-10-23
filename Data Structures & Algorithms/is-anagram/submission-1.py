class Solution:
    def isAnagram(self, a: str, b: str) -> bool:
        if len(a) != len(b):     

            return False

        count = {}
        for ch in a:
            count[ch] = count.get(ch, 0) + 1

        for ch in b:
            if count.get(ch, 0) == 0:  
                return False
            count[ch] -= 1

        return True