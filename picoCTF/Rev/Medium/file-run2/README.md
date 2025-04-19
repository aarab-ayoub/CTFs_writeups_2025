# file-run2 - Basic Challenge Writeup

## Challenge Description
Another program, but this time, it seems to want some input. What happens if you try to run it on the command line with input "Hello!"?

## Hint
Try running it and add the phrase "Hello!" with a space in front (i.e. "./run Hello!")

## Solution

This challenge builds slightly on the previous one (file-run1) by requiring us to provide a command-line argument to the program.

### Step 1: Download the Program
First, I downloaded the provided program file.

### Step 2: Make the File Executable
Similar to the previous challenge, I needed to make the file executable with the chmod command:

```bash
chmod +x ./run
```

### Step 3: Execute the Program with the Required Argument
Based on the challenge description and hint, the program expects an input argument of "Hello!". I executed the program with this argument:

```bash
./run Hello!
```

Upon execution with the correct argument, the program output the flag.

## Flag
```
picoCTF{F1r57_4rgum3n7_be0714da}
```

## Learning Points
- How to pass command-line arguments to executable programs
- Building on basic command-line skills
- Understanding that programs can be designed to expect specific inputs
- The importance of reading challenge descriptions carefully to identify required inputs
