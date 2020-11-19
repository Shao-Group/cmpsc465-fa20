
# Problem Description

Given an undirected graph G = (V,E) with edge length l(e) > 0 for any e in E. Use Kruskal's algorithm to find the minimum spanning tree of G.

# Input

The graph has `n` vertices and `m` edges.
There are m + 1 lines, the first line gives two numbers `n`,`m` describing the number of vertices, the number of edges. Each of the following lines contains three integers `a`, `b` and `c`, meaning there is an edge (a,b) belong to E and the length of the edge is c. All the numbers in a line are separated by space. There could be multiple edges between two vertices. (`1 <= a,b <= n`) 


You can assume that 1 <= n <= 1000, 1 <= m <= 2000, and the length of edge is in the range of [1, 1000]. 

Your code should read the input from standard input (e.g. 
using functions `input()/raw_input()` in Python and `cin/scanf` in C++).

# Output

One number, the sum of the edges in the minimum spanning tree.

Your code should write the output to standard output (e.g. using functions `print` in Python and `cout/printf` in C++).

# Requirement

Your algorithm should run in O(mlogn) time. 

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
If you submit via GitHub, make sure your file is located in directory `assignment5/problem2/solution.py` (for Python) or `assignment5/problem2/solution.cpp` (for C++).

