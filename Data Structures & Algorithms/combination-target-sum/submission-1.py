class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []

        def dfs(start, cur_sum):
            while start < len(nums):
                # add to path
                path.append(nums[start])
                
                new_sum = cur_sum + nums[start]
                # check if its less than target(this only works bc search space is positive integers)
                if new_sum < target:
                    # explore deeper
                    dfs(start, new_sum)
                elif new_sum == target:
                    # this is a solution
                    result.append(path.copy())

                # pop the last
                path.pop()
                # this branch is done, we can iterate the candidate
                start += 1
        
        dfs(0, 0)
        return result

        # time: O(2^n * n * target)