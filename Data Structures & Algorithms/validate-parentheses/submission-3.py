class Solution:
    def isValid(self, s: str) -> bool:
        
        opens = []

        for char in s:

            if char not in ["]",")","}"]:

                opens.append(char)

            else:
                if not opens:
                    return False
                if char == "]" and opens[-1] == "[":
                    opens.pop(-1)
                    continue
                if char == "}" and opens[-1] == "{":
                    opens.pop(-1)
                    continue
                if char == ")" and opens[-1] == "(":
                    opens.pop(-1)
                    continue
                else:
                    return False
        
        print(opens)

        if not opens:
            return True
        else:
            return False

