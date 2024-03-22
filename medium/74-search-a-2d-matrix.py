from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m_start = 0
        m_end = len(matrix) - 1
        m_mid = (m_start + m_end) // 2

        while m_start <= m_end:
            if matrix[m_mid][0] > target:
                m_end = m_mid - 1
            elif matrix[m_mid][0] < target:
                m_start = m_mid + 1
            else:
                break

            m_mid = (m_start + m_end) // 2

        space = matrix[m_mid]

        start = 0
        end = len(space) - 1
        mid = (start + end) // 2

        while start <= end:
            if space[mid] > target:
                end = mid - 1
            elif space[mid] < target:
                start = mid + 1
            else:
                break

            mid = (start + end) // 2

        return space[mid] == target


s = Solution()

print(s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 23))
