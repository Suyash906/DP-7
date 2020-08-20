class Solution:
    def minDistanceUtil(self, word1: str, word2: str, l1: int, l2 :int) -> int:
        if 0 == l1:
            return l2
        if 0 == l2:
            return l1
        
        if word1[l1-1] == word2[l2-1]:
            return self.minDistanceUtil(word1, word2, l1-1, l2-1)
        else:
            return 1 + min(self.minDistanceUtil(word1, word2, l1, l2-1), 
                          self.minDistanceUtil(word1, word2, l1-1, l2),
                          self.minDistanceUtil(word1, word2, l1-1, l2-1))
        
    def minDistance(self, word1: str, word2: str) -> int:
        return self.minDistanceUtil(word1, word2, len(word1), len(word2))