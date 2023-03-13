#!/bin/env/python
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
total = np.zeros(1)
number = np.zeros(1)
if rank != 0:
    number[0] = int(rank)
    print("Rank %s sending number %s" % (rank, number))
    comm.Send(number, dest=0)
    comm.Reduce(number, total, op=MPI.SUM, root=0)
if rank == 0:
    print("Rank %s received the sum of those numbers: %s" % (rank, total))