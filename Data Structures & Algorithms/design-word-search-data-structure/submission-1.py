class TreeNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()
        
    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TreeNode()

            cur = cur.children[c]

        cur.end = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word): return node.end

            c = word[i]

            if c != ".":
                if c in node.children:
                    return dfs(node.children[c], i+1)
                return False
            else:
                for child in node.children:
                    return dfs(node.children[child], i+1)
                return False

        return dfs(self.root, 0)