class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int n= strs.size();
        sort(strs.begin(), strs.end());
        string ans="";
        for(int i=0; i<min(strs[0].size(), strs[n-1].size()); i++){
            if(strs[0][i]==strs[n-1][i]){
                ans.push_back(strs[0][i]);
            }
            else{
                return ans;
            }
        }
        return ans;
    }
};
