# MatrixEchelon: Recursive Gaussian Elimination 🧮

A Python-based tool designed to transform matrices into their **Row Echelon Form (REF)**. This project implements the Gaussian Elimination algorithm using a recursive approach to handle row pivoting, normalization, and elimination.

## 🚀 Project Overview
The core of this project is the `esglaonar` (echelon) function, which systematically processes a matrix to create a staircase pattern of zeros. This is a fundamental step in solving systems of linear equations, finding matrix ranks, or calculating determinants.

### Key Features:
* **Recursive Algorithm:** Clean and logical implementation of the elimination process.
* **Automatic Pivoting:** Searches for non-zero candidates in lower rows to swap if the current pivot is zero.
* **Pivot Normalization:** Scales rows so that each leading coefficient (pivot) becomes 1.
* **Row Operations:** Efficiently performs row subtractions to eliminate values below the pivot.
* **Dynamic Input:** Uses the `yogi` library for intuitive user data entry.



## 🛠️ Technologies Used
* **Python 3**: Main programming language.
* **NumPy**: Used for high-performance matrix manipulation and vectorized row operations.
* **Yogi**: A utility library for simplified data reading from standard input.

## 📈 Algebraic Logic
The algorithm follows the standard Gaussian procedure:
1. **Identify Pivot:** Find a non-zero element in the current column.
2. **Swap Rows:** If the current position is zero, swap with a row below that has a non-zero value.
3. **Normalize:** Multiply the row by the reciprocal of the pivot.
4. **Eliminate:** Subtract multiples of the pivot row from all rows below to create zeros in the current column.
5. **Recurse:** Move to the next diagonal element and repeat.



## 💻 Setup & Usage

1.  **Prerequisites:**
    Ensure you have the required libraries installed:
    ```bash
    pip install numpy yogi
    ```

2.  **Execution:**
    Run the script and follow the prompts to enter your matrix dimensions and values:
    ```bash
    python matrix_echelon.py
    ```

3.  **Input Format:**
    * Enter the number of rows and columns.
    * Enter the matrix elements row by row (integers or floats).

## 👥 Authors
Developed as a practical implementation of fundamental Linear Algebra algorithms.

---
*Note: This project serves as an educational tool for understanding the mechanics of matrix decomposition and numerical methods.*
