# LeetCode 101 --- Symmetric Tree

**Problem:** [Symmetric
Tree](https://leetcode.com/problems/symmetric-tree/)

**Goal:** Given the root of a binary tree, determine whether the tree is
a mirror of itself.

------------------------------------------------------------------------

## 1. The Core Idea

A binary tree is **symmetric** if its left half is the mirror image of
its right half.

The most important realization is:

> We do **not** compare `root.left` with `root.left` or `root.right`
> with `root.right`.\
> We compare the two subtrees as **mirror pairs**.

For two nodes `p` and `q` to be mirrors:

``` text
p.val == q.val

p.left  ↔ q.right
p.right ↔ q.left
```

So the recursive relationship is:

``` python
check(p.left, q.right)
check(p.right, q.left)
```

That cross-comparison is the heart of the solution.

------------------------------------------------------------------------

# 2. Start From the Definition of a Mirror

Imagine two trees facing each other:

``` text
        p                         q
       / \                       / \
      A   B                     C   D
```

For them to be mirror images:

``` text
p.left  must match q.right
p.right must match q.left
```

Therefore:

``` text
          p                 q
         / \               / \
        A   B             C   D
         ↖   ↗             ↘   ↙
           mirror pairs
```

More precisely:

``` python
check(p.left, q.right)
check(p.right, q.left)
```

At every level, we continue applying exactly the same rule.

------------------------------------------------------------------------

# 3. The Final Code

``` python
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:

        def check(p, q):
            if not p and not q:
                return True

            if not p or not q:
                return False

            return (
                p.val == q.val
                and check(p.left, q.right)
                and check(p.right, q.left)
            )

        return check(root, root)
```

------------------------------------------------------------------------

# 4. Why Do We Use `check(p, q)`?

Instead of writing a function that checks only one tree, we define:

``` python
def check(p, q):
```

This function answers a very specific question:

> **"Are the subtrees rooted at `p` and `q` mirror images of each
> other?"**

That is exactly the smaller version of the original problem.

The original problem asks:

> Is the entire tree symmetric?

We can convert that into:

> Is the tree rooted at `root` a mirror of itself?

Therefore:

``` python
check(root, root)
```

------------------------------------------------------------------------

# 5. Why `check(root, root)`?

This line can initially look strange:

``` python
return check(root, root)
```

We pass the **same root twice**.

Why?

Because we want to compare the tree with itself from opposite
directions.

Conceptually:

``` text
              root
             /    \
            L      R
```

We want:

``` text
L ↔ R
```

When we call:

``` python
check(root, root)
```

the first recursive comparison becomes:

``` python
check(root.left, root.right)
```

and:

``` python
check(root.right, root.left)
```

So the same tree is being treated as two mirror sides.

### Alternative

You could also write:

``` python
return check(root.left, root.right)
```

with appropriate handling for `root is None`.

But:

``` python
return check(root, root)
```

is elegant because the helper itself handles the complete symmetry
logic, including an empty tree.

------------------------------------------------------------------------

# 6. Condition #1 --- Both Nodes Are `None`

``` python
if not p and not q:
    return True
```

This is the first important base case.

It means:

> Both corresponding positions are empty.

Example:

``` text
p: None
q: None
```

There is nothing left to compare.

These positions are perfectly symmetric.

Therefore:

``` python
return True
```

### Why do we need this condition?

Consider:

``` text
      1
     / \
    2   2
```

When recursion reaches the leaves:

``` text
p = None
q = None
```

That is a valid mirror match.

Without this base case, the recursion would have no way to stop
successfully.

------------------------------------------------------------------------

# 7. Condition #2 --- Only One Node Is `None`

``` python
if not p or not q:
    return False
```

This condition handles:

``` text
p = None
q = actual node
```

or:

``` text
p = actual node
q = None
```

These positions cannot be mirror images because one side has a node
while the other side does not.

Example:

``` text
        1
       / \
      2   2
     /
    3
```

Compare the corresponding mirror positions:

``` text
left side:   3
right side:  None
```

That is asymmetric.

Therefore:

``` python
return False
```

------------------------------------------------------------------------

# 8. Why Is the Order of These Two Conditions Important?

We have:

``` python
if not p and not q:
    return True

if not p or not q:
    return False
```

Suppose:

``` text
p = None
q = None
```

The first condition catches it:

``` python
not p and not q
```

which is:

``` text
True and True
→ True
```

So we return:

``` python
True
```

If we only had:

``` python
if not p or not q:
    return False
```

then two empty positions would incorrectly be treated as asymmetric.

The logic is:

``` text
Both empty       → symmetric → True
Exactly one empty → asymmetric → False
Neither empty    → continue comparing
```

This is the complete structural logic for `None` cases.

------------------------------------------------------------------------

# 9. Why Do We Compare `p.val == q.val`?

Once we know both nodes exist:

``` python
if not p or not q:
    return False
```

we can safely access:

``` python
p.val
q.val
```

Now we need their values to match:

``` python
p.val == q.val
```

Example:

``` text
       5              5
      /                \
     3                  3
```

The values match.

Good.

But:

``` text
       5              5
      /                \
     3                  7
```

The structure might look mirrored, but:

``` python
3 != 7
```

so the trees cannot be symmetric.

------------------------------------------------------------------------

# 10. The Most Important Line

``` python
return p.val == q.val and check(p.left, q.right) and check(p.right, q.left)
```

This single line contains the entire definition of a mirror tree.

Break it into three requirements:

``` python
p.val == q.val
```

AND

``` python
check(p.left, q.right)
```

AND

``` python
check(p.right, q.left)
```

All three must be true.

In mathematical terms:

``` text
Mirror(p, q) =
    SameValue(p, q)
    AND
    Mirror(p.left, q.right)
    AND
    Mirror(p.right, q.left)
```

------------------------------------------------------------------------

# 11. Why `p.left` Is Compared With `q.right`

This is the key thing to remember during revision.

Suppose:

``` text
          p                 q
         / \               / \
        A   B             C   D
```

If `p` and `q` are mirror images:

``` text
A ↔ D
B ↔ C
```

Therefore:

``` python
check(p.left, q.right)
```

and:

``` python
check(p.right, q.left)
```

### Memory trick

Don't think:

> left with left, right with right

Think:

> **Mirror means opposite sides.**

So:

``` text
left  ↔ right
right ↔ left
```

------------------------------------------------------------------------

# 12. Why `and` Is Used

We need **every requirement** to be true.

For two subtrees to be mirrors:

1.  Their values must match.
2.  Their left/right structures must match as mirrors.
3.  Their right/left structures must match as mirrors.

Therefore:

``` python
p.val == q.val
and
check(p.left, q.right)
and
check(p.right, q.left)
```

If any one of them is false, the whole tree is not symmetric.

Python's `and` also short-circuits.

For example, if:

``` python
p.val != q.val
```

then Python does not need to perform the recursive calls because the
final result is already `False`.

------------------------------------------------------------------------

# 13. Full Recursive Thinking

Suppose we have:

``` text
          1
        /   \
       2     2
      / \   / \
     3   4 4   3
```

Start:

``` python
check(root, root)
```

Conceptually the comparison becomes:

``` python
check(root.left, root.right)
```

So:

``` text
2 ↔ 2
```

Values match.

Then:

``` python
check(p.left, q.right)
```

means:

``` text
3 ↔ 3
```

Then:

``` python
check(p.right, q.left)
```

means:

``` text
4 ↔ 4
```

Everything matches.

Therefore:

``` text
True
```

------------------------------------------------------------------------

# 14. Dry Run --- Symmetric Example

Tree:

``` text
          1
        /   \
       2     2
      / \   / \
     3   4 4   3
```

### Call 1

``` python
check(root, root)
```

Both point to `1`.

``` text
1 == 1
```

Continue.

### Call 2

``` python
check(root.left, root.right)
```

Compare:

``` text
2 ↔ 2
```

Values match.

### Left-side mirror

``` python
check(p.left, q.right)
```

Compare:

``` text
3 ↔ 3
```

Match.

Their children are:

``` text
None ↔ None
```

Both are `None`.

Return:

``` python
True
```

### Right-side mirror

``` python
check(p.right, q.left)
```

Compare:

``` text
4 ↔ 4
```

Match.

Again:

``` text
None ↔ None
```

Return:

``` python
True
```

All conditions are true.

Final result:

``` python
True
```

------------------------------------------------------------------------

# 15. Dry Run --- Asymmetric Example

Consider:

``` text
          1
        /   \
       2     2
      /       \
     3         4
```

Start comparing:

``` text
2 ↔ 2
```

Values match.

Then mirror comparison:

``` text
p.left ↔ q.right
```

which becomes:

``` text
3 ↔ 4
```

Now:

``` python
p.val == q.val
```

becomes:

``` python
3 == 4
```

which is:

``` python
False
```

Because the values do not match, this pair cannot be mirrors.

The whole expression becomes:

``` python
False and ... and ...
```

which is:

``` python
False
```

So the tree is not symmetric.

------------------------------------------------------------------------

# 16. Structural Asymmetry Example

Values can match but the structure can still be wrong.

``` text
          1
        /   \
       2     2
      /       \
     3         3
    /
   4
```

The values may look promising:

``` text
3 ↔ 3
```

But eventually we compare:

``` text
4 ↔ None
```

This reaches:

``` python
if not p or not q:
    return False
```

Therefore the tree is asymmetric.

This is why the algorithm checks both:

-   values
-   structure

------------------------------------------------------------------------

# 17. Why Recursion Is a Natural Fit

The definition of a mirror tree is recursive.

A pair of trees is a mirror if:

``` text
Their roots have equal values

AND

Their left subtree mirrors the other tree's right subtree

AND

Their right subtree mirrors the other tree's left subtree
```

Notice that the definition contains the same problem again:

``` text
Is this pair of subtrees a mirror?
```

That is exactly what recursion is good at.

We reduce:

``` text
Whole tree
```

into:

``` text
smaller pair of trees
```

and continue until we reach `None`.

------------------------------------------------------------------------

# 18. The Mental Model to Remember

When revising this problem, don't memorize the code first.

Memorize this:

``` text
              p                 q
             / \               / \
            L   R             L'  R'

Mirror requirement:

            L  ↔  R'
            R  ↔  L'
```

Then the code almost writes itself:

``` python
def check(p, q):

    # both empty
    if not p and not q:
        return True

    # only one empty
    if not p or not q:
        return False

    # values + cross-side recursive checks
    return (
        p.val == q.val
        and check(p.left, q.right)
        and check(p.right, q.left)
    )
```

------------------------------------------------------------------------

# 19. Why We Don't Need to Explicitly Check `root is None`

The code starts with:

``` python
return check(root, root)
```

Suppose:

``` python
root = None
```

Then this becomes:

``` python
check(None, None)
```

The first condition executes:

``` python
if not p and not q:
    return True
```

Therefore an empty tree is considered symmetric.

This is correct.

An empty tree has no violation of symmetry.

------------------------------------------------------------------------

# 20. Complexity

Let `n` be the number of nodes.

## Time Complexity

``` text
O(n)
```

Each node is visited at most once as part of the mirror comparison.

The algorithm does not repeatedly traverse the entire tree for each
node.

## Space Complexity

Because of recursion:

``` text
O(h)
```

where `h` is the height of the tree.

### Balanced tree

``` text
h = O(log n)
```

so recursion space is:

``` text
O(log n)
```

### Completely skewed tree

``` text
h = O(n)
```

so worst-case recursion space is:

``` text
O(n)
```

------------------------------------------------------------------------

# 21. Common Mistakes

## Mistake 1 --- Comparing left with left

Wrong:

``` python
check(p.left, q.left)
```

That checks corresponding positions, not mirror positions.

Correct:

``` python
check(p.left, q.right)
```

------------------------------------------------------------------------

## Mistake 2 --- Forgetting the second recursive check

Wrong:

``` python
return p.val == q.val and check(p.left, q.right)
```

This only checks one side.

You also need:

``` python
check(p.right, q.left)
```

Correct:

``` python
return (
    p.val == q.val
    and check(p.left, q.right)
    and check(p.right, q.left)
)
```

------------------------------------------------------------------------

## Mistake 3 --- Mishandling `None`

Wrong idea:

``` python
if not p or not q:
    return False
```

by itself.

That would incorrectly reject:

``` text
None ↔ None
```

Correct ordering:

``` python
if not p and not q:
    return True

if not p or not q:
    return False
```

------------------------------------------------------------------------

## Mistake 4 --- Accessing `.val` Before Checking `None`

Dangerous:

``` python
if p.val != q.val:
```

before checking whether `p` and `q` exist.

If:

``` python
p = None
```

then:

``` python
p.val
```

causes an error.

So first:

``` python
if not p or not q:
    return False
```

Then it is safe to access:

``` python
p.val
q.val
```

------------------------------------------------------------------------

# 22. A More Explicit Version for Learning

The compact solution is:

``` python
return (
    p.val == q.val
    and check(p.left, q.right)
    and check(p.right, q.left)
)
```

For learning, you can expand it:

``` python
def check(p, q):

    if not p and not q:
        return True

    if not p or not q:
        return False

    if p.val != q.val:
        return False

    if not check(p.left, q.right):
        return False

    if not check(p.right, q.left):
        return False

    return True
```

This version is useful while learning because every logical requirement
is visible.

Once the idea is comfortable, compressing it into the one-line return is
natural.

------------------------------------------------------------------------

# 23. How I Would Derive This During an Interview

Don't try to remember the final code immediately.

Start with the definition:

### Step 1 --- What does symmetric mean?

The left subtree must be the mirror of the right subtree.

### Step 2 --- What does mirror mean?

For two nodes `p` and `q`:

``` text
values equal
```

and:

``` text
p.left  ↔ q.right
p.right ↔ q.left
```

### Step 3 --- What happens with missing nodes?

``` text
None + None → True
None + node → False
node + None → False
```

### Step 4 --- Turn the definition into a function

``` python
def check(p, q):
```

### Step 5 --- Implement the base cases

``` python
if not p and not q:
    return True

if not p or not q:
    return False
```

### Step 6 --- Implement the recursive definition

``` python
return (
    p.val == q.val
    and check(p.left, q.right)
    and check(p.right, q.left)
)
```

### Step 7 --- Start by comparing the tree with itself

``` python
return check(root, root)
```

That's the entire derivation.

------------------------------------------------------------------------

# 24. The One-Line Revision Formula

Before solving this problem again, remember:

``` text
SYMMETRIC TREE

Compare two nodes p and q.

1. Both None       → True
2. One None        → False
3. Values differ   → False
4. Otherwise:
       left(p)  ↔ right(q)
       right(p) ↔ left(q)
```

Code skeleton:

``` python
def check(p, q):

    if not p and not q:
        return True

    if not p or not q:
        return False

    return (
        p.val == q.val
        and check(p.left, q.right)
        and check(p.right, q.left)
    )
```

Entry point:

``` python
return check(root, root)
```

------------------------------------------------------------------------

# 25. Final Mental Shortcut

If you have only **10 seconds** to revise this problem, remember:

> **Symmetric = mirror.**
>
> Compare two nodes.
>
> **Both empty → True.**
>
> **One empty → False.**
>
> **Values must match.**
>
> Then cross the children:
>
> **left ↔ right**
>
> **right ↔ left**

The key line to reconstruct from memory is:

``` python
check(p.left, q.right) and check(p.right, q.left)
```

Everything else follows from the definition of a mirror.
