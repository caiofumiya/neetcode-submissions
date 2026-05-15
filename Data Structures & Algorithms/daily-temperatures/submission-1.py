class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0]*len(temperatures)

        for i in range(len(temperatures)):

            temp = 0
            
            j = i + 1

            while j < len(temperatures):

                if temperatures[j] <= temperatures[i]:

                    temp += 1

                if temperatures[j] > temperatures[i]:
                    
                    temp += 1
                    res[i] = temp
                    break
                
                j += 1
        return res   