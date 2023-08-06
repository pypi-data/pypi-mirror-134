#!/usr/bin/env python3

import asyncio
import functools

async def make_async(func, loop=None, executor=None, *args, **kwargs):
    if not loop:
        loop = asyncio.get_running_loop()
    async def run_func_as_async(func, loop, executor, *args, **kwargs):
        func_return = await loop.run_in_executor(
            executor, 
            functools.partial(
                func, *args, **kwargs
            )
        )
        return func_return
    return await run_func_as_async(func, loop, executor, *args, **kwargs)