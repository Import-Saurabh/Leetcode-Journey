# Binary Tree Inorder Traversal --- Visualization

## Code

``` python
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        result=[]

        def inorder(node):
            if node is None:
                return

            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)
        return result
```

------------------------------------------------------------------------

## Example Input

``` text
root = [1, null, 2, 3]
```

The tree is:

``` text
    1
     \
      2
     /
    3
```

------------------------------------------------------------------------

## Inorder Rule

``` text
LEFT → ROOT → RIGHT
```

The function always follows these three operations:

``` python
inorder(node.left)
result.append(node.val)
inorder(node.right)
```

------------------------------------------------------------------------

## Step-by-Step Execution

### Step 1 --- Start at node 1

``` text
        1  ← current node
         \
          2
         /
        3
```

Call:

``` python
inorder(1)
```

First:

``` python
inorder(1.left)
```

But:

``` text
1.left = None
```

So:

``` python
inorder(None)
```

hits:

``` python
if node is None:
    return
```

Nothing is added.

``` text
result = []
```

------------------------------------------------------------------------

### Step 2 --- Visit node 1

The left side is finished.

Now:

``` python
result.append(1)
```

So:

``` text
result = [1]
```

Then:

``` python
inorder(1.right)
```

moves to node `2`.

------------------------------------------------------------------------

### Step 3 --- Visit node 2

``` text
    2
   /
  3
```

Call:

``` python
inorder(2)
```

First go left:

``` python
inorder(2.left)
```

which means:

``` python
inorder(3)
```

------------------------------------------------------------------------

### Step 4 --- Visit node 3

``` text
3
```

First:

``` python
inorder(3.left)
```

But:

``` text
3.left = None
```

Return.

Now:

``` python
result.append(3)
```

Result becomes:

``` text
result = [1, 3]
```

Then:

``` python
inorder(3.right)
```

But:

``` text
3.right = None
```

Return.

Node `3` is completely finished.

------------------------------------------------------------------------

### Step 5 --- Return to node 2

We are back at node `2`.

Its left subtree is finished:

``` text
    2
   /
  3  ✓
```

Now execute:

``` python
result.append(2)
```

Result:

``` text
result = [1, 3, 2]
```

Then:

``` python
inorder(2.right)
```

But:

``` text
2.right = None
```

Return.

------------------------------------------------------------------------

## Final Result

``` text
result = [1, 3, 2]
```

The function returns:

``` python
[1, 3, 2]
```

------------------------------------------------------------------------

## Recursion Flow

A simplified view of the calls:

``` text
inorder(1)
│
├── inorder(None)
│
├── append(1)
│
└── inorder(2)
    │
    ├── inorder(3)
    │   │
    │   ├── inorder(None)
    │   ├── append(3)
    │   └── inorder(None)
    │
    ├── append(2)
    └── inorder(None)
```

Values are appended in this order:

``` text
1 → 3 → 2
```

Therefore:

``` text
LEFT → ROOT → RIGHT
```

produces:

``` text
[1, 3, 2]
```

------------------------------------------------------------------------

## The Key Idea

`root` or `node` is a **TreeNode**.

Therefore:

``` python
node.val
```

gets the value.

``` python
node.left
```

gets the left child.

``` python
node.right
```

gets the right child.

Think of every node as:

``` text
       node
      /    \
   left   right
     \
     val
```

More precisely:

``` text
TreeNode
├── val
├── left  → TreeNode or None
└── right → TreeNode or None
```

The recursive algorithm simply keeps moving:

``` text
LEFT
 ↓
ROOT
 ↓
RIGHT
```

until it reaches `None`.
