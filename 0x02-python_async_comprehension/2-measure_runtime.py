#!/usr/bin/env python3
"""Task measure_runtime
"""

import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """return time to execute 4 times async_comprehension
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    result = time.time() - start_time
    return result
