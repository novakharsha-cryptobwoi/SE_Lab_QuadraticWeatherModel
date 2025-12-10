# SE_Lab_QuadraticWeatherModel
1️⃣ “Implement weather modeling* using the quadratic solution in stages”
Ignore the “weather modeling” story for a moment.
Think of it as:

Write a program that uses a quadratic formula (something like
y = ax² + bx + c) to compute some value (maybe temperature, rainfall, etc.).

You don’t need real weather science. It’s just a math formula program dressed up as a “weather model”.

2️⃣ “in stages: hard-coding variables, keyboard input, read from a file, for a single set of input, multiple sets of inputs”
This is the real requirement.

They want you to evolve your program in steps:

✅ Stage 1: Hard-coding variables
You directly put values in the code.

Example (in any language):

python
Copy code
a = 1.0
b = 2.0
c = 3.0
x = 4.0
# compute y using quadratic formula or y = ax*x + b*x + c
No input from the user. Everything is fixed inside the program.

✅ Stage 2: Keyboard input
Now modify the program so it:

Asks the user to type values.

Example:

python
Copy code
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
x = float(input("Enter x: "))
You now compute using user-entered values, not hard-coded ones.

✅ Stage 3: Read from a file – single set of input
Next version: the program doesn’t ask the user.
Instead, it reads the values from a file (like input.txt).

input.txt might contain one line, e.g.
1.0 2.0 3.0 4.0 → representing a b c x

Your program:

Opens the file

Reads one line

Extracts the 4 numbers

Uses them to compute the result

This is one set of input from the file.

✅ Stage 4: Read from a file – multiple sets of inputs
Now extend it again:

input.txt might have many lines, e.g.:

Copy code
1.0 2.0 3.0 4.0
0.5 1.0 0.0 2.0
2.0 3.5 4.1 1.2
Each line is one case (one weather scenario).

Your program should:

Loop over all lines

For each line, read a b c x

Compute and print the result

So now, your program handles multiple inputs automatically from a file.

3️⃣ “save all versions, debug, fix problems, create a Github account”
This line is about good programming practice:

Save all versions
Don’t overwrite the old ones.
Example:

weather_v1_hardcoded.py

weather_v2_keyboard.py

weather_v3_file_single.py

weather_v4_file_multi.py

Debug, fix problems

Run each program.

If there are errors (wrong output / crashes), fix them.

Make sure each stage works correctly.

Create a GitHub account

Go to GitHub, sign up.

Optionally:

Create a repository like weather-quadratic-assignment

Upload all versions of your code there.

They’re teaching you both programming and workflow:

Write code

Improve it in steps

Save versions

Use GitHub to store/share your work

TL;DR — What you’re expected to do
Write a quadratic-based “weather” program with:

Version 1: hard-coded values

Version 2: read from keyboard

Version 3: read one set from a file

Version 4: read many sets from a file (loop)

Save each version as a separate file/program.

Test and debug them.

Create a GitHub account and (most likely) upload these files.
