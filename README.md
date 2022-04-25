# instawork-fullstack
## This is a project for instawork coop interview

**Version 1.0.0** 

## Installation

```bash
python -m pip install django
````

## Run this project
```bash
cd instawork-fullstack/hw2022
```

```bash
python manage.py runserver
```
Then this project will run on port 8000 at your localhost

## Backend API
### Name: Info
Primary key: ID  
FirstName,  
LastName,  
email,  
phone,  
isAdmin  

## Api Folder
models.py --database table for this website  
views.py --click events for this website  

## Static Folder
Include script and images for frontend  

## Template Folder
Three html files for this website  

# Data structure is a particular way of organizing data in a computer so that it can be used efficiently.  

## Common data structure
- Array int a[10] = xxxxxxxxxx
- Stack
- Queue
- Linked List
- Tree
- Heap
- Graph
- Hash table

## Array: Physic memory
基本知识点: 都建立在array这个数据结构上
- Binary Search
- Partition
- Sorting Alogrithms
- SubSet
- Deduplication
- Longest subarray/sequence
- Common Sequence
- Sliding Window
- Re-ordering
- Compression
- Geometry

## How to judge whether you program is good or not
Big O notation: algorithm complexity (time complexity, space complexity)

## Binary Search
What is binary search in the context of an array?  
1. Common assumptions: Array has to be sorted. ascending or descending. (Is this necessary?)  
2. 春招新题目  
    2 3 6 8 12 15 19 17 13 9 7 4 2 1    find target = 9  
    找到分界点，然后对各自sorted的数组使用binary search  

    left = mid 或者right = mid 会进入死循环，切记避免。eg: array[0] = 1, target = 2;  

Question 2: Classical Binary Search in 2D Space  
2D matrix, sorted on each row, first element of next row is larger(or equal) to the last element of previous   row, now giving a target number, returning the position that the target locates within the matrix  
1   3   4   6   7  
8   9   10  11  14  
15  17  19  20  23  

target = 11;  

index:0 1   2   3   4   5   6   7   8   9   10  
input:1 3   4   6   7   8   9   10  11  14  17  

how to map index = 7 back to 2D coordinate?  

row = 7 / 5 = 1.XX 向下取整 前面有一行  
col = 7 % 5 取余  

```java
public boolean ifFind(int[][] matrix, int target)
{
    if(matrix.length == 0 || matrix[0].length == 0)
    {
        return false;l
    }
    int row = matrix.length;
    int col = matrix[0].length;
    int i = 0;
    int j = row * col - 1;
    while(i <= j)
    {
        int mid = i + (j - i) / 2;
        int r = mid / col;
        int c = mid % col;
    }
    if(matrix[r][c] == target)
    {
        return true;
    }else if(matrix[r][c] > target)
    {
        j = mid - 1;
    }else if(matrix[r][c] < target)
    {
        i = mid + 1;
    }
    return false;
}
```

## Why and when does the dead loop happen?  
Principles of Binary Search  
1. We must guarantee that the search space decreases over time(after each iteration)
2. We must guarantee that the target (if exists) cannot be ruled out accidentally, when we cahnge the value of Left or Right.(It is critical to define the rule about how to move the rage for search, 注意要点： 反逻辑)

## Binary Search Variants
Question 3: Closest Element to Target
How to find an element in the array that is closeset to the target number?

When you only have two elements left in the valid range, then you only need to check whether the left choice or right choice is the answer(if exists)

```Java
int binarySearch(int[] a, int left, int right, int target)
{
    int mid;
    while(left < right - 1)
    {
        mid = left + (right - left) / 2;
        if(a[mid] == target)
        {
            return mid;
        }else if(a[mid] < target)
        {
            left = mid;
        }else {
            right = mid;
        }
    }
}
```

## Question 4: First Target
How to return the index of the first occurrence of an element, let's say 5  
index: 0 1 2 3 4 5 6  
value: 2 5 5 5 5 5 5  
iteration 1:


## Question 5: Last Target


## Binary Search mid
Question 6: Closes k Elements:  
How to return the index of k elements that are closest elements to the target.  


## Question 7: Smallest Element that is larget than target -- First occurrence

## 思考题 One missing number in sorted array of [0, n -1], find this missing number
Solution:
How can we convert this problem into the existing solutions that we have?  

First occurence of 2  

## Binary Search 高等难度
K-th Smallest in Two Sorted Arrays
1. tow sorted integer arrays, how to find the median of the two arrays
2. two sorted integer arrays, how to find the k-th smallest element from them
A[] = {2, 5, 7, 10, 13}
b[] = {1, 3, 4, 13, 20, 29}

Solution1: 谁小移谁，双指针

## Binary search with unknown size
Given a sorted array with unknown size, how to determin whether is a number is in it or not.  
Example: dictionary[x] = {1, 3, 5, 7, ..., ...}  
Target = 9999  
Assumption if unput[index] == NULL then we know the size of dictionary is < index;  
Problem: 不知道right boundary  

Step 1: Jump From left most 2 times each time O(log N)  
找右边界  
Step 2: [L, R] Binary Search  
二分查找  
