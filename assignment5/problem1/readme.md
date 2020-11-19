
# Problem Description

Given n jobs, job i starts from S_i, finishes at T_i, and has the weight V_i. Two jobs are compatible if they don't overlap. Design an algorithm to find maximum weight subset of mutually compatible jobs. (Job i and job j are compatible if T_i == S_j)

# Input

There are n + 1 lines, the first line gives only one number `n`, the number of jobs. Each of the following lines gives three intergers S_i, T_i, V_i separated by space.

1 <= S_i < T_i <= 10000
1 <= V_i <= 10000
1 <= n <= 1000

Your code should read the input from standard input (e.g. 
using functions `input()/raw_input()` in Python and `cin/scanf` in C++).

# Output

One number in a line, the weight of the maximum weight compatible job subset.

Your code should write the output to standard output (e.g. using functions `print` in Python and `cout/printf` in C++).

# Requirement

Your algorithm should run in O(nlogn) time. 

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
If you submit via GitHub, make sure your file is located in directory `assignment5/problem1/solution.py` (for Python) or `assignment5/problem1/solution.cpp` (for C++).

