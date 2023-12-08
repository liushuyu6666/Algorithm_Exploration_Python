import unittest

from src.Trie.Trie import Trie


class TestTrie(unittest.TestCase):

    def test_trie(self):
        words = ['apple', 'banana', 'orange', 'grape', 'kiwi', 'melon', 'peach', 'banana', 'pear', 'cherry']
        trie = Trie()

        for word in words:
            trie.insert_word(word)

        self.assertEqual(trie.search('banana'), 2)

        self.assertEqual(trie.search('eggs'), -1)

        self.assertEqual(trie.search('orange'), 1)




if __name__ == "__main__":
    unittest.main()
