# tests/test_filter.py

import pytest
from corstream import Stream

@pytest.mark.asyncio
async def test_filter_sync():
    result = []
    
    async def collect(x):
        result.append(x)
        
    await (
        Stream.from_iterable([1, 2, 3, 4])
        .filter(lambda x: x % 2 == 0)
        .for_each(collect)
    )
    
    assert result == [2, 4]
    
    
@pytest.mark.asyncio
async def test_filter_async():
    async def is_even(x):
        return x % 2 == 0
    
    result = []
    
    async def collect(x):
        result.append(x)
        
    await (
        Stream.from_iterable([5, 6, 7])
        .filter(is_even)
        .for_each(collect)
    )
    
    assert result == [6]