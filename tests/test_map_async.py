# tests/test_map_async.py

import pytest
import asyncio
from corstream import Stream

@pytest.mark.asyncio
async def test_map_async_basic():
    async def double(x):
        await asyncio.sleep(0.01)
        return x * 2
    
    result = []
    
    await (
        Stream.from_iterable([1, 2, 3])
        .map_async(double, max_concurrent=2)
        .for_each(lambda x: result.append(x))
    )
    
    assert sorted(result) == [2, 4, 6]
    
    
@pytest.mark.asyncio
async def test_map_async_order_independence():
    async def echo_with_delay(x):
        await asyncio.sleep(0.02 if x == 2 else 0.01)
        return x
    
    result = []
    
    await (
        Stream.from_iterable([1, 2, 3])
        .map_async(echo_with_delay, max_concurrent=3)
        .for_each(lambda x: result.append(x))
    )
    
    # Items may arrive out of order depending on delay
    assert sorted(result) == [1, 2, 3]
    assert set(result) == {1, 2, 3}
    
@pytest.mark.asyncio
async def test_map_async_error_propagation():
    async def risky(x):
        if x == 2:
            raise ValueError("Bad input!")
        return x
    
    stream = Stream.from_iterable([1, 2, 3]).map_async(risky)
    
    with pytest.raises(ValueError, match="Bad input!"):
        await stream.for_each(lambda x: None)
        
@pytest.mark.asyncio
async def test_map_async_invalid_concurrency():
    async def noop(x):
        return x
    
    with pytest.raises(ValueError):
        Stream.from_iterable([1]).map_async(noop, max_concurrent=0)