class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # Step 1: Build Trie
        root = TrieNode()

        for word in words:
            node = root

            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

            node.word = word


        ROWS = len(board)
        COLS = len(board[0])

        res = []

        # Step 2: DFS + Trie traversal
        def dfs(row, col, node):

            # invalid board position
            if (
                row < 0
                or col < 0
                or row >= ROWS
                or col >= COLS
            ):
                return

            ch = board[row][col]

            # visited cell
            if ch == "#":
                return

            # current character is not a valid Trie continuation
            if ch not in node.children:
                return

            # move to next Trie node
            next_node = node.children[ch]

            # complete word found
            if next_node.word is not None:
                res.append(next_node.word)

                # prevents duplicate result
                next_node.word = None

            # mark current board cell visited
            board[row][col] = "#"

            # explore four directions
            dfs(row + 1, col, next_node)
            dfs(row - 1, col, next_node)
            dfs(row, col + 1, next_node)
            dfs(row, col - 1, next_node)

            # backtrack
            board[row][col] = ch


        # Step 3: Try every board cell as starting point
        for row in range(ROWS):
            for col in range(COLS):
                dfs(row, col, root)

        return res
# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # ROWS = len(board)
        # COLS = len(board[0])
        # res = []
        
        # def wordmatch(row, col, i, word):

        #     if i == len(word):
        #         return True
        #     # non ideal condition 
        #     if row < 0 or col < 0 or row >= ROWS or col >= COLS or board[row][col] != word[i]:
        #         return False

        #     temp = board[row][col]
        #     board[row][col] = "#"

        #      # if condition met then we need to search in all direction
        #     found = wordmatch(row, col+1, i+1, word) or wordmatch(row, col-1, i + 1, word) or wordmatch(row+1, col, i+1, word) or wordmatch(row-1, col, i+1,word)
        #     board[row][col] = temp

        #     return found

        # # try every cell as a starting point
        # for word in words:
        #     found = False
        #     for row in range(ROWS):
        #         for col in range(COLS):
        #             if wordmatch(row, col, 0, word):
        #                 res.append(word)
        #                 found = True
        #                 break
        # return res





        