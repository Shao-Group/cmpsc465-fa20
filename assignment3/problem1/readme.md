# Problem Description

Given a directed graph G = (V, E), find the number of connected components in G.

# Input

The graph has `n` vertices and `m` edges.
There are m + 1 lines, the first line gives two numbers `n` and `m`, describing the number of vertices and edges. Each of the following lines contains two  numbers `a` and `b` meaning there is an edge (a,b) belong to E. All the numbers in a line are separated by space. (`1 <= a,b <= n`)

You can assume that 2 <= n <= 10000, 1 <= m <= 50000.

Your code should read the input from standard input (e.g. 
using functions `input()/raw_input()` in Python and `cin/scanf` in C++).

# Output

One number representing the number of connected components in the graph.


Your code should write the output to standard output (e.g. using functions `print` in Python and `cout/printf` in C++).

# Requirement

Your algorithm should run in O(|V| + |E|) time. 

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
If you submit via GitHub, make sure your file is located in directory `assignment3/problem1/solution.py` (for Python) or `assignment3/problem1/solution.cpp` (for C++).

# Hints

Use adjacency list to store all the edges.


