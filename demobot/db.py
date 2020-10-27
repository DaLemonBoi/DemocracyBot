import asyncio
from typing import Optional, Awaitable

import aiomysql as sql

from demobot import config

_pool_task: Optional[Awaitable[sql.Pool]] = None


async def pool() -> sql.Pool:
    global _pool_task
    if _pool_task is None:
        # store the task so that get_pool can't be called while the pool is being created
        _pool_task = asyncio.create_task(sql.create_pool(
            host=config.DB_HOST, port=config.DB_PORT,
            user=config.DB_USER, password=config.DB_PASSWORD,
            db=config.DB_DEFAULT_DATABASE, loop=asyncio.get_event_loop(),
        ))
    return await _pool_task


async def close():
    global _pool_task
    if _pool_task is not None:
        p = await _pool_task
        p.close()
        await p.wait_closed()


async def connection() -> sql.Connection:
    p = await pool()
    return p.acquire()
