# LeetCode Journey

> A structured collection of my LeetCode solutions, problem-solving
> notes, and revision material.

This repository documents my journey of solving **Data Structures &
Algorithms problems on LeetCode**.

The goal is not just to collect accepted solutions, but to understand
**how I arrived at each solution**, why the algorithm works, what each
condition means, and how to reconstruct the solution later without
memorizing code.

---

## Why This Repository?

I don't want my LeetCode preparation to become:

```text
Problem → Copy solution → Submit → Forget
```

Instead, I want the process to be:

```text
Understand
   ↓
Identify the pattern
   ↓
Derive the solution
   ↓
Implement
   ↓
Analyze complexity
   ↓
Document the reasoning
   ↓
Revise later
   ↓
Solve independently
```

The most important part of this repository is therefore **the reasoning
behind the code**.

---

## What Each Solution Contains

For problems where detailed notes are created, the documentation focuses
on:

- Problem understanding
- Core intuition
- How to identify the underlying pattern
- Step-by-step derivation
- Why each line of code exists
- Why each condition is checked
- Recursion / iteration flow
- Dry runs
- Common mistakes
- Time complexity
- Space complexity
- Interview-style explanation
- Quick revision notes
- Mental shortcuts for reconstructing the solution

The objective is to make every solution **reconstructable**, rather than
something that has to be memorized.

---

## Repository Structure

```text
leetcode-journey/
│
├── README.md
│
├── Arrays/
│   ├── Two_Sum.py
│   └── ...
│
├── Strings/
│   ├── ...
│
├── Linked_List/
│   ├── ...
│
├── Stack/
│   ├── ...
│
├── Queue/
│   ├── ...
│
├── Binary_Tree/
│   ├── Symmetric_Tree.py
│   ├── Symmetric_Tree.md
│   └── ...
│
├── Binary_Search/
│   └── ...
│
├── Heap/
│   └── ...
│
├── Graph/
│   └── ...
│
├── Dynamic_Programming/
│   └── ...
│
├── Backtracking/
│   └── ...
│
└── Patterns/
    ├── Recursion.md
    ├── Two_Pointers.md
    ├── Sliding_Window.md
    ├── Binary_Search.md
    ├── DFS.md
    ├── BFS.md
    └── Dynamic_Programming.md
```

> The structure may evolve as more problems and patterns are added.

---

# Problem-Solving Roadmap

The journey is organized around common DSA patterns rather than only
individual problems.

### 1. Arrays

Focus areas:

- Traversal
- Hash maps / hash sets
- Prefix sums
- Two pointers
- Sliding window
- Sorting
- Kadane's algorithm
- Intervals

---

### 2. Strings

Focus areas:

- Character frequency
- Hashing
- Two pointers
- Sliding window
- String construction
- Palindromes
- Anagrams

---

### 3. Linked Lists

Focus areas:

- Fast & slow pointers
- Reversal
- Merging
- Cycle detection
- Dummy nodes
- Recursive linked-list manipulation

---

### 4. Stack & Queue

Focus areas:

- Monotonic stack
- Parentheses
- Expression problems
- BFS
- Deques
- Next greater element

---

### 5. Binary Trees

Focus areas:

- DFS
- BFS
- Recursion
- Tree traversal
- Tree height/depth
- Lowest Common Ancestor
- Path problems
- Symmetry
- Binary Search Trees

---

### 6. Binary Search

Focus areas:

- Search space reduction
- Lower/upper bound
- Search on answer
- Rotated arrays
- Monotonic predicates

---

### 7. Heaps / Priority Queues

Focus areas:

- Top K
- K-way merge
- Scheduling
- Running median
- Min heap / max heap

---

### 8. Graphs

Focus areas:

- DFS
- BFS
- Connected components
- Cycle detection
- Topological sorting
- Union Find
- Shortest paths
- Minimum spanning tree

---

### 9. Backtracking

Focus areas:

- Subsets
- Permutations
- Combinations
- Constraint search
- Decision trees
- Pruning

---

### 10. Dynamic Programming

Focus areas:

- 1D DP
- 2D DP
- State definition
- State transitions
- Memoization
- Tabulation
- Space optimization

---

# Pattern Recognition

A major goal of this repository is learning to recognize **patterns**.

For example:

Problem Clue Pattern to Consider

---

Sorted array + pair Two Pointers
Contiguous subarray Sliding Window / Prefix Sum
"Top K" Heap
Shortest path in unweighted graph BFS
Explore all possibilities Backtracking
Tree relationships DFS / BFS
Repeated subproblems Dynamic Programming
Monotonic search space Binary Search
Matching nested structures Stack
Cycle in linked list Fast & Slow Pointers

The objective is to eventually look at a new problem and ask:

> **"What pattern is this?"**

before asking:

> **"What code should I write?"**

---

# Example: Symmetric Tree

One of the documented problems is:

**LeetCode 101 --- Symmetric Tree**

The important insight is:

```text
Symmetric Tree
      ↓
Mirror
      ↓
Compare two nodes
      ↓
left  ↔ right
right ↔ left
```

The recursive relationship becomes:

```python
check(p.left, q.right)
check(p.right, q.left)
```

The important lesson is not memorizing:

```python
return p.val == q.val and ...
```

It is understanding:

> **A symmetric tree is a tree that is its own mirror.**

This distinction is what makes the solution reusable when encountering
similar recursive problems.

---

# Revision Strategy

For every solved problem, revision should happen at multiple levels.

### Level 1 --- 10 Seconds

Remember the key pattern.

Example:

```text
Symmetric Tree → Mirror → Cross comparison
```

---

### Level 2 --- 1 Minute

Reconstruct the algorithm without looking at the code.

Ask:

1.  What is the problem really asking?
2.  What invariant must always hold?
3.  What are the base cases?
4.  What smaller problem do I recurse/iterate on?

---

### Level 3 --- 5 Minutes

Explain the complete solution:

```text
Problem
  ↓
Observation
  ↓
Pattern
  ↓
Algorithm
  ↓
Correctness
  ↓
Complexity
```

---

### Level 4 --- Coding

Close the solution and implement it from scratch.

If the implementation fails, inspect **the reasoning**, not just the
syntax.

---

# My Rule for Solving Problems

For every problem, try to answer these questions before coding:

### 1. What is the input?

What data structure am I given?

```text
Array?
String?
Linked List?
Tree?
Graph?
Matrix?
```

### 2. What exactly must be returned?

```text
Boolean?
Integer?
Array?
Node?
Count?
Path?
```

### 3. What constraints matter?

Constraints often determine the possible complexity.

For example:

```text
n ≤ 20
```

may allow exponential approaches.

While:

```text
n ≤ 10^5
```

usually requires something close to:

```text
O(n)
O(n log n)
```

---

### 4. What pattern does this resemble?

Ask:

```text
Hashing?
Two pointers?
Sliding window?
Binary search?
DFS?
BFS?
Heap?
Greedy?
Backtracking?
DP?
```

---

### 5. What is the invariant?

An invariant is something that remains true while the algorithm runs.

Finding the invariant often makes the implementation much easier.

---

### 6. What are the edge cases?

Always consider:

```text
Empty input
One element
Duplicate values
All values equal
Already sorted
Reverse sorted
Maximum/minimum values
Missing children
Disconnected graph
```

depending on the problem.

---

# Progress Tracking

As the repository grows, problems can be tracked using categories such
as:

Category Solved Notes

---

Arrays --- ---
Strings --- ---
Linked Lists --- ---
Stack / Queue --- ---
Trees --- ---
Binary Search --- ---
Heap --- ---
Graphs --- ---
Backtracking --- ---
Dynamic Programming --- ---

The exact numbers will be updated as the journey progresses.

---

# What "Solved" Means Here

A problem is not considered fully learned just because the code was
accepted.

A stronger definition is:

```text
Accepted
   ↓
Can explain the idea
   ↓
Can explain why it works
   ↓
Can explain every important condition
   ↓
Can analyze complexity
   ↓
Can reproduce the solution later
```

Only then does the problem become part of the long-term DSA toolkit.

---

# Solution Documentation Philosophy

Each detailed `.md` file should answer:

> **"If I completely forget this problem six months from now, can I read
> this note and reconstruct the solution?"**

That means the notes should explain **why**, not just **what**.

Bad documentation:

```text
Use recursion.
Check left and right.
Return the result.
```

Better documentation:

```text
A symmetric tree is its own mirror.

Therefore, instead of comparing corresponding
children, compare opposite children:

left of p  ↔ right of q
right of p ↔ left of q

Both nodes being None means the positions match.
Exactly one being None means the structures differ.
```

The second explanation teaches the underlying pattern.

---

# Long-Term Goal

The goal of this repository is to build a personal **DSA pattern
library**.

Eventually, when encountering a new problem, the process should become:

```text
New Problem
     ↓
Understand constraints
     ↓
Identify pattern
     ↓
Recall similar problems
     ↓
Derive algorithm
     ↓
Implement
     ↓
Test edge cases
     ↓
Analyze complexity
     ↓
Document
     ↓
Revise
```

The end goal is not to solve a large number of LeetCode problems
blindly.

The goal is to develop the ability to:

> **Recognize a problem, derive the right approach, and implement it
> independently.**

---

## Journey

```text
                 DSA JOURNEY

      Learn
        ↓
   Solve Problem
        ↓
 Understand Why
        ↓
 Document
        ↓
    Revise
        ↓
 Solve Again
        ↓
 Recognize Pattern
        ↓
 Apply to New Problem
        ↓
      Repeat
```

---

## Principle

> **Don't memorize solutions. Build the ability to derive them.**

---

## Language

Primary language:

```text
Python
```

Solutions may be accompanied by detailed Markdown explanations and dry
runs.

---

## Current Notes

- [LeetCode 101 --- Symmetric Tree](./Binary_Tree/Symmetric_Tree.md)

---

## License

This repository is for personal learning and educational purposes.
