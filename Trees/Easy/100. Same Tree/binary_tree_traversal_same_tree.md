# Binary Tree Traversal & Comparing Two Trees

## Problem: Same Tree

Given two binary trees `p` and `q`, determine whether they are exactly the same.

Two trees are the same when:

1. They have the same structure.
2. Corresponding nodes have the same values.

---

## 1. First understand what `p` and `q` are

On LeetCode, you may see:

```text
p = [1, 2]
q = [1, null, 2]
```

These are representations of binary trees.

Inside the function, however:

```python
p: TreeNode | None
q: TreeNode | None
```

So `p` and `q` are **TreeNode objects**, not Python lists.

Therefore, this does NOT work:

```python
len(p)
```

Instead, access the tree through:

```python
p.val
p.left
p.right
```

---

# 2. How do we traverse a tree?

For every node, there are three important things:

```python
node.val
node.left
node.right
```

For example:

```text
       1
      / \
     2   3
```

Starting at `1`:

```python
root.val       # 1
root.left.val  # 2
root.right.val # 3
```

To visit the entire tree, we recursively visit:

```python
left subtree
right subtree
```

A basic traversal looks like:

```python
def traverse(root):
    if root is None:
        return

    print(root.val)

    traverse(root.left)
    traverse(root.right)
```

This is **preorder traversal**:

```text
Node → Left → Right
```

---

# 3. Why comparing only values is NOT enough

Suppose:

```text
Tree p:          Tree q:

    1                1
   /                  \
  2                    2
```

Both contain:

```text
1, 2
```

So this:

```python
values_p == values_q
```

could say they are equal.

But the trees are NOT the same.

Why?

Because in `p`, `2` is the **left child**.

In `q`, `2` is the **right child**.

Therefore:

> For trees, we must compare both **values AND structure**.

---

# 4. The most important question: what condition do we check first?

When comparing two tree nodes, think about the possible situations.

## Case 1: Both nodes are empty

```python
p is None
q is None
```

There is nothing left to compare.

Therefore:

```python
if p is None and q is None:
    return True
```

This is our **base case**.

---

## Case 2: Only one node is empty

Example:

```text
p:       1          q:       1
        /                   \
       2                     2
```

At some point we compare:

```text
p.left = 2
q.left = None
```

One exists and the other doesn't.

Therefore the trees cannot be the same:

```python
if p is None or q is None:
    return False
```

This condition should come **before accessing `.val`**.

Why?

Because this would crash:

```python
p.val
```

if `p` is `None`.

---

# 5. Now compare the values

Once we know both nodes exist:

```python
if p is None or q is None:
    return False
```

we can safely access:

```python
p.val
q.val
```

Then:

```python
if p.val != q.val:
    return False
```

If the values differ, the trees are immediately different.

---

# 6. What remains?

If:

```python
p.val == q.val
```

we still haven't proven that the trees are the same.

We must compare:

```text
left subtree with left subtree
right subtree with right subtree
```

So:

```python
self.isSameTree(p.left, q.left)
```

and:

```python
self.isSameTree(p.right, q.right)
```

Both must be `True`.

Therefore:

```python
return (
    self.isSameTree(p.left, q.left)
    and
    self.isSameTree(p.right, q.right)
)
```

---

# 7. Final solution

```python
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:

        # 1. Both are empty
        if p is None and q is None:
            return True

        # 2. Only one is empty
        if p is None or q is None:
            return False

        # 3. Values are different
        if p.val != q.val:
            return False

        # 4. Compare left and right subtrees
        return (
            self.isSameTree(p.left, q.left)
            and
            self.isSameTree(p.right, q.right)
        )
```

---

# 8. The order of conditions is important

Remember this order:

```text
             Start
               |
               v
       Both nodes None?
          /          \
        YES           NO
         |             |
       True       One node None?
                    /       \
                  YES        NO
                   |          |
                 False    Values different?
                              /      \
                            YES       NO
                             |         |
                           False    Compare
                                    left + right
```

In code:

```python
if p is None and q is None:
    return True

if p is None or q is None:
    return False

if p.val != q.val:
    return False

return (
    self.isSameTree(p.left, q.left)
    and
    self.isSameTree(p.right, q.right)
)
```

---

# 9. General pattern for recursive tree problems

A very useful pattern is:

```python
def function(root):

    # Base case
    if root is None:
        ...

    # Process current node
    ...

    # Recursively process children
    function(root.left)
    function(root.right)
```

For comparing **two** trees:

```python
def function(p, q):

    # Base cases
    ...

    # Compare current nodes
    ...

    # Compare corresponding children
    function(p.left, q.left)
    function(p.right, q.right)
```

---

# 10. Mental checklist

When you see a binary-tree comparison problem, ask:

### Step 1
Are both nodes `None`?

```python
p is None and q is None
```

→ `True`

### Step 2
Is exactly one node `None`?

```python
p is None or q is None
```

→ `False`

### Step 3
Do their values differ?

```python
p.val != q.val
```

→ `False`

### Step 4
Are their left subtrees the same?

```python
self.isSameTree(p.left, q.left)
```

### Step 5
Are their right subtrees the same?

```python
self.isSameTree(p.right, q.right)
```

Both must be true.

---

## Key takeaway

For `Same Tree`, don't think:

> "How do I get all the values into two lists?"

Think:

> "At every corresponding position, do these two nodes match?"

You compare:

```text
             p                 q

             1                 1       ← values match
            / \               / \
           2   3             2   3     ← values match
```

and recursively continue until every corresponding position has been checked.

That is why recursion is a natural solution for binary trees.
