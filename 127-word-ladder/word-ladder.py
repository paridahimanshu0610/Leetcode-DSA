from collections import deque

class Solution:
    def isUnitApart(self, s1, s2):
        i, j, cnt = 0, 0, 0

        while i < len(s1) and j < len(s2):
            if s1[i] != s2[j]:
                cnt +=1
            if cnt > 1:
                return False
            i += 1
            j += 1

        return (cnt == 1)

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 0

        q = deque()
        n = len(wordList)

        wordSet = set(wordList)

        for char_idx in range(len(beginWord)):
            for i in range(26):
                if chr(97+i) == beginWord[char_idx]:
                    continue

                temp_word = beginWord[0:char_idx] + chr(97+i) + beginWord[char_idx+1:]

                if (temp_word in wordSet):
                    q.appendleft((temp_word, 1))
                    wordSet.remove(temp_word)
        
        if len(q) == 0:
            return 0
        
        while len(q)!=0:
            currWord, steps = q.pop()

            if currWord == endWord:
                return steps+1

            for char_idx in range(len(currWord)):
                for i in range(26):
                    if chr(97+i) == currWord[char_idx]:
                        continue

                    temp_word = currWord[0:char_idx] + chr(97+i) + currWord[char_idx+1:]

                    if (temp_word in wordSet):
                        q.appendleft((temp_word, steps+1))
                        wordSet.remove(temp_word)

        return 0