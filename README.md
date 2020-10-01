# setsInPython
Work 11: Implementing the list comprehension in basic sets. 

Example 1: Union
```python
  def union(A, B):
      return [x for x in A if x not in B] + intersect(A,B) + [x for x in B if x not in A]
```
```c++
Input[1]: union([0, 8, 5, 9, 7, 3, 6, 2, 4], [1, 0, 4, 3, 6, 7])
Ouput[1]: [8, 5, 9, 2, 0, 7, 3, 6, 4, 1]
```
Example 2: Intersection
```python
def intersect(A, B):
    return [x for x in A if x in B]
```
```c++
Input[2]: intersect([0, 8, 5, 9, 7, 3, 6, 2, 4], [1, 0, 4, 3, 6, 7])
Output[2]: [0, 7, 3, 6, 4]
```
Example 3: Returning the elements from set A, but not in set B: eg. ```set(a) - (set(a) & set(b) ```
```python
def setDiff(A, B):
    return [x for x in A if x not in B]
```
```c++
Input[3]: setDiff([0, 8, 5, 9, 7, 3, 6, 2, 4], [1, 0, 4, 3, 6, 7])
Output[3]: [8, 5, 9, 2]
```

Example 4: Merging the two sets and eliminating the all duplicates of set A and set B. eg. ``` (set(a) | set(b)) - (set(a) & set(b))```
```python
def symDiff(A, B):
    return union(setDiff(A,B), setDiff(B,A))
```
```c++
Input[4]: union(setDiff([1,2,3,4,5],[0,1,2,3]), setDiff([0,1,2,3],[1,2,3,4,5]))
Output[4]: [0, 4, 5]
```
Example 5: A nested list of the elements of two sets.
```python
a,b = [0,1], [1,2]
```python
def cartProd(A, B):
    return [[a,b] for a in A for b in B]
a,b = [0,1], [1,2]
#expected output = [[0,1], [0,2], [1,1], [1,2]]
#explanation - [i,k] -> i is the element of set A, k is the element of set B; and k is from 0th to the last index for each i. 

```c++
Input[5]: cartProd([0,1],[1,2])
Output[5]: [[0,1], [0,1], [1,1], [1,2]]
```
