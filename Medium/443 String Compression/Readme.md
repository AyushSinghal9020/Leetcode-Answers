<img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/43987818-4669c0edac7f1aa086911b80f259e221.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231102%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231102T144601Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=e1057ad0be43fa7050b2acda215c34cd34db5e386d15535d87bfa331727a34a9' width = 400><img src = 'https://awesomescreenshot.s3.amazonaws.com/image/4900480/43987833-9497e608c5e57cde72552a7e834bed7b.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20231102%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231102T144637Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=f33444f282a16544b2f8e249c1df80ed96cce17249d3f580910feae7e82bbe0d' width = 400>

# Question 443
****
## String Compression

****
### Problem Statement -

Given an array of characters `chars`, compress it using the following algorithm:

Begin with an empty string `s`. For each group of **consecutive repeating characters** in `chars`:

* If the group's length is `1`, append the character to `s`.
* Otherwise, append the character followed by the group's length.

The compressed string `s` **should not be returned separately**, but instead, be stored **in the input character array** `chars`. Note that group lengths that are `10` or longer will be split into multiple characters in `chars`.

After you are done **modifying the input array**, *return the new length of the array*.

You must write an algorithm that uses only constant extra space.
### Examples
```
Input: chars = ["a","a","b","b","c","c","c"]

Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
```
```
Input: chars = ["a"]

Output: Return 1, and the first character of the input array should be: ["a"]

Explanation: The only group is "a", which remains uncompressed since it's a single character.
```
```
Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
```

****
### Constraints
```
1 <= chars.length <= 2000

chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.
```
