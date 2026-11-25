class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        # idea: graph where pattern is the key
        # values are the strings that fit the pattern
        graph = defaultdict(list)
        for word in wordList:
            for c in range(len(word)):
                pattern = word[0:c] + '*' + word[c+1:len(word)]
                graph[pattern].append(word)
        
        # bfs
        q = deque()
        q.append(beginWord)
        visited = set()
        output = 1
        while q:
            for _ in range(len(q)):
                candidate = q.popleft()
                if candidate == endWord:
                    return output
                for c in range(len(candidate)):
                    pattern = candidate[0:c] + '*' + candidate[c+1:len(word)]
                    for adj_word in graph[pattern]:
                        if adj_word not in visited:
                            visited.add(adj_word)
                            q.append(adj_word)
            output += 1
        return 0


