"""Virtualization Concurrency & Persistence:

There are 3 key ideas: virtualization, concurrency and persistence.
These determine how an OS works, how it decides what program to run next on a CPU, how it handles memory overload,
how machine monitors work, how to manage information on disks
and how to build a distributed system that works when parts have failed.
"""


"""Introduction to Operating Systems:
Let's learn 2 things:
- What happens when a program runs?
- Virtualizaiton


What happens when a program runs?
An OS does one very simple thing: it executes instructions.

Virtualization:
The primary way an OS operates is through a general technique called virtualization.
The OS takes a physical resource(processor, memory or a disk) and transforms it into a more general powerful easy-to-use virtual form of itself.
Thus we sometimes refer to the OS as a virtual machine.

In order to allow users to tell the OS what to do and thus make use of the features of the VM(such as running a program), the OS also
provides some interfaces(APIs) that you can call.  A typical OS exports a few hundred system calls available to all applications, 
provided in the standard library.

Virtualization allows many programs to run, which results in sharing the CPU.  This results in the OS sometimes being referred to as the resource manager.
The OS assumes the responsability of managing resources, doing so efficiently.
"""

"""Running cpu.c, Runninc multiple instances of cpu.c:

Here's a program that calls a Spin() function that repeatedly checks the time and returns once it has run for a second.
Then it prints out the string that the user passed in on the command line, and repeats forever.

# cpu.c
#include <stdio.h>
#include <stdlib.h>
#include "common.h"

int main(int argc, char *argv[])
{
    if (argc != 2) {
        fprintf(stderr, "usage: cpu <string>\n");
        exit(1);
    }
    char *str = argv[1];

    while (1) {
        printf("%s\n", str);
        Spin(1);
    }
    return 0;
}


The system begins running the program, which repeatedly checks the time until a second has elapsed.
Once a second has gone by, the code prints the input string passed in by the user(A).
This program will run forever until we control-c out


Let's try the same thing, but run many different instances of the same program.

./cpu A & ./cpu B & ./cpu C & ./cpu D &
this will output all 4 programs.  Even though we have only 1 processor, all 4 programs run at the same time.
The OS, with some help from the hardware allow many programs to run at once by virtualizing the CPU.
If more than 1 program runs at the same time, the program that runs is determined by a policy of the OS.
Policies are used in many different places within an OS to answer different varieties of questions
"""

"""Virtualizing memory:
The model of physical memory presented by modern machines is simple.
Memory is an array of bytes.
To read memory, one must specify the address to be able to access the data stored there.
To write memory, the data to be written to the address must also be given.

Each address accesses its own private virtual address space, which the OS maps onto physical memory of the machine.
Pysical memory is a shared resource, managed by the OS.  This is accomplished through virtualization.
"""
