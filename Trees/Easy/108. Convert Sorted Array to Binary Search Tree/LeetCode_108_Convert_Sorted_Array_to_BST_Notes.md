# LeetCode 108 --- Convert Sorted Array to Binary Search Tree

## Problem

Given a sorted array, construct a **height-balanced Binary Search Tree
(BST)**.

Example:

``` text
nums = [-10, -3, 0, 5, 9]
```

One valid answer is:

``` text
        0
       / \
     -3   9
     /   /
  -10   5
```

------------------------------------------------------------------------

# How I Figured Out the Solution

## 1. First confusion: Does the smallest number become the root?

My first thought was:

> "Smallest number will be the root."

That is **not correct** for a balanced BST.

If the smallest number were the root, almost all values would have to go
into the right subtree, making the tree unbalanced.

For:

``` text
[1, 2, 3, 4, 5, 6, 7]
```

the better root is:

``` text
4
```

because there are three elements on each side.

### Key insight

Because the array is sorted:

``` text
[1, 2, 3]  4  [5, 6, 7]
             ↑
            root
```

So:

> **The middle element should become the root.**

------------------------------------------------------------------------

# 2. Split the array

After choosing the middle:

``` text
[1, 2, 3, 4, 5, 6, 7]
         ↑
         4
```

The array becomes:

``` text
left half:  [1, 2, 3]
right half: [5, 6, 7]
```

Therefore:

``` text
        4
       / \
 [1,2,3] [5,6,7]
```

Then I realized:

> We can do the exact same thing to each half.

This is **recursion**.

------------------------------------------------------------------------

# 3. Recursion means solving the same smaller problem

For:

``` text
[1, 2, 3]
```

the middle is:

``` text
2
```

For:

``` text
[5, 6, 7]
```

the middle is:

``` text
6
```

So:

``` text
        4
       / \
      2   6
     / \ / \
    1  3 5  7
```

The same operation keeps repeating.

### Recursive pattern

``` text
sorted array
     ↓
find middle
     ↓
middle becomes root
     ↓
left half → recursively build left subtree
right half → recursively build right subtree
```

------------------------------------------------------------------------

# 4. The difficult part: When does recursion stop?

This was the part I found difficult.

I initially thought about stopping when there was only one element.

But the better way to think about it is:

> **Stop when there are no elements left to build a subtree.**

If the current range is:

``` text
left = 4
right = 3
```

then there are no valid indices.

Therefore:

``` python
if left > right:
    return None
```

This is the **base case**.

------------------------------------------------------------------------

# 5. Why use `left` and `right`?

Initially I tried to manipulate the array directly.

But then I understood that the recursive function should know which part
of the original array it is currently responsible for.

So we create:

``` python
def build(left, right):
```

For example:

``` text
build(0, 6)
```

means:

> Build a tree using indices 0 through 6.

After choosing index 3 as the root:

``` text
build(0, 2)    → left subtree
build(4, 6)    → right subtree
```

Then:

``` text
build(0, 2)
    ↓
build(0, 0)
build(2, 2)
```

and so on.

------------------------------------------------------------------------

# 6. Finding the middle

At first I used:

``` python
mid = len(nums) // 2
```

That works only for the **entire array**.

It does not work inside recursive calls because each call operates on a
different range.

For example:

``` text
build(0, 2)
```

should have:

``` text
mid = 1
```

while:

``` text
build(4, 6)
```

should have:

``` text
mid = 5
```

Therefore the middle must be calculated from the current boundaries:

``` python
mid = (left + right) // 2
```

This is the same idea used in binary search.

------------------------------------------------------------------------

# 7. Creating the current root

Once we know `mid`:

``` python
mid = (left + right) // 2
```

the value at that position becomes the root:

``` python
root = TreeNode(nums[mid])
```

Important distinction:

``` text
mid       → index
nums[mid] → actual value
```

For example:

``` text
nums = [1, 2, 3, 4, 5, 6, 7]
mid = 3
nums[mid] = 4
```

So:

``` python
root = TreeNode(nums[mid])
```

creates:

``` text
    4
```

------------------------------------------------------------------------

# 8. The biggest recursion insight

The most important part was understanding these two lines:

``` python
root.left = build(left, mid - 1)
root.right = build(mid + 1, right)
```

I initially tried to manually change `left` and `right`.

That was wrong.

Instead, each recursive call receives a **new range**.

For:

``` text
build(0, 6)
```

we get:

``` text
             4
           /   \
      build(0,2) build(4,6)
```

The helper function builds each subtree and **returns its root**.

That returned node is assigned to:

``` python
root.left
```

or:

``` python
root.right
```

This is the key idea to remember for recursive tree problems:

> **A recursive tree function usually returns the root of the subtree it
> just built.**

------------------------------------------------------------------------

# 9. Final solution

``` python
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:

        def build(left, right):
            if left > right:
                return None

            mid = (left + right) // 2
            root = TreeNode(nums[mid])

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(nums) - 1)
```

------------------------------------------------------------------------

# 10. Full visualization / Dry Run

For:

``` text
nums = [1, 2, 3, 4, 5, 6, 7]
```

## Call 1

``` text
build(0, 6)

left = 0
right = 6
mid = 3
nums[3] = 4
```

Create:

``` text
        4
```

Then:

``` text
build(0, 2)
build(4, 6)
```

------------------------------------------------------------------------

## Call 2 --- Left subtree

``` text
build(0, 2)

left = 0
right = 2
mid = 1
nums[1] = 2
```

Create:

``` text
        4
       /
      2
```

Then:

``` text
build(0, 0)
build(2, 2)
```

------------------------------------------------------------------------

## Call 3 --- Node 1

``` text
build(0, 0)

mid = 0
nums[0] = 1
```

Create:

``` text
        4
       /
      2
     /
    1
```

Then:

``` text
build(0, -1) → None
build(1, 0)  → None
```

So node `1` is complete.

------------------------------------------------------------------------

## Call 4 --- Node 3

``` text
build(2, 2)

mid = 2
nums[2] = 3
```

Create:

``` text
        4
       /
      2
     / \
    1   3
```

Its children are empty:

``` text
build(2, 1) → None
build(3, 2) → None
```

So node `2` is complete.

------------------------------------------------------------------------

## Call 5 --- Right subtree

Back to:

``` text
build(4, 6)
```

``` text
left = 4
right = 6
mid = 5
nums[5] = 6
```

Create:

``` text
        4
       / \
      2   6
```

Then:

``` text
build(4, 4)
build(6, 6)
```

These create `5` and `7`.

Final tree:

``` text
            4
          /   \
         2     6
        / \   / \
       1   3 5   7
```

------------------------------------------------------------------------

# 11. The recursion tree

The calls can be visualized as:

``` text
build(0,6)
│
├── build(0,2)
│   │
│   ├── build(0,0)
│   │   ├── build(0,-1) → None
│   │   └── build(1,0)  → None
│   │
│   └── build(2,2)
│       ├── build(2,1) → None
│       └── build(3,2) → None
│
└── build(4,6)
    │
    ├── build(4,4)
    │   ├── build(4,3) → None
    │   └── build(5,4) → None
    │
    └── build(6,6)
        ├── build(6,5) → None
        └── build(7,6) → None
```

------------------------------------------------------------------------

# 12. Why the base case works

The base case:

``` python
if left > right:
    return None
```

handles all the empty subtrees.

For example:

``` text
build(0, -1)
```

means there is nothing to put on the left of node `1`.

So:

``` text
1
```

gets:

``` python
left = None
```

Likewise:

``` text
build(1, 0)
```

returns `None` for its right child.

This is how the recursion naturally terminates.

------------------------------------------------------------------------

# 13. Important Notes

## BST vs Binary Tree

A **Binary Tree** only says each node has at most two children.

A **BST** additionally requires:

``` text
left subtree values < root < right subtree values
```

This problem is specifically constructing a **height-balanced BST**.

------------------------------------------------------------------------

## Do not use normal BST insertion

We don't need:

``` python
if value < root.val:
    go left
else:
    go right
```

because the input is already sorted.

The sorted order lets us directly choose the middle and split the array.

------------------------------------------------------------------------

## Do not use a `while` loop

This is not normal binary search.

Binary search searches for **one value**:

``` text
choose middle
→ discard one half
→ repeat
```

Here we need to build **both halves**:

``` text
choose middle
→ build left
→ build right
```

Therefore recursion is the natural approach.

------------------------------------------------------------------------

# 14. Complexity

### Time: `O(n)`

Every element becomes exactly one `TreeNode`.

### Space: `O(log n)`

The tree is height-balanced, so the recursion depth is approximately:

``` text
log₂(n)
```

The output tree itself requires `O(n)` space, but the **auxiliary
recursion stack** is `O(log n)`.

------------------------------------------------------------------------

# 15. Pattern to Remember for Future Tree Problems

When you see a recursive tree construction problem, ask:

### Question 1

**What represents the current subtree?**

Here:

``` text
left, right
```

### Question 2

**What is the base case?**

Here:

``` python
if left > right:
    return None
```

### Question 3

**How do I choose the current root?**

Here:

``` python
mid = (left + right) // 2
root = TreeNode(nums[mid])
```

### Question 4

**How do I construct the children?**

Here:

``` python
root.left = build(left, mid - 1)
root.right = build(mid + 1, right)
```

### Question 5

**What does the recursive function return?**

Here:

``` python
return root
```

------------------------------------------------------------------------

# Final Mental Model

``` text
              build(left, right)
                       │
                       ▼
              Is range empty?
                 /          \
               YES           NO
                │             │
             return None      ▼
                         find middle
                              │
                              ▼
                         create root
                         /          \
                        /            \
             build(left,mid-1)   build(mid+1,right)
                    │                  │
                    ▼                  ▼
                left subtree       right subtree
                        \            /
                         \          /
                          ▼        ▼
                           return root
```

## What I learned from this problem

The difficult part was **not finding the middle**.

The difficult part was understanding that:

> `build(left, right)` represents one complete subtree.

Once that is understood, the solution becomes:

``` text
middle → root
left range → left subtree
right range → right subtree
empty range → None
```

That is the main recursion pattern I should remember.
