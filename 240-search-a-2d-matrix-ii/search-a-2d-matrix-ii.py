class Solution:
    def searchMatrix(self, a: List[List[int]], x: int) -> bool:
        m, n = len(a), len(a[0])
        row, col = 0, n-1

        while row < m and col >= 0 :
            if a[row][col] == x:
                return True
            elif a[row][col] > x:
                col -= 1
            else:
                row += 1

        return False