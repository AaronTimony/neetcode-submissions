class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(j, cur):
            if j == len(word):        # explicit base case now
                return cur.word
            c = word[j]
            if c == ".":
                return any(dfs(j + 1, child) for child in cur.children.values())
            if c not in cur.children:
                return False
            return dfs(j + 1, cur.children[c])

        return dfs(0, self.root)
