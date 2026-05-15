class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        size_nums = len(nums)

        mid = size_nums // 2

        print(mid)

        if target == nums[mid]:
            return mid

        if target > nums[mid]:
            
            while mid < size_nums:

                if nums[mid] == target:
                    return mid
                mid += 1

        mid = size_nums // 2

        if target < nums[mid]:

            while mid > -1:

                if nums[mid] == target:
                    return mid
                mid -= 1

        return -1