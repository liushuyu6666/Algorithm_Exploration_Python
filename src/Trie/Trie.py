from typing import Optional

from src.Trie.TrieNode import TrieNode


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_word(self, word: str) -> None:
        curr: TrieNode = self.root

        for c in word:
            pos = ord(c) - ord('a')

            if not curr.child_node[pos]:
                curr.child_node[pos] = TrieNode()

            curr = curr.child_node[pos]

        curr.occurrence += 1

    def search(self, word: str) -> int:
        return self.search_dfs(self.root, word, 0)

    def search_dfs(self, curr: Optional[TrieNode], word: str, word_index: int) -> int:
        if not curr:
            return -1
        if word_index == len(word):
            return curr.occurrence if curr.occurrence > 0 else -1

        char = word[word_index]
        return self.search_dfs(curr.child_node[ord(char) - ord('a')], word, word_index + 1)



