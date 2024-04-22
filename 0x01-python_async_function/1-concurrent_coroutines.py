#!/usr/bin/env python3
'''Task wait_n module.
'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes wait_random n times.
    '''
    tasks = []
    for i in range(n):
        task = wait_random(max_delay)
        tasks.append(task)

    return [await task for task in asyncio.as_completed(tasks)]
