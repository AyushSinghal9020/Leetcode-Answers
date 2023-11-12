||||
|---|---|---|
|Python|
||<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/44194851-856f66f2fc031e589a4195eaca0d1765.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231112%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231112T103920Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=c4de8ef45cf2ef140736f996b4062deeb325ffce7b1d9949f1588875972cc1da' width = 400>|<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/44194854-4f1cbbccb43391e1eb2dd2c7d9faaf5e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231112%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231112T103942Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=d12c42ad1e099ba0ee5a83b0ebe5c3f34bf0867baff7e4ff540f12af5a54eeb1' width = 400>


# Question 39
****
## Combination Sum

****
### Problem Statement -

Given an array of **distinct** integers `candidates` and a target integer `target`, return *a list of all* **unique combinations** *of* `candidates` *where the chosen numbers sum to* `target`. You may return the combinations in any **order**.

The **same** number may be chosen from `candidates` an **unlimited number of times**. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to `target` is less than `150` combinations for the given input

### Examples

```
Input: candidates = [2,3,6,7], target = 7

Output: [[2,2,3],[7]]

Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

```
```
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
```
```
Input: candidates = [2], target = 1

Output: []
```
****
### Constraints
```
1 <= candidates.length <= 30

2 <= candidates[i] <= 40

All elements of candidates are distinct.

1 <= target <= 40
```
