class Solution:
    def findMin(self, nums: List[int]) -> int:
        # think about this as two sub arrays left and right
        # the elements in the elft array will always be bigger than the right
        # this is the product of being ascending order and sorted and then rotated
        # we are trying to see which section middle is in (left or right)
        # since we're looking for the minimum if its in section left we can elimate all elements on the left of it


        l, r = 0, len(nums) - 1


        while l <= r:
            mid = (l + r) // 2

            if nums[mid] >= nums[r]:
                # we know mid is on the left array
                # the minimum will not be before mid
                l = mid + 1
            else:
                r = mid
        return nums[mid]
        