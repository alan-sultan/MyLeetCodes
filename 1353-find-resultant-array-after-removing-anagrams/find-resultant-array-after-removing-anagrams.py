class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = [words[0]]
        # for i in range(1, len(words)):
        #     a, b = sorted(ans[-1]), sorted(words[i])
        #     if a != b:
        #         ans.append(words[i])
        # return ans
        freq = [Counter(w) for w in words]
        for i in range(1, len(words)):
            if freq[i] != freq[i-1]:
                ans.append(words[i])
        return ans