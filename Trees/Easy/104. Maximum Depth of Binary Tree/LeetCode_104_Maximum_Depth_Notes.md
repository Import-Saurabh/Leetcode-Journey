# LeetCode 104 — Maximum Depth of Binary Tree

## Problem

Given the root of a binary tree, return its maximum depth.

The maximum depth is the number of nodes along the longest path from the root to the farthest leaf.

Example:

```text
        3
       / \
      9   20
         /  \
        15   7
```

Maximum depth = `3`.

---

# How I Arrived at the Solution

I wanted to solve this using recursion.

## Step 1 — Traverse left and right recursively

My first thought was:

> I need to recursively traverse the left and right nodes until the very end and count the nodes along the longest path.

That led to the idea that every node should ask its left and right subtrees for their depth.

---

## Step 2 — Find the base case

I asked:

> What happens when there is no node?

If:

```python
root is None
```

there are zero nodes, so:

```python
return 0
```

This became the base case:

```python
if root == None:
    return 0
```

This check must happen **before** accessing `root.left` or `root.right`.

---

## Step 3 — Get the depth of the left subtree

Instead of manually walking through the left subtree, I realized that I could ask the same function to calculate its depth:

```python
left_depth = self.maxDepth(root.left)
```

The important idea is that the function is calling itself with a smaller tree.

For example:

```text
        3
       /
      9
```

When `3` calls:

```python
self.maxDepth(root.left)
```

the new `root` becomes `9`.

Then `9` performs exactly the same process.

---

## Step 4 — Get the depth of the right subtree

The same thing happens on the right:

```python
right_depth = self.maxDepth(root.right)
```

So every node asks:

```text
What is the depth of my left subtree?
What is the depth of my right subtree?
```

---

## Step 5 — Compare the two depths

Once we have:

```python
left_depth
right_depth
```

we need to determine which side is deeper.

I first thought about using an `if` statement:

```python
if left_depth > right_depth:
    ...
else:
    ...
```

If the left side is deeper:

```python
return left_depth + 1
```

Otherwise:

```python
return right_depth + 1
```

---

## Step 6 — Why do we add 1?

This was an important part of the reasoning.

Suppose:

```text
left_depth = 1
right_depth = 2
```

The current node is also part of the path.

So the current node's depth is:

```text
max(left_depth, right_depth) + 1
```

The `+1` represents the **current node**.

---

# Final Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root == None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        if left_depth > right_depth:
            return left_depth + 1
        else:
            return right_depth + 1
```

---

# The Recursion Flow

For:

```text
        3
       / \
      9   20
         /  \
        15   7
```

The recursion goes all the way down first.

### Node 15

```text
left = None  → 0
right = None → 0
```

Therefore:

```text
depth = 0 + 1 = 1
```

### Node 7

Same:

```text
depth = 1
```

### Node 20

```text
left_depth  = 1
right_depth = 1
```

Therefore:

```text
depth = 1 + 1 = 2
```

### Node 9

```text
left_depth  = 0
right_depth = 0
```

Therefore:

```text
depth = 1
```

### Node 3

Now:

```text
left_depth  = 1
right_depth = 2
```

The right side is deeper:

```text
depth = 2 + 1 = 3
```

Final answer:

```text
3
```

---

# Important Mistake I Encountered

Initially I wrote:

```python
left_depth = maxDepth(root.left)
right_depth = maxDepth(root.right)
```

This produced:

```text
NameError: name 'maxDepth' is not defined
```

The reason is that `maxDepth` is a method belonging to the `Solution` object.

Therefore, when calling the method recursively, I need:

```python
self.maxDepth(...)
```

instead of:

```python
maxDepth(...)
```

---

# Core Pattern Learned

The important recursion pattern is:

```text
Current node
    ↓
Ask left subtree for its answer
    ↓
Ask right subtree for its answer
    ↓
Combine both answers
    ↓
Return answer for current node
```

For maximum depth:

```text
depth(node)
=
1 + max(
    depth(left),
    depth(right)
)
```

with the base case:

```text
depth(None) = 0
```

---

# Complexity

### Time Complexity

```text
O(n)
```

Every node is visited once.

### Space Complexity

```text
O(h)
```

where `h` is the height of the tree, because of the recursive call stack.

For a balanced tree this is approximately:

```text
O(log n)
```

For a completely skewed tree it can become:

```text
O(n)
```

---

# What I Actually Learned

The main lesson wasn't just how to solve Maximum Depth.

It was understanding how recursion works on a tree:

> **A node doesn't need to know how to traverse the entire tree. It only needs to ask its children for their answers and combine those answers.**

For this problem:

```text
left subtree → gives left depth
right subtree → gives right depth
current node → adds 1
```

This pattern will be useful for many other binary-tree problems.
