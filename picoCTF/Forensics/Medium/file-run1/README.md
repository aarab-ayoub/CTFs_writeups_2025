# file-run1 - Basic Challenge Writeup

## Challenge Description
A program has been provided to you, what happens if you try to run it on the command line?

## Hints
1. To run the program at all, you must make it executable (i.e. `$ chmod +x run`)
2. Try running it by adding a '.' in front of the path to the file (i.e. `$ ./run`)

## Solution

This challenge is extremely straightforward and focuses on basic command-line skills. The solution involves simply running an executable file.

### Step 1: Download the Program
First, I downloaded the provided program file.

### Step 2: Make the File Executable
Before running any program on Linux/Unix systems, you need to ensure it has execution permissions. I used the `chmod` command to add execute permissions:

```bash
chmod +x ./run
```

### Step 3: Execute the Program
Then I executed the program by running:

```bash
./run
```

The program immediately output the flag:

```
picoCTF{U51N6_Y0Ur_F1r57_F113_e5559d46}
```

## Flag
`picoCTF{U51N6_Y0Ur_F1r57_F113_e5559d46}`

## Learning Points
- Basic command line usage in Linux/Unix systems
- Understanding file permissions (execute permissions are needed to run programs)
- How to run executable files from the current directory using `./`
- Some CTF challenges can be very simple, testing fundamental skills rather than complex techniques
