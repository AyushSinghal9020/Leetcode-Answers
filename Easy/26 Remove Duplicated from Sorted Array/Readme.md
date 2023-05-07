# Question 26
## Remove Duplicates from Sorted Array
### Problem Statement - 

Given an integer array `nums` sorted in **non-decreasing order**, remove the duplicates in-place such that each unique element appears only **once**. The **relative order** of the elements should be kept the **same**. Then return the number of unique elements in `nums`.

Consider the number of unique elements of `nums` to be `k`, to get accepted, you need to do the following things:

* Change the array `nums` such that the first `k` elements of `nums` contain the unique elements in the order they were present in `nums` initially. The remaining elements of `nums` are not important as well as the size of `nums`.
* Return `k`.

### Custom Judge:
```
The judge will test your solution with the following code:```
int[] nums = [...];                          // Input array
int val = ...;                               // Value to remove
int[] expectedNums = [...];                  // The expected answer with correct length.
                                             // It is sorted with no values equaling val.

int k = removeElement(nums, val);            // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k);                            // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
```

If all assertions pass, then your solution will be **accepted**.

### Examples
#### Example 1
```
Input: nums = [1,1,2]

Output: 2, nums = [1,2,_]

Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

```

#### Example 2
```
Input: nums = [0,1,2,2,3,0,4,2], val = 2

Output: 5, nums = [0,1,4,0,3,_,_,_]

Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
```
### Constraints
```
0 <= nums.length <= 100

0 <= nums[i] <= 50

0 <= val <= 100
```

