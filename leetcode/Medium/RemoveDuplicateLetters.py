class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        s_count_list, seen, stack = collections.Counter(s), set(), []
        for char in s:
            s_count_list[char] -= 1
            if char in seen:
                continue
            while stack and char < stack[-1] and s_count_list[stack[-1]] > 0:
                seen.remove(stack.pop())
            
            stack.append(char)
            seen.add(char)
        return ''.join(stack)