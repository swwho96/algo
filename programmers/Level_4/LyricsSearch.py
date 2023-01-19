class Node():
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.len = []
        self.child = {}

class Trie():
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        cur_node = self.head
        n = len(string)
        cur_node.len.append(n)
        for char in string:
            if char not in cur_node.child:
                cur_node.child[char] = Node(char)
            cur_node = cur_node.child[char]
            cur_node.len.append(n)
        cur_node.len.append(n)
        cur_node.data = string

    def search(self, string, n):
        cur_node = self.head
        if string == '':
            return cur_node.len.count(n)
        for char in string:
            if char not in cur_node.child:
                return False
            cur_node = cur_node.child[char]
        if cur_node.data or n in cur_node.len:
            return cur_node.len.count(n)
        return False


def solution(words, queries):
    t = Trie()
    t_reversed = Trie()
    answer = []
    for w in words:
        t.insert(w)
        t_reversed.insert(w[::-1])
    for q in queries:
        q_replaced = q.replace('?', '')
        if q_replaced == '':
            answer.append(t.search(q_replaced, len(q)))
            continue
        elif q[0] == '?':
            tmp = t_reversed.search(q_replaced[::-1], len(q))
        elif q[-1] == '?':
            tmp = t.search(q_replaced, len(q))
        if tmp > 0:
            answer.append(tmp)
        else:
            answer.append(0)
    return answer