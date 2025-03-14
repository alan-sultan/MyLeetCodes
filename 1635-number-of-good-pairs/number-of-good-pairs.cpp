class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        unordered_map<int, int> counter;
        int ans = 0;
        for(int num : nums){
            ans += counter[num] ++;
        }
        return ans;
    }
};