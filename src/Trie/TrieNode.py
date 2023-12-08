from typing import List, Optional


class TrieNode:
    def __init__(self):
        self.child_node: List[Optional[TrieNode]] = [None] * 26
        self.occurrence: int = 0

