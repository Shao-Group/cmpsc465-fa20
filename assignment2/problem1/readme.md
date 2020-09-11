# Problem Description

Given an array A with n distinct integers, design an algorithm to count the number of pairs (A[i],A[j]) satisfying that i < j and A[i] > A[j].

# Input

Two lines, the first line gives only one number `n`, the number of integers in the array. And the second line gives `n` numbers which are
the `n` integers in the array. All numbers are separated by space.

You can assume that 0 <= n <= 10000, and that each number in the arrarys
are in the range of [-2147483648, 2147483647]. 

Your code should read the input from standard input (e.g. 
using functions `input()/raw_input()` in Python and `cin/scanf` in C++).

# Output

One number in a line, representing the number of pairs (A[i],A[j]) satisfying that i < j and A[i] > A[j].

Your code should write the output to standard output (e.g. using functions `print` in Python and `cout/printf` in C++).

# Requirement

Your algorithm should run in O(nlogn) time. You are not allowed to call any in-built sort function.

Time limtation: 5 seconds.

Memory limitation: 1.0 GB.

# Environment

Your code will be running on Ubuntu 18.04.5.

Now only accept C++ and Python2/Python3 code, g++ version 7.5.0 and Python versions are Python 2.7.17 and Python 3.6.9.

# Examples and Testing

Some examples (e.g., input-x.txt and output-x.txt, x = 1, 2) are provided. 
For Python code, try the following to test your code
```
python ./solution.py < input-x.txt > my-output-x.txt
```
For C++ code, try the following to test your code
```
g++ -o mybinary solution.cpp
./mybinary < input-x.txt > my-output-x.txt
```

Your output `my-output-x.txt` needs to be *match exactly* to the given `output-x.txt`.
On Unix-based systems you can use `diff` to compare them:
```
diff my-output-x.txt output-x.txt
```
On Windows you can use `fc` to compare them:
```
fc my-output-x.txt output-x.txt
```

# Submission

If you want to upload a single file, make sure the file is named as `solution.py` (for Python) or `solution.cpp` (for C++).
If you submit via GitHub, make sure your file is located in directory `assignment2/problem1/solution.py` (for Python) or `assignment2/problem1/solution.cpp` (for C++).

# Hints

Reuse the code you write for assignment 1.

