class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for letters,lettert in zip("".join(sorted(s)),"".join(sorted(t))):
            if letters != lettert:
                return False
        return True
        
        