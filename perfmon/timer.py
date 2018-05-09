"""
Homegrown timing tools for function calls.
Does total time, best-of time, and best-of-totals time
"""

import time, sys

timer = time.clock if sys.platform[:3] == 'win' else time.time

def total(reps, func, *pargs, **kargs):
    """
    Total time to run func() reps times
    :param reps:
    :param func:
    :param pargs:
    :param kargs:
    :return:
    """
    repslist = list(range(reps))
    start = timer()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return (elapsed, ret)

def bestof(reps, func, *pargs, **kargs):
    """
    Quickest func() among reps runs.
    :param reps:
    :param func:
    :param pargs:
    :param kargs:
    :return: (best time, last result)
    """

    best = 2 ** 32  #136 years
    print("Best of {} {} {}".format(func.__name__, pargs, kargs))
    for i in range(reps): # not changing to list b/c range usage not timed here
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        print("--> elapsed({}): {}".format(i, elapsed))
        if elapsed < best:
            best = elapsed
        return (best, ret)

def bestoftotal(reps1, reps2, func, *pargs, **kargs):
    """
    Best of totals
    :param reps1:
    :param reps2:
    :param func:
    :param pargs:
    :param kargs:
    :return: (best of reps1 runs of (total of reps2 runs of func))
    """
    return bestof(reps1, total, reps2, func, *pargs, **kargs)


