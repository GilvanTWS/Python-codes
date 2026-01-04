# 🐍 Python Studies & Exercises

This repository contains **independent Python scripts** created for learning, practice, and problem-solving.
Each file focuses on a specific concept, algorithm, or small challenge.

The repository is continuously updated as new scripts are added.

---

## 📂 Repository Structure

- Each `.py` file is **self-contained**
- Scripts may cover:
  - Basic Python syntax
  - Logic and algorithms
  - Data structures
  - Small challenges and exercises
  - Experiments and tests

---

## 📌 Scripts Overview

Below is a list of the scripts currently available in this repository.
This section will be updated whenever a new file is added.

### 🔹 `average_odds.py`
**Description:**  
This program was created with the intention of solving the challenge of fixing the code provided on the Discord server 'Brazilian Programmers'. It consists of taking a piece of code that was wrong (I will provide the challenge message below) and correcting it.

**Challenge proposed:**
Description
Correct the following code and point out its errors and why.

This code should take a list[int] as a parameter and return the arithmetic mean of the odd numbers contained therein. If there are none, return -1.

Example

Input | Output

[1, 2, 3, 4, 6] | 4.0

[2, 4, 3, 7] | 5.0

[8, 10, 2] | -1.0

Bugged Code
This is the code, and it's in the Python programming language.

You must:
Identify the errors;
Point out where the bugs are and how to correct them;
Correct the code.

def averageOdds(numbers: list[int]) -> float:
    total = 0
    count = 0

    for n in numbers:
        if n % 2:
            total += n
            count += 1

    return total / count

Rules
You cannot change the current code structure;

You cannot change the programming language.
