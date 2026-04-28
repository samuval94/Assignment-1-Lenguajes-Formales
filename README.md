# Assignment 1 - Failure Function
### Samuel Valencia Montoya - Matias Zapata Rojas
School of Applied Sciences and Engineering – Eafit
Professor: Cesar Guerra Villa
## Versions

| Component        | Version / Details                     |
|-----------------|---------------------------------------|
| Operating System | Windows 11    |
| Programming Language | Python 3.14.0                   |
| Compiler / Runtime | CPython 3.14.0             |

---

## How to Run

**1. Make sure Python 3 is installed:**

```bash
python3 --version
```

You should see `Python 3.14.0` or higher.

**2. Navigate to the `assignment1/` folder:**

```bash
cd assignment1
```

**3. Run the program:**

```bash
failure_function.py
```

The program will print the failure function table for each of the following patterns:

- `abababaab` — Exercise 3.4.3 a)
- `aaaaaa` — Exercise 3.4.3 b)
- `abbaabb` — Exercise 3.4.3 c)

**4. To use the function in your own code:**

```python
from failure_function import failure_function, solution_3_4_3
# Compute the failure function for a pattern
f = failure_function("ababaa")
# f = [0, 0, 0, 1, 2, 3, 1]
# f[1]=0, f[2]=0, f[3]=1, f[4]=2, f[5]=3, f[6]=1
# Print the full table
print(f)
```

---

## Algorithm Explanation

The **failure function** is defined in
**Figure 3.19 (page 137)** of:

> Aho, Lam, Sethi, Ullman. *Compilers: Principles, Techniques, and Tools*. 2nd ed. Pearson/Addison Wesley, 2007.

### What it does

Given a pattern `b[1] b[2] ... b[n]`, the failure function `f(s)` computes,
for each state `s` (from 1 to n), the **length of the longest proper suffix**
of `b[1..s]` that is also a **prefix** of the pattern.

For example, for the pattern `ababaa`:

| s    | 1 | 2 | 3 | 4 | 5 | 6 |
|------|---|---|---|---|---|---|
| b[s] | a | b | a | b | a | a |
| f(s) | 0 | 0 | 1 | 2 | 3 | 1 |

`f(5) = 3` means the longest proper suffix of `ababa` that is also a prefix is `aba` (length 3).

### Why it is used

During the scanning phase of a compiler, tokens must be recognized efficiently from the source text. The failure function is used to **build the transition function** of the pattern-matching automaton. When a mismatch occurs at state `s`, instead of restarting from zero, the automaton jumps to state `f(s)`, preserving the longest valid partial match found so far.
