# Hashtables
A hash table (hash map) is a data structure in computing that implements an associative array abstract data type, which may map keys to values. A hash table employs a hash function to generate an index, often referred to as a hash code, into an array of buckets or slots from which the necessary item may be retrieved.

## Challenge
Implement a Hashtable Class with the following methods:

(add)

Arguments: key, value

Returns: nothing

This method should hash the key, and add the key and value pair to the table, handling collisions as needed.

(get)

Arguments: key

Returns: Value associated with that key in the table

(contains)

Arguments: key

Returns: Boolean, indicating if the key exists in the table already.

(hash)

Arguments: key

Returns: Index in the collection for that key

## Approach & Efficiency:
Time : O(1)

Space : O(1)
## API
(add)

Arguments: key, value

Returns: nothing

This method should hash the key, and add the key and value pair to the table, handling collisions as needed.

(get)

Arguments: key

Returns: Value associated with that key in the table

(contains)

Arguments: key

Returns: Boolean, indicating if the key exists in the table already.

(hash)

Arguments: key

Returns: Index in the collection for that key

## PR link:
https://github.com/Talafhamohammad-cloud/data-structures-and-algorithms-python/pull/43


#######################################################################################################################

# CH-31(repeated word)

# Challenge Summary
Write a function called repeated word that finds the first word to occur more than once in a string
Arguments: string
Return: string

## Whiteboard Process

![image](repeatedwords.jpg)

## Approach & Efficiency
Time O(n)
Space O(1)
## Solution
     def repeatedword(string):
      if not string:
        return "empty"
     strng =[".",",","-"]  
     for char in strng:  
     string = (string.replace(char, "")).lower()
     words = string.split()
     new_hashtable = Hashtable()
     for word in words:
        if new_hashtable.contains(word):
            return word
        else:
            new_hashtable.add(word, word)
     return "There is no dublication"

## PR LINK:
https://github.com/Talafhamohammad-cloud/data-structures-and-algorithms-python/pull/46

####################################################################################


