# Merge sort :
To perform the merging, we use an auxiliary procedure Merge(A,p,q,r) where
A is an array, p,q,r are indices of elements in the array, 
such that p≤q<r and the subarrays A[p..q] and A[q+1..r] are in sorted order
It merges them to form a single sorted subarray that replaces the current subarray A[p..r].
Basic idea: Suppose we have two piles of cards face up on a table. Each pile is sorted, with the smallest cards on top.
We choose the smaller of the two cards on top of the face-up piles, removing it from its pile, placing this card face down onto the output pile. 
We repeat this step until one input pile is empty
We take the remaining input pile and place it face down onto the output pile.
