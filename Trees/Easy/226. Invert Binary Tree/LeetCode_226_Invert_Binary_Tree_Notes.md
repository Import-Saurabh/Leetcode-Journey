# LeetCode 226 --- Invert Binary Tree

-   **Difficulty:** Easy
-   **Topic:** Binary Tree, Recursion, Depth-First Search
-   **Problem:** [226. Invert Binary
    Tree](https://leetcode.com/problems/invert-binary-tree/)
-   **Status:** Solved with hints and debugging

------------------------------------------------------------------------

## 1. Understand the problem

We are given the root of a binary tree. We must invert the tree and
return its root.

Inverting a tree means **swapping the left and right child of every
node**. The values do not change; only the links between nodes change.

Example:

``` text
Original:                 Inverted:

        4                         4
       / \\                       / \\
      2   7                     7   2
     / \\ / \\                   / \\ / \\
    1  3 6  9                 9  6 3  1
```

Input: `[4,2,7,1,3,6,9]`

Output: `[4,7,2,9,6,3,1]`

The root remains `4`, but every node's children are swapped.

## 2. How I arrived at the solution

### Step 1 --- Figure out what "invert" means

I first considered the root node `4`, whose left child is `2` and right
child is `7`.

To invert the root, I need to swap its `left` and `right` pointers.

In Python, two values can be swapped using tuple assignment:

``` python
node.left, node.right = node.right, node.left
```

This swaps the pointers; it does not change the values stored in the
nodes.

### Step 2 --- Realize that swapping only the root is not enough

After swapping node `4`, the top of the tree becomes:

``` text
        4
       / \\
      7   2
```

But nodes `2` and `7` also have children. If I stop here, their children
remain in their original positions, so the whole tree is not yet
inverted.

**Conclusion:** Every node must have its left and right children
swapped---not only the root.

### Step 3 --- Use recursion to process every node

I asked: "Who will swap the children of node `7` and node `2`?"

The answer is to call the same helper function on both children. The
function can solve the same problem on each smaller subtree.

Conceptually:

``` text
invert(4)
    swap children of 4
    invert(current left child)   # now node 7
    invert(current right child)  # now node 2
```

Those calls continue down the tree until all nodes have been processed.

This is recursion: a function calls itself to solve the same kind of
problem on smaller inputs.

### Step 4 --- Identify the base case

A recursive function needs a stopping condition.

If the current node is `None`, there is no node to invert. The function
must stop instead of trying to access `.left` or `.right`.

The base case for the helper is:

``` python
if node is None:
    return
```

The main function also checks whether `root` is `None`, because the
input tree itself may be empty.

### Step 5 --- Decide what to return

The problem asks us to return the root of the inverted tree.

Inverting the tree changes its child pointers; it does not replace the
root node. Therefore, after the helper has modified the tree in place,
the main function returns `root`.

A list such as `result = []` is unnecessary because this problem does
not ask us to collect node values in a traversal list.

------------------------------------------------------------------------

## 3. Final solution

``` python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if root is None:
            return None

        def invert(node):
            if node is None:
                return

            node.left, node.right = node.right, node.left

            invert(node.left)
            invert(node.right)

        invert(root)
        return root
```

## 4. The bug I encountered

My helper initially looked like this:

``` python
def invert(node):
    node.left, node.right = node.right, node.left
    invert(node.left)
    invert(node.right)
```

The recursive calls were correct, but I forgot the base case **inside
the helper**.

### Why did it crash?

When recursion reaches a leaf, such as node `1`, both children are
`None`.

The function then calls `invert(node.left)`, which becomes
`invert(None)`. Without a base case, the next line tries to access
`node.right` on `None`, causing:

``` text
AttributeError: 'NoneType' object has no attribute 'right'
```

### Fix

Check whether `node is None` before accessing its children:

``` python
if node is None:
    return
```

**Important lesson:** A base case in the outer function does not
automatically protect a separate recursive helper. The helper needs its
own stopping condition when it can receive `None`.

## 5. Trace the recursion

For the input tree:

``` text
        4
       / \\
      2   7
     / \\ / \\
    1  3 6  9
```

The first call is `invert(root)` where `root` is node `4`.

  Current node   Action          Children after swap
  -------------- --------------- ---------------------
  `4`            Swap children   Left `7`, right `2`
  `7`            Swap children   Left `9`, right `6`
  `9`            Swap children   Both `None`
  `6`            Swap children   Both `None`
  `2`            Swap children   Left `3`, right `1`
  `3`            Swap children   Both `None`
  `1`            Swap children   Both `None`

The exact order of visiting nodes follows the code: swap the current
node, then recurse into its left child, then its right child. Because
the swap happens first, those recursive calls use the **new** left and
right pointers.

Final tree:

``` text
        4
       / \\
      7   2
     / \\ / \\
    9  6 3  1
```

The returned tree is `[4,7,2,9,6,3,1]`.

## 6. Why the algorithm works

At every non-empty node, the algorithm:

1.  Swaps its two child pointers.
2.  Recursively inverts the subtree now on the left.
3.  Recursively inverts the subtree now on the right.

The base case stops at missing children. Since the helper processes
every existing node exactly once, every node is inverted. The original
root is returned after the in-place changes are complete.

## 7. Complexity analysis

Let `n` be the number of nodes and `h` be the height of the tree.

-   **Time complexity: `O(n)`** --- each node is visited once, and the
    work at each node is constant.
-   **Auxiliary space: `O(h)`** --- recursive calls occupy the call
    stack. In a balanced tree, this is `O(log n)`; in a maximally skewed
    tree, it can be `O(n)`.

## 8. What I learned

-   Inversion means swapping pointers, not swapping node values.
-   Swapping only the root does not invert the whole tree.
-   Recursion lets the same operation apply to every subtree.
-   A recursive helper must stop when its input is `None`.
-   Return the original root after changing its links in place.
-   I was close: the main algorithm and recursive calls were right. The
    runtime error came from missing the helper's base case.

## 9. Recursion checklist for future tree problems

Before submitting a recursive tree solution, ask:

1.  **Base case:** What should happen when the node is `None`?
2.  **Current node:** What work must happen at this node?
3.  **Recursive calls:** Which child subtrees need the same operation?
4.  **Return value:** What does the problem expect me to return?
5.  **Trace:** What happens at a leaf, where both children are `None`?

------------------------------------------------------------------------

## My short revision note

**Invert Binary Tree = swap every node's left and right pointers.**

Pattern:

1.  Stop if the current node is `None`.
2.  Swap its children.
3.  Recursively process both children.
4.  Return the original root from the main function.

The mistake to remember: **do not forget the base case inside the
recursive helper.**
