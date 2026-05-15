class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        
        print(s)

        i = 0
        j = len(s)-1

        if not s:
            return True

        while i != j:

            if s[i] != s[j]:
                return False
            if j == i + 1:
                return True
            i += 1
            j -= 1

        return True