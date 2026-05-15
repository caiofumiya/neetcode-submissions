class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        Lo , Ro = 0 , len(matrix) - 1

        Io = -1

        while Lo <= Ro:

            print(Lo,Ro)
            m = ( Lo+Ro ) // 2

            if matrix[m][0] <= target <= matrix[m][-1]:
                Io = m
                break

            if matrix[m][-1] < target :
                Lo = m + 1

            elif matrix[m][0] > target:
                Ro = m - 1
        
        print(Io)

        if Io == -1:
            return False
        
        Li , Ri = 0 , len(matrix[Io]) - 1

        while Li <= Ri:

            m = (Li+Ri) // 2

            if matrix[Io][m] > target:
                Ri = m - 1
            if matrix[Io][m] < target:
                Li = m + 1
            elif matrix[Io][m] == target:
                return True

        return False
            