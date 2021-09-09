from hash_table.hash_table import *

def tree_intersection(t1, t2):
    if not t1.root or not t2.root:
        return "there is empty one or both of them"
    arr1 = t1.pre_order()
    arr2 = t2.pre_order()
    t1itersectt2 = []
    new_hashtable = Hashtable()
    for node in arr1:
     new_hashtable.add(node, node)
    for element in arr2:
        if new_hashtable.contains(element):
            t1itersectt2.append(element)

    if t1itersectt2 == []:
        return "intersection = phi(Φ)"
    else:
     return t1itersectt2
