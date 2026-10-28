class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []

        def dfs(start):
            while start < len(nums):
                # add to path
                path.append(nums[start])
                
                # check if its less than target(this only works bc search space is positive integers)
                if sum(path) < target:
                    # explore deeper
                    dfs(start)
                elif sum(path) == target:
                    # this is a solution
                    result.append(path.copy())

                # pop the last
                path.pop()
                # this branch is done, we can iterate the candidate
                start += 1
        
        dfs(0)
        return result