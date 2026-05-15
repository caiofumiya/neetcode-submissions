class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        num_size = len(numbers)

        i = 0

        while i < num_size:
            
            complement = target - numbers[i]

            if complement in numbers and complement != numbers[i] :

                return [i + 1, numbers.index(complement) + 1]

            i += 1


