# Common Issues

## Input

Your code should read the input from standard input (e.g. 
using functions `input()/raw_input()` in Python and `cin/scanf` in C++). Do not use file I/O in your code. 

There is an example of reading a line of integers separated by space in Python3.

```
line = input()
line = line.strip().split(' ')
array = []
for number in line:
	array.append(int(number))

```

Ther
## Output

Your code should write the output to standard output (e.g. using functions `print` in Python and `cout/printf` in C++). The same as input, don't open a file to write the answer.


## Test
When your code is done, you can use command line to run it and test it. Run your code with the command below, and you can type a sample input, then there will be an output given by your program showed in the command line.

```
python ./solution.py
```

Some examples (e.g., input-x.txt and output-x.txt, x = 1, 2, ...) are provided. 
For Python code, try the following to test your code with given test cases.
```
python ./solution.py < input-x.txt > my-output-x.txt
```
For C++ code, try the following to test your code.
```
g++ -o mybinary solution.cpp
./mybinary < input-x.txt > my-output-x.txt
```

Your output `my-output-x.txt` needs to be *matched exactly* to the given `output-x.txt`.
On Unix-based systems you can use `diff` to compare them:
```
diff my-output-x.txt output-x.txt
```
On Windows you can use `fc` to compare them:
```
fc my-output-x.txt output-x.txt
```
If nothing returns from either `diff` or `fc` then it means your code passed this example.

And sometimes it showed that there is a newline at the end of file or a space at the end of a line cause your output not exactly the same as the sample output. Don't worry, the autograder can ignore them. Have a newline at end of output or not won't affect your score.

## 

# Submission

It's OK to submit your code multiple times, and there some types of the response you may be given by the gradescope.


## Autograder failed
"The autograder failed to execute correctly. Contact your course staff for help in debugging this issue. Make sure to include a link to this page so that they can help you most effectively."

In most cases, it's because the name or the path of your submit file is not correct. 

If you want to upload a single file, make sure the file is named as `solution.py` (for Python) or `solution.cpp` (for C++).

If you submit via GitHub, make sure your file is located in directory `assignment1/problem1/solution.py` (for Python) or `assignment1/problem1/solution.cpp` (for C++). (The number will be different for different problems.)


## Wrong Answer

"Test Failed: Output did not match expected." 

If you get test failed for test cases, it's because the output of your program is not correct. Maybe your code gives the wrong output or there is an error when your code is running.

If all of the test cases fail, it means your code is not working even on the simplest test case. You may try to test it on your machine first. If only some of the test cases fail, maybe there are some situations you didn't consider.

## Time out
"Test Failed: [Errno 32] Broken pipe"

"Test Failed: Command '...' timed out after 5 seconds"

These two different results both represent your program time out. Usually, test cases 6-10 will be larger than first test cases. If the result is time out, try to improve your code to save the running time. 

Sometimes it also happens although your code is running in required time complexity due to the machine where the autograder is running is busy. You can rerun the autograder for your submission or submit it again.
