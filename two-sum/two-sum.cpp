#include <map>

class Solution {
public:
  vector<int> twoSum(vector<int>& nums, int target) {
    map<int, int> indexOfNums;
    
    for (int i = 0; i < nums.size(); i++) {
      indexOfNums.insert(pair<int, int>(nums[i], i));
    }
    
    for (int i = 0; i < nums.size(); i++) {
       try {
         int match = indexOfNums.at(target - nums[i]);
         if (match == i) {
           continue;
         } else {
           return {match, i};
         }
       } catch (const out_of_range& e) {
         continue;
       }
    } 
    return {};
  }
};


/*

2,7,11,15 = 9

3 4 7 9 19 11 = 18






*/