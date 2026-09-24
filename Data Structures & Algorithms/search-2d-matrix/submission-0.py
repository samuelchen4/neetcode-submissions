class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix or not matrix[0]:
            return false
        
        # two coorinates for each pointer 
        # col is technically the x coordinate and row is the y (col, row)
        col_nums = len(matrix[0])
        l_col, l_row = 0, 0
        r_col, r_row = col_nums - 1, len(matrix) - 1

        # need a way to get an absolute index
        # flatten into a single index

        def abs_index(col, row) -> int:
            return col_nums * row + col

        abs_l = abs_index(l_col, l_row)
        abs_r = abs_index(r_col, r_row)

        while abs_l <= abs_r:
            # calculate middle
            mid = (abs_l + abs_r) // 2
            
            # revert back to 2d coordinates
            col = mid % col_nums
            row = mid // col_nums
            
            # target == abs_index
            if target == matrix[row][col]:
                return True

            elif target < matrix[row][col]:
                # move right pointers to mid - 1
                abs_r = mid - 1
            else:
                # move left pointers to mid + 1
                abs_l = mid + 1
        return False
