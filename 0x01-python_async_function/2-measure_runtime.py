#!/usr/bin/env python3
"""measure the total execution time"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures the time it takes to run a function """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    stop = time.time()
    return start/stop
