class Solution {
public:
    vector<int> getSneakyNumbers(vector<int>& nums) {
        unordered_map<int, int> counter;
        vector<int> ans;
        for(int num : nums){
            counter[num] ++;
            if(counter[num] == 2){
                ans.push_back(num);
            }
        }
        return ans;
    }
};