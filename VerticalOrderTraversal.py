from collections import deque
from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []

        columns = defaultdict(list) #If key not in dict, return empty list. This dict holds a bunch of lists. Every list is every node in a column.
        q = deque([(0, root)])
        res = []

        maxCoord = float('-inf')
        minCoord = float('inf')

        while q:
            coord, node = q.popleft()

            maxCoord = max(maxCoord, coord)
            minCoord = min(minCoord, coord)

            columns[coord].append(node.val) # Will return an empty list if key doesnt exist (defaultdict property). Otherwise returns the list associated with this column.

            if node.left:
                q.append((coord - 1, node.left))

            if node.right:
                q.append((coord + 1, node.right))

        
        for i in range(minCoord, maxCoord + 1):
            res.append(columns[i]) # columns[i] == columns.get(i) * Where i the key/column. The associated value with any key is an array.

        return res
            

