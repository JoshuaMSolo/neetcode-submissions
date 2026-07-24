class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right :
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[right] == target :
                return right
            elif nums[left] == target :
                return left
            elif nums[left] < nums[mid] < nums[right] :
                if nums[mid] < target :
                    left = mid + 1
                else :
                    right = mid - 1
            elif nums[right] < nums[left] < nums[mid] :
                if nums[mid] < target or target <= nums[right]:
                    left = mid + 1
                else :
                    right = mid - 1
            else :
                if nums[mid] > target or target > nums[left]:
                    right = mid - 1
                else :
                    left = mid + 1
        return -1


