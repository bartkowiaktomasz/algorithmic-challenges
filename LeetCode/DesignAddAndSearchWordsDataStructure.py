from typing import Dict


class TrieNode:
    def __init__(self, char: str):
        self.val = char
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode("")

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                child = TrieNode(c)
                cur.children[c] = child
            cur = cur.children[c]
        cur.isWord = True

    def search(self, word: str) -> bool:
        root = self.root
        def searchFrom(word: str, cur: TrieNode):                
            for i, c in enumerate(word):
                if c in cur.children: cur = cur.children[c]
                else:
                    if c == ".":
                        return any([searchFrom(word[i + 1:], child) for child in cur.children.values()])
                    else: return False
            return cur.isWord
        found = searchFrom(word, root)
        return found

wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
wordDictionary.search("pad")
wordDictionary.search("bad")
print(
    wordDictionary.search("ba.")
)
