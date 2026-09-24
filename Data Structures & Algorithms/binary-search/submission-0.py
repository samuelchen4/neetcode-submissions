class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            # calculate middle
            mid = (l + r) // 2
            # target
            if nums[mid] == target:
                return mid
            # less than
            elif nums[mid] < target:
                # move left pointer to mid + 1
                l = mid + 1
            # greater than
            else:
                r = mid - 1
        return -1
        