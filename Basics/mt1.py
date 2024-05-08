
#### MULTITHREADING ####

import os
print(os.name)

import sys
print(sys.platform)

import platform
print(platform.platform())

## To get the number of cores
# Cores is the complete execution unit capable of independently executing instructions.
# Each core can execute its own set of instructions, enabling parallel processing of tasks.
import multiprocessing as mp
print(mp.cpu_count()) 

## Threading
import threading
activeThreads = threading.active_count()
print('Number of active threads: ', activeThreads)

## Execution Time of a Program
import time
startTime = time.time()
print('Start Time: ', startTime)

n = 1

print('Program started')
print('Waiting for %d seconds'%(n))

time.sleep(n) # Sleep for n seconds
print('Total time taken: %f'%(time.time() - startTime))

## Get the working dir
print(os.getcwd())
