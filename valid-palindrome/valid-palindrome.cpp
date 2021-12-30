#include <iostream>
#include <cctype>
class Solution {
public:
    bool isPalindrome(string s) {
      vector<char> stripped;
      vector<char> reverse;
      
      for (int i = 0; i < s.size(); i++) {
        if ((s[i] <= 90 && s[i] >= 65) || (s[i] <= 122 && s[i] >= 97)) {
          stripped.emplace_back(tolower(s[i]));
        } else if (s[i] <= 57 && s[i] >= 48) {
          stripped.emplace_back(s[i]);
        }
      }
      
      if (stripped.size() == 0) return true;
      for (int i = stripped.size() - 1; i >= 0; i--) {
        reverse.emplace_back(stripped[i]);
      }
      
      for (int i = 0; i < stripped.size(); i++) {
        std::cout << stripped[i] << ", " << reverse[i] << std::endl;
        if (stripped[i] != reverse[i]) return false;
      }
      return true;
    }
};