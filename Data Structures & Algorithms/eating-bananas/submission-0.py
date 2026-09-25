class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # we are looking for the minimum rate for eating all piles in h hours
        # low and upper bounds for rate of eating
        l, r = 1, max(piles)
        result = r
        # binary search

        while l < r:
            rate = (l + r) // 2
            print(rate)

            # how many hours to eat all piles by the rate?
            hours = 0
            for pile in piles:
                
                hours += math.ceil(pile/rate)
            # if hours <= h we have a solution
            if hours <= h:
                # try to find a better one by moving right pointer, but include it bc its a solution
                r = rate
                result = rate
            else:
                l = rate + 1

            print(l)
            print(r)

        return result

            