class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        bottom=SortedSet()
        top=SortedSet()
        curr=0
        dic=defaultdict(int)
        ans=[]

        def update(ele,add):
            nonlocal curr

            if dic[ele]>0:
                if (dic[ele],ele) in bottom: bottom.remove((dic[ele],ele))
                else:
                    top.remove((dic[ele],ele))
                    curr-=dic[ele]*ele
            
            dic[ele]+=1 if add else -1
            if dic[ele]>0: bottom.add((dic[ele],ele))

        for i in range(len(nums)):
            update(nums[i],True)
            if i>=k: update(nums[i-k],False)

            while bottom and len(top)<x:
                cnt,ele=bottom.pop()
                curr+=ele*cnt
                top.add((cnt,ele))

            while bottom and bottom[-1]>top[0]:
                cntb,b=bottom.pop()
                cntt,t=top.pop(0)
                curr+=cntb*b
                curr-=cntt*t
                bottom.add((cntt,t))
                top.add((cntb,b))
            
            if i-k+1>=0: ans.append(curr)
        
        return ans