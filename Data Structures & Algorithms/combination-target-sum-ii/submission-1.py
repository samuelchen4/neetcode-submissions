class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        result = []
        path = []

        # once we have a solution, we add the start index and add it to set, if the next candidate starts with set then skip
        # we dont even need a set it can just the value that had a result

        def dfs(start, current_sum):
            prev = 0
            while start < len(candidates):
                if candidates[start] == prev:
                    start += 1
                    continue

                path.append(candidates[start])
                new_sum = current_sum + candidates[start]

                if new_sum < target:
                    # explore this branch but with unique elements
                    dfs(start + 1, new_sum)
                elif new_sum == target:
                    # we have a solution
                    result.append(path.copy())
            
                path.pop()
                prev = candidates[start]
                start += 1

        dfs(0,0)
        return result








