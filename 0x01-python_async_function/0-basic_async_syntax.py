#!/usr/bin/env python3
'''Task wait_random module.
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Waits for a random number of seconds.
    '''
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
