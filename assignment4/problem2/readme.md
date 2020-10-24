# Problem Description

A subsequence is palindromic if it is the same whether read left to right or right to left. For
instance, the sequence
A, C, B, D, B, D, C, A, A, A, A, D, C, G
has many palindromic subsequences, including A, C, B, C, A and A, A, A, A (on the other hand,
the subsequence A, C, D is not palindromic). Devise an algorithm that takes a sequence x[1 . . . n]
and returns the length of the longest palindromic subsequence. Its running time should be O(n^2).

# Input

There is only one line containing the sequence x. There are `n` chars in a line without any space seprated them. 

1 <= `n` <= 1000. You can assume that all the chars are uppercase letters from A to Z.

Your code should read the input from standard input (e.g. 
using functions `input()/raw_input()` in Python and `cin/scanf` in C++).

# Output

One line, contain the the length of the longest palindromic subsequence.

Your code should write the output to standard output (e.g. using functions `print` in Python and `cout/printf` in C++).

# Requirement

Your algorithm should run in O(nm) time. 

Time limtation: 5 seconds.

Memory limitation: 1.0 GB.

# Environment

Your code will be running on Ubuntu 18.04.5.

Now only accept C++ and Python2/Python3 code, g++ version 7.5.0 and Python versions are Python 2.7.17 and Python 3.6.9.

# Examples and Testing

Some examples (e.g., input-x.txt and output-x.txt, x = 1, 2) are provided. 
A figure corresponding input-1 can be found in this repo too.
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
If you submit via GitHub, make sure your file is located in directory `assignment4/problem2/solution.py` (for Python) or `assignment4/problem2/solution.cpp` (for C++).

