""""Test the relative speed of iteration tool alternatives."""

import sys, perfmon.timer2 as timer

reps = 10000
repslist = list(range(reps)) # hoist out, to make 2x/3x comparable

def forLoop():
    res = []
    for x in repslist:
        res.append(abs(x))
    return res

def listComp():
    return [abs(x) for x in repslist]

def mapCall():
    return list(map(abs, repslist))

def genExpr():
    # list required to force results for a generator
    return list(abs(x) for x in repslist)

def genFunc():
    def gen():
        for x in repslist:
            yield abs(x)
    return list(gen())

print(sys.version)

for test in (forLoop, listComp, mapCall, genExpr, genFunc):
    print(timer.bestoftotal(test, _reps1=5,_reps=1000))
    (bestof, (total, result)) = timer.bestoftotal(test, _reps1=5,
                                                  _reps=1000)
    print('%-9s: %.5f => [%s...%s]' % (test.__name__, bestof, result[0], result[-1]))







