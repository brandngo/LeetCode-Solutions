class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
      
      map<int, int> outputs;
      
      for (int i = 0; i < nums.size(); i++) {
        auto res = outputs.find(nums[i]);
        if (res != outputs.end()) {
          return {i, res->second};
        } else {
          outputs.insert(make_pair(target-nums[i], i));
        }
      }
      return {-1, -1};
    }
};