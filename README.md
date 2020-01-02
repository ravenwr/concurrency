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

### Event driven programming:

    Every interaction that we do can be called an event

    Callbacks are used for anything where and action is async

### Sequential download (sequentialCalc.py)

    Execution Time: 1.2621049881

### Concurrent download (concurrentCalc.py)

    Execution Time: 0.5961260795593262


## Concurrency and I/O bottlenecks

    Multiple Actor: Different processes and threads make progeress on their own tasks, multi threads run simultaneously. 

    Shared resources: Represents the memory, disk and other resources, Utilized by actors to perform tasks

    Rules: Set of rules essentially followed by concurrent systems,if ignored, programs would tear themsleves apart

#### I/O bottlenecks:

    Where your computer spends more time waiting on various imputs and outputs than it does processing the informaiton

#### Parallelism:

    Execute 2 or more actions simultaniously, make progress on two or more things simultaniously, need to run codes on multiprocessors.

    CPU bottleneck = inverse of IO bottlenecks: Performs heavy number crunching, Performs computationally expensive tasks

        Programs executing rate is bound by the speed of CPU

            -i.e. If used faster CPU - observe direct increase in the speed. 

            - Use CPU-bound bottleneck:
                
                While rate of processing data outweighs rate of requesting data

### Different architectural styles: 

#### Uniform Memory access pattern (UMA)

    Shared memory space:

        Utilized in a uniform manner, By any number of processing cores

    Also known as Symmetric Shared memory Multiprocessors (SMP)

##### UMA Advantages: 

All RAM access takes exact same amount of time, cache is coherent and consistent, hardware design is simpler

##### UMA Disadvantages:

FEature one memory bus from which all systems acccess memory creating scaling isssues

#### Non-uniform Memory access (NUMA):

Style in which some memory access is faster than others depending on the processor and due to the location of processor with respect to memory

##### NUMA advantages:

SCALABLE

##### NUMA disadvantages:

Non-deterministic memory - quick access times or far longer? 


## Life of a thread

#### Thread class definition:

 Python thread class takes in 5 args:

    1) Group: reserved for future extension

    2) Target: callable object to be invoked by run method. DEfaults to None, if nothing is passed here than nothing is ran. 

    3) Name: Name of thread to be run

    4) args: Argument tuple for target

    5) kwargs: Keyword arguments to invoke base class constructor

Threads can exist in 5 states:

    1) Running --> in this state the thread makes progress and is executing tasks. From here it can go into dead or not running

    2) Not running --> paused in some way

    3) Runnable --> All resources that it needs in order to proceed

    4) Starting --> new thread state

    5) Ended --> Can die naturally or be killed

    
    When we create a thread we have no allocated any resources for it yet:

        It exists in no state (not initialized), can only be started or stopped. 


#### Posix Threads: 
 
     Implemented to follow - IEEE POSIX 1003.1c standard

#### Windows threads:

    Chosen by microsoft to implement low-level threads against other threads

#### Daemonizing threads:

    Daemon threads are essentially threads that have no defined endpoint, they will continue forever until your program quits. 

        - They will send signal to service registry

        - start when our application starts

        - remain active in the background

        - send update without any intervention

        - get killed when instance shuts down











