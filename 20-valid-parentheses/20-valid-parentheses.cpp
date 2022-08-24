class Solution {
public:
    bool isValid(string s) {
      stack<char> parenStack;
      
      for (int i = 0; i < s.size(); i++) {
        if (s[i] == '(' || s[i] == '[' || s[i] == '{') {
          parenStack.push(s[i]);
        } else {
          if (!parenStack.empty()) {
            if (s[i] == ')' && parenStack.top() == '(') {
              parenStack.pop();
            } else if (s[i] == '}' && parenStack.top() == '{') {
              parenStack.pop();
            } else if (s[i] == ']' && parenStack.top() == '[') {
              parenStack.pop();
            } else {
              return false;
            }
          } else {
            return false;
          }
        }
      }
      if (parenStack.empty()) {
        return true;
      }
      return false;
    }
};