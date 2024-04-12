class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        row = matrix[0]
        while l <= r:
            mid = (l + r) // 2
            row = matrix[mid]
            if target >= row[0] and target <= row[len(row) - 1]:
                break
            if target > row[len(row) - 1]:
                l = mid + 1
            else:
                r = mid - 1
        
        l, r = 0, len(row) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == row[mid]:
                return True
            if target < row[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return False
    
s = Solution()

print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))