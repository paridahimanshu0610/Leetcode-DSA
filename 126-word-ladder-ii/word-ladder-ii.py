from collections import deque

class Solution:
    def dfs(self, curr_word, curr_path, word_map, res, beginWord):
        if curr_word == beginWord:
            res.append(curr_path[::-1])
            return
        
        for i in range(len(curr_word)):
            for ch_idx in range(26):
                char = chr(97+ch_idx)

                if char == curr_word[i]:
                    continue

                temp_word = curr_word[:i] + char + curr_word[i+1:]

                if temp_word in word_map and (word_map[curr_word] == word_map[temp_word]+1):
                    self.dfs(temp_word, curr_path + [temp_word], word_map, res, beginWord)

    def findLadders(self, beginWord: str, endWord: str, words: List[str]) -> List[List[str]]:
        word_set = set(words)
        q = deque()
        q.appendleft((beginWord, 0))
        word_set.discard(beginWord)

        word_map = {}
        found = False

        while len(q) != 0:
            curr_word, dist = q.pop()
            word_map[curr_word] = dist

            if curr_word == endWord:
                found = True
                break

            for i in range(len(curr_word)):
                for ch_idx in range(26):
                    char = chr(97+ch_idx)
                    if char == curr_word[i]:
                        continue

                    temp_word = curr_word[:i] + char + curr_word[i+1:]

                    if temp_word in word_set:
                        q.appendleft((temp_word, dist+1))
                        word_set.discard(temp_word)

        if not found:
            return []

        res = []
        
        self.dfs(endWord, [endWord], word_map, res, beginWord)

        return res