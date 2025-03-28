class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        ch = set()
        for path, _ in paths:
            ch.add(path)
        for _, path in paths:
            if path not in ch:
                return path
    

