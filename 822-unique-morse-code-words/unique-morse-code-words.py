class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        imc = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ans = set()
        for word in words:
            an = ""
            for ch in word:
                an += imc[ord(ch) - 97]
            ans.add(an)
        return(len(ans))
