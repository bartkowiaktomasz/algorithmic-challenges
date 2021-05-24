from typing import Tuple


class TrieNode:
    def __init__(self, char: str):
        self.char = char
        self.children = dict()
        self.end = False

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode('')

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if not word:
            return None
        cur = self.root
        for char in word:
            if char in cur.children:
                cur = cur.children[char]
            else:
                node = TrieNode(char)
                cur.children[char] = node
                cur = node
        cur.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        is_prefix, end_node = self._startsWithVerbose(word)
        if is_prefix and end_node.end:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self._startsWithVerbose(prefix)[0]

    def delete(self, word: str):
        """
        Recursively remove a word from the Trie
        """
        is_prefix, end_node = self._startsWithVerbose(word)
        if not is_prefix:
            # Word does not exist in the Trie
            return
        else:
            if end_node.children: 
                # Word exists but a terminal node has children so we can't free
                #  any memory
                end_node.end = False
                return
        
        def _delete(word: str, node: TrieNode) -> bool:
            if not word:
                if not node.children:
                    del node
                    return True
                else:
                    node.end = False
                    return False
            char = word[0]
            child_deleted = _delete(word[1:], node.children[char])
            if child_deleted:
                del node.children[char]
                if not node.children:
                    del node
                    return True
                else:
                    return False
            return False
        _delete(word, self.root)     

    def _startsWithVerbose(self, prefix: str) -> Tuple[bool, TrieNode]:
        """
        Returns a tuple [bool, TrieNode], where:
        - bool indicates if there exists a word in a Trie that starts with a given prefix
        - TrieNode is a terminal node encountered
        """
        if not prefix:
            return False
        cur = self.root
        for char in prefix:
            if char in cur.children:
                cur = cur.children[char]
            else:
                return False, cur
        return True, cur


trie = Trie()
trie.insert("apple")
trie.search("apple")
trie.search("app")
trie.startsWith("app")
trie.insert("app")
trie.search("app")
trie.delete("app")
trie.delete("apple")