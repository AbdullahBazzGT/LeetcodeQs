class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Store the complete word when a path completes.

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # Step 1: Build a Trie from the words list.
        root = self.buildTrie(words)
        foundWords = set()
        rows, cols = len(board), len(board[0])

        def dfs(row, col, node):
            # Check bounds and visited status
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] == '#':
                return
            
            char = board[row][col]
            if char not in node.children:
                return
            
            nextNode = node.children[char]
            if nextNode.word:  # Found a valid word
                foundWords.add(nextNode.word)  # Add to result set
                nextNode.word = None  # Avoid duplicates
            
            # Mark the cell as visited
            board[row][col] = '#'
            # Explore all four directions
            dfs(row + 1, col, nextNode)
            dfs(row - 1, col, nextNode)
            dfs(row, col + 1, nextNode)
            dfs(row, col - 1, nextNode)
            # Restore the cell
            board[row][col] = char

        # Step 2: Perform DFS from every cell in the board
        for i in range(rows):
            for j in range(cols):
                if board[i][j] in root.children:
                    dfs(i, j, root)
        
        return list(foundWords)

    def buildTrie(self, words):
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word  # Mark the end of a word.
        return root
