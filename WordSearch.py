class Solution(object):
    def exist(self, board, word):
        rows = len(board)
        cols = len(board[0])

        def dfs(row, col, index):
            # Check out of bounds or mismatch
            inBounds = (0 <= row < rows and 0 <= col < cols)
            if not inBounds or board[row][col] != word[index]:
                return False

            # If we've reached the end of the word, return True
            if index == len(word) - 1:
                return True

            # Temporarily mark the cell as visited
            temp = board[row][col]
            board[row][col] = "#"

            # Explore all four directions
            found = (
                dfs(row + 1, col, index + 1) or
                dfs(row - 1, col, index + 1) or
                dfs(row, col + 1, index + 1) or
                dfs(row, col - 1, index + 1)
            )

            # Restore the cell's original value
            board[row][col] = temp

            return found

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:  # Start search from cells that match the first letter
                    if dfs(i, j, 0):
                        return True

        return False
