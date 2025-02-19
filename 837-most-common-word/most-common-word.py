class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        count = sorted(Counter(map( lambda x : x.lower(), re.split(r"[ \!\?'\.,;]+", paragraph))).items(), key = lambda x : x[1], reverse = True)
        for key, val in count:
            if key not in banned and key != '':
                return key