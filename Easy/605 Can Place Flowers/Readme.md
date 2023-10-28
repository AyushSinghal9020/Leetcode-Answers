<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/43874845-80af5007c5adff98f7531d12f2b9a0e3.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231028T081445Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=8c7e182e54cc008eda52ec126afec6365efa4d3cc28c91349cb98768a6f5296c' width = 400><img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/43874860-25f1e9f4695a922757b72c5e00d5c5e6.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231028%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231028T081645Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=18fa9531e07d385229487d117c3b984cb80926f185f96b7b8e45d39f08b768c8' width = 400>

# Question 605
****
## Can Place Flowers

****
### Problem Statement -

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in **adjacent** plots.

Given an integer array `flowerbed` containing `0`'s and `1`'s, where `0` means empty and `1` means not empty, and an integer `n`, return `true` *if* `n` *new flowers can be planted in the* `flowerbed` *without violating the no-adjacent-flowers rule and* `false` *otherwise*.
### Examples
```
Input: flowerbed = [1,0,0,0,1], n = 1

Output: true
```
```
Input: flowerbed = [1,0,0,0,1], n = 2

Output: false
```

****
### Constraints
```
1 <= flowerbed.length <= 2 * 104

flowerbed[i] is 0 or 1.

There are no two adjacent flowers in 
flowerbed.

0 <= n <= flowerbed.length
```


