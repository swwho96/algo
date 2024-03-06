from collections import defaultdict
import sys
input = sys.stdin.readline

class TrieNode():
    def __init__(self):
        self.child = defaultdict(TrieNode)
        self.is_end = False

class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            node = node.child[char]
        node.is_end = True
    
    def is_startwith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.child:
                return False
            node = node.child[char]
        return True

T = int(input())
for _ in range(T):
    n = int(input())
    consistency = True
    phone_numbers = []
    for _ in range(n):
        phone_numbers.append(input().rstrip())
    phone_numbers = sorted(phone_numbers, key=lambda x: len(x), reverse=True)
    trie = Trie()
    for number in phone_numbers:
        if trie.is_startwith(number) is True:
            consistency = False
            break
        trie.insert(number)
    print('YES' if consistency is True else 'NO')