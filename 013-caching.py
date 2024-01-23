from functools import lru_cache

@lru_cache(maxsize=128)
def steps_to(stair):
    if stair == 1:
        return 1
    if stair == 2:
        return 2
    if stair == 3:
        return 4
    
    return steps_to(stair - 1) + steps_to(stair - 2) + steps_to(stair - 3)

import time

t0 = time.perf_counter()
print(steps_to(32))
print(steps_to.cache_info())
t1 = time.perf_counter()

print(t1 - t0)