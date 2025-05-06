# tests/test_map.py

import pytest
import asyncio
from corstream import Stream

@pytest.mark.asyncio
async def test_map_sync_function():
    result = []
    
    async def collect(x):
        result.append(x)
        
    await (
        Stream.from_iterable([1, 2, 3])
        .map(lambda x: x * 2)
        .for_each(collect)
    )
    
    assert result == [2, 4, 6]
    
@pytest.mark.asyncio
async def test_map_async_function():
    async def double(x):
        await asyncio.sleep(0.001)
        return x * 2
    
    result = []
    
    async def collect(x):
        result.append(x)
        
    await (
        Stream.from_iterable([4, 5])
        .map(double)
        .for_each(collect)
    )
    
    assert result == [8, 10]