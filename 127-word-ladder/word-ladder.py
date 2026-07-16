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

        visited = [0]*n

        for i in range(n):
            if self.isUnitApart(beginWord, wordList[i]):
                q.appendleft((wordList[i], 1))
                visited[i] = 1
        
        if len(q) == 0:
            return 0

        while len(q)!=0:
            currWord, steps = q.pop()

            if currWord == endWord:
                return steps+1

            for i in range(n):
                if (not visited[i]) and self.isUnitApart(currWord, wordList[i]):
                    q.appendleft((wordList[i], steps+1))
                    visited[i] = 1

        return 0