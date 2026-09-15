class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # build a graph with all letter as nodes
        graph = {c: set() for word in words for c in word}

        # building a adjency list directed graph
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]: # Invalid as words are already sorted and if len of w1 is greater the word2 then it is invalid and we need to return empty string
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    graph[w1[j]].add(w2[j])
                    break
        state = {}
        result = []

        def dfs(node):

            if node in state:
                if state[node] == 1:
                    return False
                if state[node] == 2:
                    return True

            state[node] = 1

            for nei in graph[node]:
                if not dfs(nei):
                    return False

            state[node] = 2
            result.append(node)

            return True

        for node in graph:
            if node not in state:
                if not dfs(node):
                    return ""

        result.reverse()

        return "".join(result)