class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            name, domain = s.split('@')
            ans = name[0].lower() + "*" * 5 + name[-1].lower() + '@'
            bdot, adot = domain.split('.')
            ans += bdot.lower() +'.' + adot.lower() 
            return ans
        nums =""
        for num in s:
            if num.isalnum():
                nums += num
        print
        if len(nums) == 10:
            return "***-***-" + nums[len(nums) - 4:]
        if len(nums) == 11:
            return "+*-***-***-" + nums[len(nums) - 4:]
        if len(nums) == 12:
            return "+**-***-***-" + nums[len(nums) - 4:]
        if len(nums) == 13:
            return "+***-***-***-" + nums[len(nums) - 4:]
