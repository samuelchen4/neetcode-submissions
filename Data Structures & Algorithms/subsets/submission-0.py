class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # since its unique paths, we can create an algo where
        # going deeper will never be on a previous element in the array
        result = []
        path = []

        def dfs(start):
            result.append(path.copy()) # we need to make a shallow copy since variable is just a pointer to the object

            # explore all future paths
            while start < len(nums):
                # append to path
                path.append(nums[start])

                # explore this path
                dfs(start + 1)

                # backtrack
                path.pop()

                # if it reaches here, the previous path has been fully explored, iterate start
                start += 1

        dfs(0)
        return result