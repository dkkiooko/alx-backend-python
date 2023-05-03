#!/usr/bin/env python3
"""take random numbers"""
import asyncio
import random
import typing

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """ get list from generator """
    numbers = [i async for i in async_generator()]
    return numbers
