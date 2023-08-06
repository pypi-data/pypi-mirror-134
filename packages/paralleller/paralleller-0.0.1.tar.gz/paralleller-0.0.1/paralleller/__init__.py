"""paralleller namespace."""

from .jl import JoblibPool
from .mpi import MPIPool
from .serial import SerialPool
from .multiprocessing import MultiPool
from importlib_metadata import PackageNotFoundError, version

__author__ = "Rontomai"
__email__ = "rontomai@gmail.com"

# Used to automatically set version number from github actions
# as well as not break when being tested locally
try:
    __version__ = version(__package__)  # type: ignore
except PackageNotFoundError:  # pragma: no cover
    __version__ = "0.0.1"


import sys
from log import get_logger
log = get_logger(__name__)



def choose_pool(mpi=False, processes=1, **kwargs):
    """
    Choose between the different pools given options from, e.g., argparse.
    Parameters
    ----------
    mpi : bool, optional
        Use the MPI processing pool, :class:`~schwimmbad.mpi.MPIPool`. By
        default, ``False``, will use the :class:`~schwimmbad.serial.SerialPool`.
    processes : int, optional
        Use the multiprocessing pool,
        :class:`~schwimmbad.multiprocessing.MultiPool`, with this number of
        processes. By default, ``processes=1``, will use the
        :class:`~schwimmbad.serial.SerialPool`.
    **kwargs
        Any additional kwargs are passed in to the pool class initializer
        selected by the arguments.
    """

    if mpi:
        if not MPIPool.enabled():
            raise SystemError("Tried to run with MPI but MPIPool not enabled.")

        pool = MPIPool(**kwargs)
        log.info("Running with MPI on {0} cores".format(pool.size))
        return pool

    elif processes != 1 and MultiPool.enabled():
        log.info("Running with MultiPool on {0} cores".format(processes))
        return MultiPool(processes=processes, **kwargs)

    else:
        log.info("Running with SerialPool")
        return SerialPool(**kwargs)
