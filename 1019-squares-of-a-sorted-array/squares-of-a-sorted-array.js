/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
    var newarr = []
    for (var x = 0 ; x < nums.length ; x++){
        let num = nums[x] ** 2
        newarr.push(num)
    }

    newarr.sort((a, b) => a - b);
    return newarr
};