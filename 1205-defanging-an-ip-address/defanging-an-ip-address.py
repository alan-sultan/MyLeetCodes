class Solution:
    def defangIPaddr(self, address: str) -> str:
        return "".join("[.]" if x == '.' else x for x in address)