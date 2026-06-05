class Trie:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        
class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:        
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = Trie()
            cur = cur.children[char]

        cur.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                char = word[i]
                if char == ".":
                    for entry in cur.children.values():
                        if dfs(i + 1, entry):
                            return True

                    return False

                elif char in cur.children:
                    cur = cur.children[char]

                else:
                    return False
            return cur.endOfWord

        return dfs(0, self.root)
