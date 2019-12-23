# Concurrency

## Thread:

    - ordered stream of instructions, live in processes.

    - Able to interact with shared resources, can share memory

    - multithreading- a processor being able to execute multiple thread concurently. 

    User level threads: Used to create, run and kill for al tasks (i.e. Python)

    Kernal level threads: Very low level threads acting on behalf of the perating system. 

#### Advantages of threading:

    They are lightweight(memory), speed up blocking, I/O bound programs, shared resources (easier communication)

#### Disadvantages:

    Global Interpreter lock (GIL), Do not implement code subject to race conditions
    
## Processes and event driven programming:

    Processes are similar in nature to threads only they are not bound to a single CPU core, able to work on multiple things at the same time. 

    They can become multi threaded

#### Advantages of processes:

    Make use of multi core processors, Handle CPU intensive tasks, Side step limitations of GIL by spawning multiple processes, crashing processes will not kill enitre program.

#### Disadvatages:

    No shared resources between prcesses, implement some form of IPC requiring more memory

## Event driven programming:

    Every interaction that we do can be called an event

    Callbacks are used for anything where and action is async

## Sequential download (sequentialCalc.py)

    Execution Time: 1.2621049881

## Concurrent download (concurrentCalc.py)

    Execution Time: 0.5961260795593262