class Solution {
public:
    int numberOfEmployeesWhoMetTarget(vector<int>& hours, int target) {
        int count = 0;
        for ( int x = 0 ; x < hours.size() ; x++){
            if (hours[x] >= target){
                count++;
            }
        }

        return count;
    }
};