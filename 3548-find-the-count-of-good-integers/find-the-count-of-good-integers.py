class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        if n == 1:
            tot = 0
            for i in range(1, 10):
                if i % k == 0:
                    tot += 1
            return tot

        ft = [1]
        for i in range(1, n + 1):
            ft.append(ft[-1] * i)
        
        seen = set()
        ans = 0
        for left in range(10 ** ((n - 1) // 2), 10 ** ((n + 1) //2)):
            l = str(left)
            r = l[::-1]
            if n % 2 == 1:
                r = r[1:]
            t = l + r
           
            if int(t) % k != 0:
                continue

            s = "".join(sorted(list(t)))
            if s in seen:
                continue
            seen.add(s)
            count = Counter(t)

            tot = ft[n]
            for key in count.keys():
                tot //= ft[count[key]]

            ans += tot
            if count["0"] >= 1:
                totnzero = ft[n - 1]
                count["0"] -= 1
                for key in count.keys():
                    totnzero //= ft[count[key]]
                ans -= totnzero
        return ans