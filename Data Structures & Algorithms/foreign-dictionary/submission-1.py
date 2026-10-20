class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #Build adj list
        adj = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            mLen = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:mLen] == w2[:mLen]:
                return ""
            
            for j in range(mLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        # DFS
        visit = {}
        res = ""

        def dfs(c):
            nonlocal res
            if c in visit:
                return visit[c]
            visit[c] = True
            for n in adj[c]:
                if dfs(n):
                    return True
            visit[c] = False
            res = res + c
        for c in adj:
            if dfs(c):
                return ""
        return res[::-1]