
# Problem Description

Give a directed graph G = (V,E), find the maximum network flow from `s` to `t`. 

# Input

There are m + 1 lines, the first line gives two numbers `n` and `m`, `n` is the number of vertices, `m` is the number of edges. 
Each of the following lines gives three intergers a, b, c separated by space which means there is an edge from a to b with capacity c. There could be multiple edges between two vertices. (1 <= a,b <= n)
The source vertex `s` is always 1, and the sink vertex `t` is n.

1 <= n <= 100

1 <= m <= 300

1 <= a,b <= n

1 <= c <= 1000

Your code should read the input from standard input (e.g. 
using functions `input()/raw_input()` in Python and `cin/scanf` in C++).

# Output

One number in a line, the maximum netfork flow from s to t.

Your code should write the output to standard output (e.g. using functions `print` in Python and `cout/printf` in C++).

# Requirement


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
If you submit via GitHub, make sure your file is located in directory `assignment6/problem1/solution.py` (for Python) or `assignment6/problem1/solution.cpp` (for C++).

