# Hashmap LEFT JOIN
Implement a simplified LEFT JOIN for 2 Hashmaps

## Challenge
Write a function that LEFT JOINs two hashmaps into a single data structure
    Write a function called left join
    Arguments: two hash maps
        The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
        The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.
Return: The returned data structure that holds the results is up to you. It doesn't need to exactly match the output below, so long as it achieves the LEFT JOIN logic

## Approach & Efficiency
Time O(n^2)
Space O(n)
## Solution
def leftjoin(h1, h2):
    final_result = []
    if h1.map == h1.size*[None]:
        return 'Right is empty'
    if h2.map == h2.size*[None]:
        return 'left is empty'
    for item in h1.map:
        if item:
            a2=[]
            a2.append(item.head.data[0])
            a2.append(h1.get(item.head.data[0]))
            a2.append(h2.get(item.head.data[0]))
            final_result.append(a2)
    return final_result
## NOTE:
**The solution contains strech goals for right joint**
## PR LINK:
https://github.com/Talafhamohammad-cloud/data-structures-and-algorithms-python/pull/49    
