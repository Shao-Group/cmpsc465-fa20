# Common Issues


## Read the problem description carefully

Lots of issues we see can be avoided by doing so.

## Input

Your code should read the input from standard input (e.g.  using `input()/raw_input()` 
in Python or `cin/scanf` in C++). Do not use file I/O in your code. 
Don't put any prompting string in it, as this string will be printed to standard output.
For example, this is wrong: `input("please input: ")`.

Here is an example of reading a line of integers separated by space in Python3.

```
line = input()
line = line.strip().split(' ')
array = []
for number in line:
	array.append(int(number))

```

## Output

Your code should write the output to standard output (e.g. using
`print` in Python and `cout/printf` in C++). Don't write to any file.


## Testing

Make sure you follow the commands provided in the problem description to test
your code. Submit your code after you pass all given test cases.

## Submission

For now you may submit your code multiple times.
The possible responses you may get and how you could revise your code are given below.


### Autograder failed

"The autograder failed to execute correctly. Contact your course staff for help
in debugging this issue. Make sure to include a link to this page so that they
can help you most effectively."

In most cases, this is because the name or the path of your submitted file is
not correct.

### Wrong Answer

"Test Failed: Output did not match expected." 

If your code fail on all test cases, likely you haven't passed the given test cases.
If a subset of test cases fail, then your code haven't considered all situations;
you may want to generate your own test cases to debug.

### Time out

"Test Failed: [Errno 32] Broken pipe"

"Test Failed: Command '...' timed out after 5 seconds"

These two different results both represent your program times out (some of our test
cases are large). If this happens, try to improve the efficiency of your code. For example, try to convert input strings into integers, string operations are inefficient comparing to operations with integers. There is a sample below:

```
if Array1[pointer1] >= Array2[pointer2]: 
	Output_array.append(Array2[pointer2]) 
```
Use an integer array to save the results is more efficient than using string. And there is a bad sample using string to save the results.

```
if Array1[pointer1] >= Array2[pointer2]: 
	Output_string = Output_string + ' ' + str(Array2[pointer2])
```
Although very rare, 
it may also happen that your code runs within the required time
but you get a time-out error. You can try to rerun the autograder or resubmit.
